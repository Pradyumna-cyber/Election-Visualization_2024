from tkinter import Tk, Label, Frame, Button, filedialog
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from customtkinter import *

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Lok Sabha Election 2024 Analysis")
        self.root.geometry("1000x800")

        set_appearance_mode("light")
        self.center_window()

        # Initialize data to None
        self.data = None

        # Load the image
        path = "/Users/pradyumnadeepakaher/Desktop/project_py/arr.png"
        img = Image.open(path)
        img = img.resize((20, 20), Image.LANCZOS)
        self.photo = CTkImage(img)

        self.home_page()

    def home_page(self):
        self.clear_window()
        self.info = '''The 2024 Indian Lok Sabha election, spanning seven phases from April 19 to June 1, emerged as a watershed moment in the country's democratic history with unprecedented voter participation exceeding 968 million. Despite Prime Minister Narendra Modi's Bharatiya Janata Party (BJP) aiming for a third consecutive term, it experienced a setback, securing 240 seats compared to 303 in 2019. The National Democratic Alliance (NDA), comprising BJP and regional allies, retained a majority with 293 seats, relying on coalition support. The Indian National Developmental Inclusive Alliance (INDIA), led by the Indian National Congress (INC), secured 234 seats, with INC alone winning 99 seats to reclaim the status of official opposition after a decade. The election highlighted significant engagement from women voters and revolved around critical issues like economic policies, social welfare programs, and political pluralism.
        '''
        self.l1 = CTkLabel(self.root, text="🇮🇳 Lok Sabha Election 2024 🇮🇳", font=("Arial", 24, "bold"), justify="center")
        self.l1.pack(padx=20, pady=20)
        self.l2 = CTkLabel(self.root, text=self.info, wraplength=680, justify="left", font=("Arial", 15))
        self.l2.pack(pady=20, padx=20)
        self.analysis_label = CTkLabel(self.root, text="Click here for detailed analysis", font=("Arial", 14, "bold"))
        self.analysis_label.pack()
        self.analysis_button = CTkButton(self.root, text="Analysis", command=self.show_analysis, fg_color="#0000BF")
        self.analysis_button.pack(pady=20)

    def center_window(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = 800
        window_height = 600
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def uploadfile(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if file_path:
            try:
                self.data = pd.read_csv(file_path)
                # Check and clean data if necessary
                self.data['Margin'] = pd.to_numeric(self.data['Margin'], errors='coerce')  # Convert to numeric

                if self.data['Margin'].isnull().any():
                    raise ValueError("Margin column contains non-numeric values.")

                self.plot_party_votes()  # Initial plot
            except Exception as e:
                self.show_error_message(f"Error loading data: {str(e)}")

    def plot_party_votes(self):
        if self.data is not None:
            try:
                party_votes = self.data.groupby('Leading Party')['Margin'].sum().sort_values(ascending=False)

                fig, ax = plt.subplots(figsize=(10, 6))
                sns.barplot(x=party_votes.index, y=party_votes.values, palette='viridis', ax=ax)
                ax.set_title('Votes by Party')
                ax.set_xlabel('Party')
                ax.set_ylabel('Total Votes (Margin)')
                plt.xticks(rotation=90)

                self.update_plot(fig)
            except Exception as e:
                self.show_error_message(f"Error plotting party votes: {str(e)}")

    def plot_votes_pie_chart(self):
        if self.data is not None:
            try:
                party_votes = self.data.groupby('Leading Party')['Margin'].sum().sort_values(ascending=False)

                plt.figure(figsize=(10, 8))
                wedges, texts, autotexts = plt.pie(party_votes, labels=None, autopct='%1.1f%%', startangle=140, wedgeprops=dict(edgecolor='w'))
                plt.title('Votes Distribution by Party', pad=20)
                plt.axis('equal')

                plt.legend(labels=party_votes.index, loc='center left', bbox_to_anchor=(1, 0.5), fontsize='medium')

                self.update_plot(plt.gcf())  # Update plot in the same frame
            except Exception as e:
                self.show_error_message(f"Error plotting pie chart: {str(e)}")

    def show_error_message(self, message):
        error_label = CTkLabel(self.root, text=message, fg="red")
        error_label.pack()

    def update_plot(self, fig):
        if hasattr(self, 'canvas'):
            self.canvas.get_tk_widget().destroy()
        self.canvas = FigureCanvasTkAgg(fig, master=self.plot_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill="both", expand=True)

    def show_analysis(self):
        self.analysis_page()

    def analysis_page(self):
        self.clear_window()

        # Main frame
        self.main_frame = CTkFrame(self.root)
        self.main_frame.pack(fill="both", expand=True)

        # Header frame
        header_frame = CTkFrame(self.main_frame)
        header_frame.pack(fill="x")

        # Icon button in header frame
        icon_button = CTkButton(header_frame, image=self.photo, text="", width=30, height=30)
        icon_button.pack(side="left", padx=(0, 10))

        # "Analysis Page" label in header frame
        label = CTkLabel(header_frame, text="Analysis Page", font=("Arial", 15, "bold"))
        label.pack(side="left")

        # Content frame
        self.side_frame = CTkFrame(self.main_frame, width=300)
        self.side_frame.pack(side="left", fill="y")

        # Upload label in content frame
        upload = CTkLabel(self.side_frame, text="Upload Files", font=("Arial", 12, "bold"))
        upload.pack(pady=(5, 0))

        # Upload button in content frame
        upload_btn = CTkButton(self.side_frame, text="Click here", command=self.uploadfile, fg_color="#FF5733")
        upload_btn.pack()

        # Analysis buttons
        analysis_buttons = [
            ("Party Votes", self.plot_party_votes),
            ("Votes Pie Chart", self.plot_votes_pie_chart),
            ("Compare Candidates", self.compare_candidates),  # Include button for comparing candidates
            ("Highest & Lowest Margin", self.plot_highest_lowest_margin),  # New button for highest and lowest margin
            ("Histogram of Margin", self.plot_margin_histogram),  # Button for histogram of margin
            ("Boxplot of Margin by Party", self.plot_boxplot_margin_by_party),  # New button for boxplot by party
            ("Top 10 Trailing Parties by Votes", self.plot_top_trailing_parties_votes),  # New button for top trailing parties by votes
            ("Top 10 Trailing Parties by Seats", self.plot_top_trailing_parties_seats)  # New button for top trailing parties by seats
            # Add other analysis functions as needed
        ]

        for text, command in analysis_buttons:
            button = CTkButton(self.side_frame, text=text, command=command, bg_color="#007BFF")
            button.pack(pady=5, fill="x")

        # Back button
        back_button = CTkButton(self.side_frame, text="Back to Home", command=self.home_page, bg_color="#6C757D")
        back_button.pack(pady=(20, 10), fill="x")

        # Plot frame for graphs
        self.plot_frame = CTkFrame(self.main_frame)
        self.plot_frame.pack(side="right", fill="both", expand=True)

    def compare_candidates(self):
        if self.data is not None:
            try:
                rahul_entries = self.data[self.data['Leading Candidate'] == 'RAHUL GANDHI']
                modi_entries = self.data[self.data['Leading Candidate'] == 'NARENDRA MODI']
                amit_entries = self.data[self.data['Leading Candidate'] == 'AMIT SHAH']

                # Get the votes for Rahul Gandhi, Narendra Modi, and Amit Shah
                rahul_votes = rahul_entries['Margin'].values
                modi_votes = modi_entries['Margin'].values[0] if not modi_entries.empty else 0
                amit_votes = amit_entries['Margin'].values[0] if not amit_entries.empty else 0

                # Get the original constituency names for Rahul Gandhi
                rahul_constituencies = list(rahul_entries['Constituency'])

                # Get the original constituency name for Narendra Modi
                modi_constituency = modi_entries['Constituency'].values[0] if not modi_entries.empty else "Modi Constituency"

                # Get the original constituency name for Amit Shah
                amit_constituency = amit_entries['Constituency'].values[0] if not amit_entries.empty else "Amit Shah Constituency"

                # Combine the data
                data_to_plot = pd.DataFrame({
                    'Candidate': ['Rahul Gandhi'] * len(rahul_votes) + ['Narendra Modi', 'Amit Shah'],
                    'Constituency': rahul_constituencies + [modi_constituency, amit_constituency],
                    'Votes': list(rahul_votes) + [modi_votes, amit_votes]
                })

                # Plot the comparison on the same plot frame
                plt.figure(figsize=(10, 6))
                sns.barplot(data=data_to_plot, x='Constituency', y='Votes', hue='Candidate', palette='muted')
                plt.title('Comparison of Votes for Rahul Gandhi, Narendra Modi, and Amit Shah')
                plt.xlabel('Constituency')
                plt.ylabel('Votes')
                plt.xticks(rotation=45)

                self.update_plot(plt.gcf())  # Update plot in the same frame

            except Exception as e:
                self.show_error_message(f"Error comparing candidates: {str(e)}")

    def plot_highest_lowest_margin(self):
        if self.data is not None:
            try:
                highest_margin_entry = self.data.loc[self.data['Margin'].idxmax()]
                lowest_margin_entry = self.data.loc[self.data['Margin'].idxmin()]

                # Combine the data
                data_to_plot = pd.DataFrame({
                    'Candidate': [highest_margin_entry['Leading Candidate'], lowest_margin_entry['Leading Candidate']],
                    'Party': [highest_margin_entry['Leading Party'], lowest_margin_entry['Leading Party']],
                    'Margin': [highest_margin_entry['Margin'], lowest_margin_entry['Margin']]
                })

                # Plot the comparison
                plt.figure(figsize=(10, 6))
                sns.barplot(data=data_to_plot, x='Candidate', y='Margin', hue='Party', palette='muted')
                plt.title('Candidates with Highest and Lowest Margin of Victory')
                plt.xlabel('Candidate')
                plt.ylabel('Margin of Victory')
                plt.xticks(rotation=45)

                self.update_plot(plt.gcf())  # Update plot in the same frame

            except Exception as e:
                self.show_error_message(f"Error plotting highest and lowest margin: {str(e)}")

    def plot_margin_histogram(self):
        if self.data is not None:
            try:
                plt.figure(figsize=(10, 6))
                sns.histplot(self.data['Margin'], bins=20, kde=True)
                plt.title('Histogram of Margin of Victory')
                plt.xlabel('Margin of Victory')
                plt.ylabel('Frequency')

                self.update_plot(plt.gcf())  # Update plot in the same frame

            except Exception as e:
                self.show_error_message(f"Error plotting histogram of margin: {str(e)}")

    def plot_boxplot_margin_by_party(self):
        if self.data is not None:
            try:
                plt.figure(figsize=(12, 6))
                sns.boxplot(data=self.data, x='Leading Party', y='Margin', palette='muted')
                plt.title('Boxplot of Margin of Victory by Party')
                plt.xlabel('Party')
                plt.ylabel('Margin of Victory')
                plt.xticks(rotation=90)

                self.update_plot(plt.gcf())  # Update plot in the same frame

            except Exception as e:
                self.show_error_message(f"Error plotting boxplot of margin by party: {str(e)}")

    def plot_top_trailing_parties_votes(self):
        if self.data is not None:
            try:
                trailing_party_votes = self.data.groupby('Trailing Party')['Margin'].sum().sort_values(ascending=False)

                plt.figure(figsize=(20, 6))
                plt.subplot(1, 2, 1)
                sns.barplot(x=trailing_party_votes.index[:10], y=trailing_party_votes.values[:10], palette='viridis')
                plt.title('Top 10 Trailing Parties by Votes')
                plt.xlabel('Party')
                plt.ylabel('Total Votes')
                plt.xticks(rotation=45)

                self.update_plot(plt.gcf())  # Update plot in the same frame

            except Exception as e:
                self.show_error_message(f"Error plotting top trailing parties by votes: {str(e)}")

    def plot_top_trailing_parties_seats(self):
        if self.data is not None:
            try:
                trailing_party_seats = self.data['Trailing Party'].value_counts().sort_values(ascending=False)

                plt.figure(figsize=(20, 6))
                plt.subplot(1, 2, 2)
                sns.barplot(x=trailing_party_seats.index[:10], y=trailing_party_seats.values[:10], palette='viridis')
                plt.title('Top 10 Trailing Parties by Seats')
                plt.xlabel('Party')
                plt.ylabel('Number of Seats')
                plt.xticks(rotation=45)

                plt.tight_layout()
                self.update_plot(plt.gcf())  # Update plot in the same frame

            except Exception as e:
                self.show_error_message(f"Error plotting top trailing parties by seats: {str(e)}")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = CTk()
    app = App(root)
    app.run()
