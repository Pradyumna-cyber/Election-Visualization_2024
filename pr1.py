from tkinter import *
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from functools import partial
from PIL import ImageTk,Image

class Home:
    def __init__(self, master):
        self.master = master
        self.f1 = Frame(master, width=500, height=500, background="black")
        self.f1.pack()
        
        label = Label(self.f1, text="Election Visualization", font=("Times New Roman", 30, "bold"), bg="black", fg="white")
        label.pack(pady=20)

        button = Button(self.f1, text="Click Me", font=("Times New Roman", 20), command=self.result_page)
        button.pack()
        self.img = ImageTk.PhotoImage(Image.open("election_india.jpg"))
        img_lbl = Label(self.f1, image=self.img)
        img_lbl.pack(side="bottom", fill="both", expand="yes")


    def result_page(self):
        self.f1.pack_forget()
        
        self.f2 = Frame(self.master, background="black")
        self.f2.pack(side="left", fill="y", padx=20, pady=20)

        self.f3 = Frame(self.master, background="black")
        self.f3.pack(expand=True, fill='both', padx=20, pady=20)

        self.l2 = Label(self.f2, text="Upload Files", bg="black", fg="white", font=("Times New Roman", 20))
        self.l2.pack(fill="x", pady=5)

        self.b2 = Button(self.f2, text="Upload", font=("Times New Roman", 20), command=self.upload_file)
        self.b2.pack(fill="x", pady=10)

        self.dropdown_label = Label(self.f2, text="Select State", bg="black", fg="white", font=("Times New Roman", 20))
        self.dropdown_label.pack(fill="x", pady=5)

        self.selected_state = StringVar(self.f2)
        self.selected_state.set("Choose a state")

        self.dropdown_menu = OptionMenu(self.f2, self.selected_state, "")
        self.dropdown_menu.pack(fill="x", pady=10)

        self.dropdown_label2 = Label(self.f2, text="Select Year", bg="black", fg="white", font=("Times New Roman", 20))
        self.dropdown_label2.pack(fill="x", pady=5)

        self.selected_year = StringVar(self.f2)
        self.selected_year.set("Choose a year")

        self.dropdown_menu2 = OptionMenu(self.f2, self.selected_year, "")
        self.dropdown_menu2.pack(fill="x", pady=10)

        self.dropdown_label3 = Label(self.f2, text="Select Party", bg="black", fg="white", font=("Times New Roman", 20))
        self.dropdown_label3.pack(fill="x", pady=5)

        self.selected_party = StringVar(self.f2)
        self.selected_party.set("Choose a party")

        self.dropdown_menu3 = OptionMenu(self.f2, self.selected_party, "")
        self.dropdown_menu3.pack(fill="x", pady=10)

        self.plot_button = Button(self.f2, text="Show Graph", font=("Times New Roman", 20), command=self.show_graph)
        self.plot_button.pack(fill="x", pady=20)

        self.selected_year.trace('w', self.on_year_change)
        self.selected_party.trace('w', self.on_party_change)
        self.selected_state.trace('w', self.on_state_change)

    def upload_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.data = pd.read_csv(file_path)
            self.data['year'] = self.data['year'].astype(int)  # Convert year to int
            self.update_dropdowns(self.data)

    def update_dropdowns(self, data):
        required_columns = ['st_name', 'year', 'partyname', 'totvotpoll']
        if all(column in data.columns for column in required_columns):
            # Update state dropdown
            st_names = data['st_name'].unique()
            self.update_option_menu(self.dropdown_menu, self.selected_state, st_names)
        else:
            missing_columns = [column for column in required_columns if column not in data.columns]
            print(f"Columns {missing_columns} not found in the data")

    def update_option_menu(self, option_menu, variable, values):
        menu = option_menu['menu']
        menu.delete(0, 'end')
        for value in values:
            menu.add_command(label=value, command=partial(self.set_variable, variable, value))

    def set_variable(self, variable, value):
        variable.set(value)

    def on_state_change(self, *args):
        state = self.selected_state.get()
        filtered_data = self.data[self.data['st_name'] == state]

        if not filtered_data.empty:
            years = filtered_data['year'].unique()
            parties = filtered_data['partyname'].unique()
            self.update_option_menu(self.dropdown_menu2, self.selected_year, years)
            self.update_option_menu(self.dropdown_menu3, self.selected_party, parties)
            self.show_graph()  # Update graph immediately when state changes
        else:
            self.update_option_menu(self.dropdown_menu2, self.selected_year, ["Choose a year"])
            self.update_option_menu(self.dropdown_menu3, self.selected_party, ["Choose a party"])

            # Clear the graph area when no data is available
            self.clear_graph()

    def on_year_change(self, *args):
        if self.selected_state.get() != "Choose a state":
            self.show_graph()

    def on_party_change(self, *args):
        if self.selected_state.get() != "Choose a state" and self.selected_year.get() != "Choose a year":
            self.show_graph()

    def clear_graph(self):
        for widget in self.f3.winfo_children():
            widget.destroy()

    def show_graph(self):
        state = self.selected_state.get()
        year = self.selected_year.get()
        party = self.selected_party.get()
        self.clear_graph()
        if year == "Choose a year" or party == "Choose a party":
            # If either year or party is not selected, clear the graph area
            self.clear_graph()
            Label(self.f3, text="Please select a valid year and party", font=("Times New Roman", 14)).pack(anchor="center")
            return

        filtered_data = self.data[(self.data['st_name'] == state) &
                                (self.data['year'] == int(year)) &
                                (self.data['partyname'] == party)]

        if not filtered_data.empty:
            self.plot(filtered_data)
        else:
            self.clear_graph()
            Label(self.f3, text="No data available for the selected criteria", font=("Times New Roman", 14)).pack(anchor="center")

    def plot(self, data):
        self.clear_graph()

        fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, figsize=(12, 15))

        # Plotting the pie chart for party-wise results
        party_counts = data['partyname'].value_counts()
        ax1.pie(party_counts, labels=party_counts.index, autopct='%1.1f%%', startangle=140)
        ax1.set_title(f'Party-wise Election Results: {self.selected_state.get()} - {self.selected_year.get()}', fontsize=15)

        # Calculating y-axis limits for the second plot based on each state's year range
        state_year_ranges = data.groupby('st_name')['year'].agg(['min', 'max'])
        state_year_ranges['max'] += 1  # Adding a slight buffer to the maximum year for better visualization

        # Plotting the bar graph (data['year'])
        for state, (min_year, max_year) in state_year_ranges.iterrows():
            state_data = data[data['st_name'] == state]
            ax2.bar(state_data['st_name'], state_data['year'], label=state, alpha=0.7)

        ax2.set_xlabel('States', fontsize=18)
        ax2.set_ylabel('Year', fontsize=18)
        ax2.set_title(f'Election Results by Year: {self.selected_state.get()} - {self.selected_party.get()}', fontsize=22)
        ax2.grid(True)

        # Set y-axis limits for the second plot based on the calculated ranges
        ax2.set_ylim(state_year_ranges['min'].min() - 1, state_year_ranges['max'].max() + 1)

        # Adjusting layout and rotation of x-axis ticks for ax2
        plt.setp(ax2.get_xticklabels(), rotation=45, ha='right', fontsize=14)

        # Plotting the pie chart for st_name and totvotpoll
        st_name_counts = data.groupby('st_name')['totvotpoll'].sum()
        ax3.pie(st_name_counts, labels=st_name_counts.index, autopct='%1.1f%%', startangle=140)
        ax3.set_title(f'Total Votes Polled by State: {self.selected_state.get()} - {self.selected_year.get()}', fontsize=15)

        # Adjusting layout for ax3
        ax3.axis('equal')  # Equal aspect ratio ensures the pie chart is circular

        # Adjust overall layout of the figure
        plt.tight_layout()

        # Creating canvas and displaying the plot
        canvas = FigureCanvasTkAgg(fig, master=self.f3)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both', expand=True)


   


def center_window(window, width=1080, height=720):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')

root = Tk()
root.title("India Elections 2023")
root.geometry("1080x720")
root.configure(background="black")
center_window(root, 1080, 720)
a = Home(root)
root.mainloop()