import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import Messagebox

def settings():
    # Function to save values to a file
    def save_to_file():
        # Check each entry for empty values and gather data
        values = {
            "Addition Limit": add_limit_entry.get(),
            "Subtraction Limit": sub_limit_entry.get(),
            "Multiplication Limit": mult_limit_entry.get(),
            "Multiplication Table Limit": mult_table_limit_entry.get(),
            "Division Limit": div_limit_entry.get(),
            "time_duration": time_duration.get()
        }

        # Validate that no fields are empty
        for key, value in values.items():
            if not value.strip().isdigit():  # Check if the value is a digit
                Messagebox.show_error(f"{key} must be a valid integer!", "Error")
                return  # Stop if any field is empty or not an integer

        # Write values to a text file
        with open("limits.txt", "w") as file:
            for key, value in values.items():
                file.write(f"{key}: {value}\n")

        setWin.quit()

    def stFoc(event):
        exit_button.focus_set()

    def btnByOnclick(event):
        save_to_file()
        save_to_file()

    # Function to load values from a file
    def load_values():
        try:
            with open("limits.txt", "r") as file:
                for line in file:
                    key, value = line.strip().split(": ")
                    if key == "Addition Limit":
                        add_limit_entry.insert(0, value)
                    elif key == "Subtraction Limit":
                        sub_limit_entry.insert(0, value)
                    elif key == "Multiplication Limit":
                        mult_limit_entry.insert(0, value)
                    elif key == "Multiplication Table Limit":
                        mult_table_limit_entry.insert(0, value)
                    elif key == "Division Limit":
                        div_limit_entry.insert(0, value)
                    elif key == "time_duration":
                        time_duration.insert(0, value)
        except FileNotFoundError:
            Messagebox.show_error("Limitation Error", "Error")
            setWin.quit()
            

    # Create the main window
    setWin = ttk.Window(themename="superhero")
    setWin.title("Speed Maths Limit Setting")
    setWin.iconbitmap('icon2.ico')
    setWin.iconbitmap(default='icon2.ico')

    # Center window
    screen_width = setWin.winfo_screenwidth()
    screen_height = setWin.winfo_screenheight()
    x = (screen_width // 2) - (500 // 2)
    y = (screen_height // 2) - (600 // 2)
    setWin.geometry(f'500x600+{x}+{y}')
    setWin.overrideredirect(True)

    # Style settings
    section_font = ("Helvetica", 14, "bold")
    label_font = ("Helvetica", 10)

    # Frame for Addition Settings
    add_frame = ttk.Labelframe(setWin, text="Addition Settings", padding=10)
    add_frame.grid(row=0, column=0, columnspan=2, sticky="ew", padx=20, pady=10)

    ttk.Label(add_frame, text="Set Addition Limit:", font=label_font).grid(row=0, column=0, sticky="w", padx=5)
    add_limit_entry = ttk.Entry(add_frame, width=25)
    add_limit_entry.grid(row=0, column=1, padx=5)

    # Frame for Subtraction Settings
    sub_frame = ttk.Labelframe(setWin, text="Subtraction Settings", padding=10)
    sub_frame.grid(row=1, column=0, columnspan=2, sticky="ew", padx=20, pady=10)

    ttk.Label(sub_frame, text="Set Subtraction Limit:", font=label_font).grid(row=0, column=0, sticky="w", padx=5)
    sub_limit_entry = ttk.Entry(sub_frame, width=25)
    sub_limit_entry.grid(row=0, column=1, padx=5)

    # Frame for Multiplication Settings
    mult_frame = ttk.Labelframe(setWin, text="Multiplication Settings", padding=10)
    mult_frame.grid(row=2, column=0, columnspan=2, sticky="ew", padx=20, pady=10)

    ttk.Label(mult_frame, text="Set Multiplication Limit:", font=label_font).grid(row=0, column=0, sticky="w", padx=5)
    mult_limit_entry = ttk.Entry(mult_frame, width=25)
    mult_limit_entry.grid(row=0, column=1, padx=5, pady=2)

    ttk.Label(mult_frame, text="Set Multiplication Table Limit:", font=label_font).grid(row=1, column=0, sticky="w", padx=5)
    mult_table_limit_entry = ttk.Entry(mult_frame, width=25)
    mult_table_limit_entry.grid(row=1, column=1, padx=5, pady=2)

    # Frame for Division Settings
    div_frame = ttk.Labelframe(setWin, text="Division Settings", padding=10)
    div_frame.grid(row=3, column=0, columnspan=2, sticky="ew", padx=20, pady=10)

    ttk.Label(div_frame, text="Set Division Limit:", font=label_font).grid(row=0, column=0, sticky="w", padx=5)
    div_limit_entry = ttk.Entry(div_frame, width=25)
    div_limit_entry.grid(row=0, column=1, padx=5)

    # Frame for time Set
    time_frame = ttk.Labelframe(setWin, text="Duration Time (minits)", padding=10)
    time_frame.grid(row=4, column=0, columnspan=2, sticky="ew", padx=20, pady=10)
    
    ttk.Label(time_frame, text="Set Division Limit:", font=label_font).grid(row=0, column=0, sticky="w", padx=5)
    time_duration = ttk.Entry(time_frame, width=25)
    time_duration.grid(row=0, column=1, padx=5)


    # Exit button to save and quit
    exit_button = ttk.Button(setWin, text="Save & Exit", command=save_to_file, bootstyle="success")
    exit_button.grid(row=5, column=0, columnspan=2, pady=20)

    
    add_limit_entry.bind("<Return>", stFoc)
    sub_limit_entry.bind("<Return>", stFoc)
    mult_limit_entry.bind("<Return>", stFoc)
    mult_table_limit_entry.bind("<Return>", stFoc)
    div_limit_entry.bind("<Return>", stFoc)
    time_duration.bind("<Return>", stFoc)

    exit_button.bind("<Return>", btnByOnclick)

    # Load values when the application starts
    load_values()

    # Run the application
    setWin.mainloop()

#settings()