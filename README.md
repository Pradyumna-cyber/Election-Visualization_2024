# India_Election-Visualization_2024



Lok Sabha Election 2024 Analysis Application Overview
The Lok Sabha Election 2024 Analysis application is an interactive tool designed to provide users with an in-depth analysis of the 2024 Indian Lok Sabha election results. The application utilizes the tkinter library for creating the graphical user interface (GUI) and customtkinter for enhanced UI components. The analysis functionalities are powered by pandas for data manipulation and matplotlib and seaborn for data visualization.

Home Page
Title and Information Display:
The home page welcomes the user with a title "🇮🇳 Lok Sabha Election 2024 🇮🇳" displayed prominently in bold, large font.
Below the title, there is a detailed description of the 2024 Indian Lok Sabha election, highlighting key events, outcomes, and voter participation.
Navigation:
The page includes an "Analysis" button that guides users to the detailed analysis section of the application.
Analysis Page
Main Layout:

The analysis page is structured into multiple sections for a clean and organized layout.
It features a main frame that divides the content into a side frame for controls and a plot frame for visualizations.
Header Section:

The header includes a small button with an image icon, enhancing the visual appeal and providing a distinct section for navigation.
A label stating "Analysis Page" informs users about the current page context.
File Upload:

An upload button is provided for users to upload the CSV file containing the election data.
The file dialog only accepts CSV files, ensuring users upload the correct file type.
Analysis Options:

The side frame houses several buttons, each corresponding to a different type of analysis. The buttons are color-coded for better visibility and user experience. The options include:
Party Votes Bar Plot: Visualizes the total votes (margin) for each leading party.
Votes Pie Chart: Displays the distribution of votes among different parties in a pie chart.
Compare Candidates: Compares votes for key candidates (Rahul Gandhi, Narendra Modi, Amit Shah) across their constituencies.
Highest & Lowest Margin: Plots the candidates with the highest and lowest margins of victory.
Histogram of Margin: Shows the distribution of the margin of victory across all candidates.
Boxplot of Margin by Party: Displays the distribution of victory margins by party.
Top 10 Trailing Parties by Votes: Bar plot of the top 10 trailing parties based on total votes.
Top 10 Trailing Parties by Seats: Bar plot of the top 10 trailing parties based on the number of seats won.
Plot Display:

The plot frame is designed to dynamically adjust and display different types of visualizations. It ensures that the plots are well-fitted within the frame for better readability.
Data Handling
File Upload and Data Cleaning:

Upon uploading the CSV file, the application reads the data into a pandas DataFrame.
The Margin column is converted to numeric to ensure accurate calculations and visualizations. Any non-numeric values in the Margin column are handled to prevent errors.
Error Handling:

The application is equipped with error handling mechanisms to display appropriate error messages if there are issues with data loading or visualization. This ensures a smooth user experience even when unexpected issues arise.
Visualization Functions
Party Votes Bar Plot:

This plot shows the total votes (measured by margin) for each leading party, allowing users to see which parties received the most votes.
Votes Pie Chart:

The pie chart provides a visual representation of the vote distribution among the different parties, offering a quick overview of each party's share.
Compare Candidates:

This function compares the votes received by key candidates, such as Rahul Gandhi, Narendra Modi, and Amit Shah, across their respective constituencies.
Highest & Lowest Margin:

This plot highlights the candidates who won with the highest and lowest margins of victory, showcasing the extremes in the election results.
Histogram of Margin:

The histogram shows the distribution of victory margins across all candidates, helping users understand the overall competitiveness of the election.
Boxplot of Margin by Party:

This boxplot visualizes the distribution of victory margins for each party, highlighting the spread and central tendency of margins within each party.
Top 10 Trailing Parties by Votes and Seats:

These bar plots show the top 10 trailing parties based on total votes and the number of seats won, respectively, providing insights into the performance of less dominant parties.
User Interface Enhancements
The application aims to offer a user-friendly and visually appealing interface. Key enhancements include:

Color-Coded Buttons:

Analysis buttons are color-coded for better differentiation and a more attractive interface.
Proper Alignment and Positioning:

Buttons and other UI elements are aligned properly to ensure a clean and organized layout.
Dynamic Plot Adjustment:

The plots are designed to adjust correctly within the frame, ensuring they are always well-fitted and readable.
Error Handling
The application incorporates robust error handling to manage unexpected issues:

Data Loading Errors:

If there is an issue with loading the data, an error message is displayed to inform the user of the problem.
Plotting Errors:

Any issues encountered during plotting are caught, and appropriate error messages are shown to the user, ensuring the application does not crash.
Conclusion
The Lok Sabha Election 2024 Analysis application provides a comprehensive tool for analyzing election results through a user-friendly interface. It combines powerful data visualization capabilities with intuitive controls, making it accessible for users to explore and understand the election data in depth. The application's robust error handling and dynamic UI adjustments further enhance the user experience, ensuring a smooth and engaging interaction.

App Screens:

1. <img width="800" alt="image" src="https://github.com/Pradyumna-cyber/Election-Visualization_2024/assets/73057121/d1a63f49-d04d-4b5f-a199-fd52ebe5458e">



2. <img width="798" alt="image" src="https://github.com/Pradyumna-cyber/Election-Visualization_2024/assets/73057121/b1a8e14c-bcee-44cd-bf2b-b7d1d52485a5">

3. Plots
   <img width="1440" alt="image" src="https://github.com/Pradyumna-cyber/Election-Visualization_2024/assets/73057121/3159e4b4-b88a-4b05-ad8d-1a522a959ca2">

   <img width="1439" alt="image" src="https://github.com/Pradyumna-cyber/Election-Visualization_2024/assets/73057121/dff289ec-dc4a-4adf-946f-78af3fc8f45b">

   <img width="1439" alt="image" src="https://github.com/Pradyumna-cyber/Election-Visualization_2024/assets/73057121/6be39e74-aaa9-4027-98a6-6f8d0a56ada8">

   <img width="1440" alt="image" src="https://github.com/Pradyumna-cyber/Election-Visualization_2024/assets/73057121/d7026b85-bfe5-4f0b-a98b-c3e7ad2639c9">

   <img width="1440" alt="image" src="https://github.com/Pradyumna-cyber/Election-Visualization_2024/assets/73057121/86d3569c-8f2a-4e7b-9877-1b4ffabcccd9">

   <img width="1436" alt="image" src="https://github.com/Pradyumna-cyber/Election-Visualization_2024/assets/73057121/2d6e1342-ec5f-4237-9c78-e694c6bd1785">

   <img width="1403" alt="image" src="https://github.com/Pradyumna-cyber/Election-Visualization_2024/assets/73057121/a5002d95-6092-4c24-a655-46433d98d991">

   <img width="1436" alt="image" src="https://github.com/Pradyumna-cyber/Election-Visualization_2024/assets/73057121/bbfe043d-17df-42b7-9307-5a0e6e6125be">







