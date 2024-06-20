import pandas as pd
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from functools import partial
import statistics
import plotly.graph_objs as go

class Home:
    def __init__(self, master):
        self.master = master
        self.f1 = Frame(master, width=500, height=500, background="black")
        self.f1.pack()
        label = Label(self.f1, text="Election Visualization", font=("Times New Roman", 30, "bold"))
        label.pack(pady=20)
        button = Button(self.f1, text="Click Me", font=("Times New Roman", 20), command=self.result_page)
        button.pack()
        self.img = ImageTk.PhotoImage(Image.open("election_india.jpeg"))
        img_lbl = Label(self.f1, image=self.img)
        img_lbl.pack(side="bottom", fill="both", expand="yes")

    def result_page(self):
        self.f1.pack_forget()
        self.f2 = Frame(self.master, background="black", width=300, height=550)
        self.f2.pack(side="left", fill="y", anchor='n')
        self.f3 = Frame(self.master, background="black")
        self.f3.pack(expand=True, fill='both')

        self.l2 = Label(self.f2, text="Upload Files", bg="black", fg="white", font=("Times New Roman", 20))
        self.l2.pack(fill="x", anchor='n', pady=5)

        self.b2 = Button(self.f2, text="Upload", font=("Times New Roman", 20), command=self.upload_file)
        self.b2.pack(fill="x", anchor='n', pady=10)

        self.dropdown_label = Label(self.f2, text="Select State", bg="black", fg="white", font=("Times New Roman", 20))
        self.dropdown_label.pack(fill="x", anchor='n', pady=5)

        self.selected_state = StringVar(self.f2)
        self.selected_state.set("Choose a state")

        self.dropdown_menu = OptionMenu(self.f2, self.selected_state, "")
        self.dropdown_menu.pack(fill="x", anchor='n', pady=10)

        self.dropdown_label2 = Label(self.f2, text="Select Year", bg="black", fg="white", font=("Times New Roman", 20))
        self.dropdown_label2.pack(fill="x", anchor='n', pady=5)

        self.selected_year = StringVar(self.f2)
        self.selected_year.set("Choose a year")

        self.dropdown_menu2 = OptionMenu(self.f2, self.selected_year, "")
        self.dropdown_menu2.pack(fill="x", anchor='n', pady=10)

        self.dropdown_label3 = Label(self.f2, text="Select Party", bg="black", fg="white", font=("Times New Roman", 20))
        self.dropdown_label3.pack(fill="x", anchor='n', pady=5)

        self.selected_party = StringVar(self.f2)
        self.selected_party.set("Choose a party")

        self.dropdown_menu3 = OptionMenu(self.f2, self.selected_party, "")
        self.dropdown_menu3.pack(fill="x", anchor='n', pady=10)

        self.plot_button = Button(self.f2, text="Show Graph", font=("Times New Roman", 20), command=self.show_graph)
        self.plot_button.pack(fill="x", anchor='n', pady=20)

        self.selected_state.trace('w', self.on_state_change)

    def upload_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.data = pd.read_csv(file_path)
            self.data['year'] = self.data['year'].astype(int)  # Convert year to int
            self.update_dropdowns(self.data)

    def update_dropdowns(self, data):
        required_columns = ['st_name', 'year', 'partyname']
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

    def show_graph(self):
        state = self.selected_state.get()
        year = self.selected_year.get()
        party = self.selected_party.get()

        if year == "Choose a year" or party == "Choose a party":
            # If either year or party is not selected, show a message or handle as needed
            for widget in self.f3.winfo_children():
                widget.destroy()
            Label(self.f3, text="Please select a valid year and party", bg="black", fg="white").pack(anchor="center")
            return

        filtered_data = self.data[(self.data['st_name'] == state) &
                                  (self.data['year'] == int(year)) &
                                  (self.data['partyname'] == party)]

        if not filtered_data.empty:
            self.plot(filtered_data)
        else:
            for widget in self.f3.winfo_children():
                widget.destroy()
            Label(self.f3, text="No data available for the selected criteria", bg="black", fg="white").pack(anchor="center")

    def plot(self, data):
        for widget in self.f3.winfo_children():
            widget.destroy()

        fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(10, 6))

        # Plotting the bar chart for statistics
        mean_votes = statistics.mean(data['totvotpoll'])
        mean_electors = statistics.mean(data['electors'])

        ax1.bar(['Total Votes Polled', 'Electors'], [mean_votes, mean_electors], alpha=0.7, color=['blue', 'green'])
        ax1.set_xlabel('Categories', fontsize=12)
        ax1.set_ylabel('Values', fontsize=12)
        ax1.set_title(f'Election Statistics: {self.selected_state.get()} - {self.selected_party.get()}', fontsize=12)
        ax1.grid(True)

        # Plotting the bar chart for state-year ranges
        state_year_ranges = data.groupby('st_name')['year'].agg(['min', 'max'])
        state_year_ranges['max'] += 1  # Adding 1 to max year for better visual range
        for state, (min_year, max_year) in state_year_ranges.iterrows():
            state_data = data[data['st_name'] == state]
            ax2.bar(state_data['st_name'], state_data['year'], label=state, alpha=0.7)

        ax2.set_xlabel('States', fontsize=12)
        ax2.set_ylabel('Year', fontsize=12)
        ax2.set_title(f'Election Results by Year: {self.selected_state.get()} - {self.selected_party.get()}', fontsize=12)
        ax2.grid(True)

        # Adjusting layout and rotation of x-axis ticks
        plt.setp(ax2.get_xticklabels(), rotation=45, ha='right', fontsize=10)
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

