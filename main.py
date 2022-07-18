import pandas as pd
import matplotlib.pyplot as plt

# Reading csv file using pandas
data = pd.read_csv("rainfall_data.csv")

# Creating a list of years
years = []  # This will be used as a common x-axis

# Getting years from one data piece and using it as common data:
for year in list(data.iloc[117:234, 1]):
    years.append(int(year))  # Appending each year to the list

# Getting data for each region:

# Getting the data for Madhya Maharashtra:
madhya_maha_average_rainfall = data.iloc[0:117, 2].values
madhya_maha_jun_to_sept = data.iloc[0:117, 3].values

# Getting the data for Marathwada:
marathwada_average_rainfall = data.iloc[117:234, 2].values
marathwada_jun_to_sept = data.iloc[117:234, 3].values

# Getting the data for Vidharbha:
vidarbha_average_rainfall = data.iloc[234:351, 2].values
vidarbha_jun_to_sept = data.iloc[234:351, 3].values


# Defining class to browse data from csv sheet:
class Browse:
    def __init__(self):
        self.user_year = int(input("\nPlease enter the year you want to access data of (Enter from 1901 to 2017): "))

    def browse_madhya_maha(self):
        if self.user_year in years:
            print(
                f"Average Annual Rainfall: {madhya_maha_average_rainfall[self.user_year - 1901]} mm\nAverage Rainfall "
                f"from "
                f" Jun - "
                f"Sept: {madhya_maha_jun_to_sept[self.user_year - 1901]} mm")
        else:
            print("The year is not in the database. Exiting function...")

    def browse_marathwada(self):
        if self.user_year in years:
            print(f"Average Annual Rainfall: {marathwada_average_rainfall[self.user_year - 1901]} mm\nAverage Rainfall "
                  f"from "
                  f"Jun - "
                  f"Sept: {marathwada_jun_to_sept[self.user_year - 1901]} mm")
        else:
            print("The year is not in the database. Exiting function...")

    def browse_vidarbha(self):
        if self.user_year in years:
            print(
                f"Average Annual Rainfall: {vidarbha_average_rainfall[self.user_year - 1901]} mm\nAverage Rainfall from"
                f" Jun - "
                f"Sept: {vidarbha_jun_to_sept[self.user_year - 1901]} mm")
        else:
            print("The year is not in the database. Exiting function...")


# Plotter function will plot the graph according to user requirement
def plotter():
    keep_plotting = True
    while keep_plotting:
        user_region = input("\nPlease "
                            "enter the letter of the region you want to plot:\n'mm' for Madhya "
                            "Maharashtra\n'm' for Marathwada\n'v' for Vidarbha\n'e' for exiting to main menu\nYour "
                            "choice: ")
        if user_region == "mm":
            plot_graph(madhya_maha_average_rainfall, madhya_maha_jun_to_sept, "Madhya Maharashtra Rainfall")
        elif user_region == "m":
            plot_graph(marathwada_average_rainfall, marathwada_jun_to_sept, "Marathwada Rainfall")
        elif user_region == "v":
            plot_graph(vidarbha_average_rainfall, vidarbha_jun_to_sept, "Vidarbha Rainfall")
        elif user_region == "e":
            print("Going back to main menu\n\nWelcome back to main menu")
            keep_plotting = False
        else:
            print("Invalid Input... Rerunning...")


# Defining a function to create a graph and display:
def plot_graph(avg_rainfall_data, jun_sept_data, title):
    fig, ax = plt.subplots()  # Create a figure containing a single axes.
    # Creating two plots to compare the data
    ax.plot(years, avg_rainfall_data, label="Average Rainfall")
    ax.plot(years, jun_sept_data, label="Jun-Sept Rainfall")
    ax.legend()  # To show legend on graph
    fig.suptitle(str(title))  # Title of the graph
    plt.show()  # Interface


# Menu Driven Code Line Start
program_running = True  # Using boolean assigned variable

# Printing welcome string
print("\nWelcome to data analysis program.\nWe have collected the data of rainfall \nfrom 1901 to 2017 in following "
      "three regions of "
      "Maharashtra, India: Madhya Maharashtra (Western Maharashtra), Marathwada and Vidarbha.")

# Loop to make program repetitive for user convenience
while program_running:
    # Taking user choice
    user_choice = input("\nPlease enter the number corresponding to given choices:\n1 - Browse data from region\n2 "
                        "- Get Graphs\n3 - Exit\nYour choice: ")

    # Testing choices with conditions
    if user_choice == "1":
        # Using boolean assigned variable
        browse_running = True

        # Loop to let user browse through data multiple times
        while browse_running:

            # Taking input as the region of interest from user
            user_browse_region = input("\nEnter the number corresponding region which you want to browse:\n1 - Madhya "
                                       "Maharashtra (Western Maharashtra)\n2 - Vidarbha\n3 - Marathwada\n4 - Exit "
                                       "browsing\nYour choice: ")

            # Checking user choice region with conditions
            if user_browse_region == "1":
                browse_obj = Browse()  # Object declaration from class
                browse_obj.browse_madhya_maha()  # Calling function from class
            elif user_browse_region == "2":
                browse_obj = Browse()  # Object declaration from class
                browse_obj.browse_marathwada()  # Calling function from class
            elif user_browse_region == "3":
                browse_obj = Browse()  # Object declaration from class
                browse_obj.browse_vidarbha()  # Calling function from class
            elif user_browse_region == "4":
                print("Redirecting back to main menu...\n")  # Getting back to parent loop
                browse_running = False  # Changing boolean value to break loop
            else:
                print("Invlaid input. Browse rerunning..")  # In case user mistype or gives invalid input, loop will
                # rerun after this message
    elif user_choice == "2":
        # Using predefined function instead of making mess here
        plotter()
    elif user_choice == "3":
        # Exiting from loop and ending the program
        print("Exiting...")
        program_running = False  # Changing boolean value to break loop
    else:
        print("Invalid input. Rerunning...")  # In case user mistype or gives invalid input, loop will
        # rerun after this message
