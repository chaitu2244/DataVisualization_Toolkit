'''This is an Data Visualization Toolkit.This Python project provides a user-friendly interface for visualizing data using various techniques such
as Pie Chart, Histogram, Heatmap, and Scatterplot.
It utilizes the tkinter library for the graphical user interface (GUI) and pandas for data manipulation.
With this toolkit, users can easily upload their data files, select attributes of interest, and visualize their data in different ways.'''

#Importing Packages
import tkinter as tk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_window_created = False  # Define the variable globally and initialize it

#Function to select the file.
def open_file_dialog():
    file_path = filedialog.askopenfilename()
    if file_path:
        file_label.config(text="Selected File: " + file_path)
        global data_frame
        data_frame = pd.read_csv(file_path)

# Function to switch to the file selection window
def switch_to_file_selection():
    global file_window_created
    # Destroy the main window
    root.destroy()
    # Show the file selection window
    if not file_window_created:
        create_file_window()

# Function to create the file selection window
def create_file_window():
    global file_window
    file_window = tk.Tk()
    file_window.title("Select File")

    # Set window size
    window_width = 1000
    window_height = 700
    file_window.geometry(f"{window_width}x{window_height}")

    # Set background color to white
    file_window.configure(bg="white")

    # Create file selection frame
    file_selection_frame = tk.Frame(file_window, bg="white")

    # Create label for selecting file
    select_label = tk.Label(file_selection_frame, text="Select the file", font=("Arial", 40, "bold"), bg="white")
    select_label.pack(side=tk.TOP, anchor="nw", padx=10, pady=10)

    # Create browse button
    browse_button = tk.Button(file_selection_frame, text="Browse", font=("Arial", 12), command=open_file_dialog)
    browse_button.pack(side=tk.TOP, anchor="nw", padx=10, pady=10)

    # Create label to display selected file path
    global file_label
    file_label = tk.Label(file_selection_frame, text="", font=("Arial", 14), bg="white")
    file_label.pack(side=tk.TOP, anchor="nw", padx=10, pady=10)

    # Create frame for attribute input
    attribute_frame = tk.Frame(file_selection_frame, bg="white")

    # Create label and entry widgets for attribute 1
    label1 = tk.Label(attribute_frame, text="Attribute 1:", font=("Arial", 14), bg="white")
    label1.grid(row=0, column=0, padx=10, pady=10)
    entry1 = tk.Entry(attribute_frame, font=("Arial", 14))
    entry1.grid(row=0, column=1, padx=10, pady=10)

    # Create label and entry widgets for attribute 2
    label2 = tk.Label(attribute_frame, text="Attribute 2:", font=("Arial", 14), bg="white")
    label2.grid(row=1, column=0, padx=10, pady=10)
    entry2 = tk.Entry(attribute_frame, font=("Arial", 14))
    entry2.grid(row=1, column=1, padx=10, pady=10)

    # Create button to visualize data
    visualize_button = tk.Button(attribute_frame, text="Visualize Data", font=("Arial", 14), command=lambda: visualize_data(entry1.get(), entry2.get(), pie_var.get(), hist_var.get(), heatmap_var.get(), scatterplot_var.get()))
    visualize_button.grid(row=2, columnspan=2, padx=10, pady=10)

    # Create checkboxes for visualization techniques
    pie_var = tk.BooleanVar()
    pie_check = tk.Checkbutton(attribute_frame, text="Pie Chart", variable=pie_var, font=("Arial", 14), bg="white")
    pie_check.grid(row=3, columnspan=2, padx=10, pady=5, sticky="w")

    hist_var = tk.BooleanVar()
    hist_check = tk.Checkbutton(attribute_frame, text="Histogram", variable=hist_var, font=("Arial", 14), bg="white")
    hist_check.grid(row=4, columnspan=2, padx=10, pady=5, sticky="w")

    heatmap_var = tk.BooleanVar()
    heatmap_check = tk.Checkbutton(attribute_frame, text="Heatmap", variable=heatmap_var, font=("Arial", 14), bg="white")
    heatmap_check.grid(row=5, columnspan=2, padx=10, pady=5, sticky="w")

    scatterplot_var = tk.BooleanVar()
    scatterplot_check = tk.Checkbutton(attribute_frame, text="Scatterplot", variable=scatterplot_var, font=("Arial", 14), bg="white")
    scatterplot_check.grid(row=6, columnspan=2, padx=10, pady=5, sticky="w")

    # Pack attribute frame
    attribute_frame.pack(expand=True, fill='both')

    # Pack file selection frame
    file_selection_frame.pack(expand=True, fill='both')

    global file_window_created
    file_window_created = True

def visualize_data(attribute1, attribute2, pie_selected, hist_selected, heatmap_selected, scatterplot_selected):
    if attribute1 and attribute2:
        if not any([pie_selected, hist_selected, heatmap_selected, scatterplot_selected]):
            tk.messagebox.showerror("Error", "Please select at least one visualization technique!")
            return

        if not all([attribute1 in data_frame.columns, attribute2 in data_frame.columns]):
            tk.messagebox.showerror("Error", "Invalid attribute names!")
            return

        if pie_selected:
            plt.figure(figsize=(8, 8))
            plt.pie(data_frame[attribute1].value_counts(), labels=data_frame[attribute1].unique(), autopct='%1.1f%%')
            plt.title(f"Pie Chart: {attribute1}")
            plt.show()

        if hist_selected:
            plt.hist(data_frame[attribute1], bins='auto')
            plt.xlabel(attribute1)
            plt.ylabel("Frequency")
            plt.title(f"Histogram: {attribute1}")
            plt.show()

        if heatmap_selected:
            plt.figure(figsize=(10, 8))
            sns.heatmap(data_frame.pivot_table(index=attribute1, columns=attribute2, aggfunc=len), cmap="YlGnBu")
            plt.title(f"Heatmap: {attribute1} vs {attribute2}")
            plt.show()

        if scatterplot_selected:
            plt.scatter(data_frame[attribute1], data_frame[attribute2])
            plt.xlabel(attribute1)
            plt.ylabel(attribute2)
            plt.title(f"Scatterplot: {attribute1} vs {attribute2}")
            plt.show()

    else:
        tk.messagebox.showerror("Error", "Please enter attribute names!")


# Create main window
root = tk.Tk()
root.title("Data Visualization using Python")

# Set window size
window_width = 1000
window_height = 700
root.geometry(f"{window_width}x{window_height}")

# Set background color to white
root.configure(bg="white")

# Calculate optimal sizes for text and button
title_text_size = int(min(window_width, window_height) * 0.05)  # Adjust as needed
select_text_size = 48
button_font_size = 12

# Create label for title and place it in the center
title_label = tk.Label(root, text="Data Visualization using Python", font=("Arial", title_text_size, "bold"), bg="white")
title_label.place(relx=0.5, rely=0.4, anchor="center")

# Create start button with custom color, text size, and color
button_width = 7
button_height = 1
start_button = tk.Button(root, text="Start", bg="#0085FF", fg="white", font=("Arial", button_font_size, "bold"), width=button_width, height=button_height, command=switch_to_file_selection)
start_button.place(relx=0.5, rely=0.6, anchor="center")

root.mainloop()
