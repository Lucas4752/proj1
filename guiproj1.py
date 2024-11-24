import tkinter as tk
import customtkinter as c
from tkinter import messagebox
from tkinter import ttk

# Correct credentials for login
CORRECT_USERNAME = "admin"
CORRECT_PASSWORD = "password"

# Function to check login credentials
def check_login():
    username = username_entry.get()
    password = password_entry.get()
    
    if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
        messagebox.showinfo("Login Successful", "Welcome!")
        root.withdraw()  # Hide login window
        open_main_window()  # Open the main window
    else:
        messagebox.showerror("Login Failed", "Incorrect username or password")

# Function to go back to the login window
def go_back(master):
    master.destroy()  # Close the main window
    root.deiconify()  # Show the login window again

# Function to open the main window
def open_main_window():
    master = c.CTk()  # Create the main window
    master.title("Main")
    master.geometry('2560x1600')

    # Title label
    label1 = c.CTkLabel(master, 
                        text="3D Printing Material Cost Calculator", 
                        font=("Helvetica", 36))
    label1.place(relx=0.5, rely=0.05, anchor="center")

    # Back button
    ctkbutton = c.CTkButton(master, 
                            text="Back", 
                            command=lambda: go_back(master),
                            font=("Arial", 16))
    ctkbutton.place(x=30, y=30)

    # Dropdown for process selection
    process_var = tk.StringVar()
    process_var.trace('w', update_machine_dropdown)  # Update machines when process changes
    process_label = c.CTkLabel(master, text="Select Process:", font=("Arial", 18))
    process_label.place(relx=0.3, rely=0.2, anchor="center")
    process_dropdown = ttk.Combobox(master, textvariable=process_var, state="readonly", font=("Arial", 16), width=30)
    process_dropdown['values'] = list(material_cost.keys())
    process_dropdown.place(relx=0.6, rely=0.2, anchor="center")

    # Dropdown for machine selection
    machine_var = tk.StringVar()
    machine_label = c.CTkLabel(master, text="Select Machine:", font=("Arial", 18))
    machine_label.place(relx=0.3, rely=0.3, anchor="center")
    machine_dropdown = ttk.Combobox(master, textvariable=machine_var, state="readonly", font=("Arial", 16), width=30)
    machine_dropdown.place(relx=0.6, rely=0.3, anchor="center")

    # Input for material quantity
    input_label = c.CTkLabel(master, text="Enter Quantity (kg/L):", font=("Arial", 18))
    input_label.place(relx=0.3, rely=0.4, anchor="center")
    input_entry = c.CTkEntry(master, font=("Arial", 16), width=200)
    input_entry.place(relx=0.6, rely=0.4, anchor="center")

    # Function to update machine dropdown
    def update_machine_dropdown(*args):
        process = process_var.get()
        if process in material_cost:
            machines = list(material_cost[process].keys())
            machine_dropdown['values'] = machines
            machine_var.set('')  # Clear selection
        else:
            machine_dropdown['values'] = []
            machine_var.set('')

    # Function to calculate cost
    def calculate_cost():
        process = process_var.get()
        machine = machine_var.get()
        if process and machine and machine in material_cost[process]:
            machine_data = material_cost[process][machine]
            try:
                input_value = float(input_entry.get())
                # Determine cost based on price unit
                if 'price_per_kg' in machine_data:
                    cost = input_value * machine_data['price_per_kg']
                elif 'price_per_L' in machine_data:
                    cost = input_value * machine_data['price_per_L']
                elif 'price_per_unit' in machine_data:
                    cost = input_value * machine_data['price_per_unit']
                elif 'price_per_10kg' in machine_data:
                    cost = (input_value / 10) * machine_data['price_per_10kg']
                else:
                    result_label['text'] = "Error: Unsupported price format."
                    return
                # Update the result label
                result_label['text'] = f"Cost: ${cost:.2f}"
            except ValueError:
                result_label['text'] = "Error: Please enter a valid quantity."
        else:
            result_label['text'] = "Error: Invalid selection or input."

    # Button to calculate cost
    calculate_button = c.CTkButton(master, text="Calculate Cost", command=calculate_cost, font=("Arial", 16))
    calculate_button.place(relx=0.5, rely=0.5, anchor="center")

    # Label to display the result
    result_label = c.CTkLabel(master, text="Cost: $0.00", font=("Arial", 24), text_color="blue")
    result_label.place(relx=0.5, rely=0.6, anchor="center")

    master.mainloop()

# Material cost dictionary
material_cost = {
    'FDM': {
        'Ultimaker 3': {'material': 'abs', 'price_per_kg': 66.66, 'density': 1.1},
        'Fortus 360mc': {'material': 'ultem', 'price_per_unit': 343, 'density': 1.27}
    },
    'SLA': {
        'Form2_clear': {'material': 'clear resin', 'price_per_L': 149, 'density': 1.18},
        'Form2_dental': {'material': 'dental model resin', 'price_per_L': 149, 'density': 1.18},
        'ProX_950': {'material': 'accura xtreme', 'price_per_10kg': 2800, 'density': 1.18},
        'Form2_casting': {'material': 'casting resin', 'price_per_L': 299, 'density': 1.18}
    },
    'SLS': {
        'EOSINT_P800_PA2200': {'material': 'PA2200', 'price_per_kg': 67.5, 'density': 0.93},
        'EOSINT_P800_PA12': {'material': 'PA12', 'price_per_kg': 60, 'density': 1.01},
        'EOSINT_P800_ALU': {'material': 'alumide', 'price_per_kg': 50, 'density': 1.36},
    },
    'SLM': {
        'EOSm100_TI6Al4V': {'material': 'TI6Al4V', 'price_per_kg': 400, 'density': 4.43},
        'EOSm100_SSL316': {'material': 'SSL316', 'price_per_kg': 30, 'density': 8},
    },
    'DLP': {
        '3DSystems_figure4': {'material': 'Problack 10', 'price_per_kg': 250, 'density': 1.07},
    }
}

# GUI setup for the login window
root = tk.Tk()
root.title("Login")

# Set the window to full screen for 2560x1600 resolution
window_width, window_height = 2560, 1600
root.geometry(f"{window_width}x{window_height}+0+0")  # Full-screen window

# Create a frame in the center to hold the login elements
center_frame = tk.Frame(root)
center_frame.place(relx=0.5, rely=0.5, anchor="center")  # Center the frame

# Username label and entry field
username_label = tk.Label(center_frame, text="Username:", font=("Arial", 18))
username_label.grid(row=0, column=0, padx=5, pady=5)
username_entry = tk.Entry(center_frame, font=("Arial", 18))
username_entry.grid(row=0, column=1, padx=5, pady=5)

# Password label and entry field
password_label = tk.Label(center_frame, text="Password:", font=("Arial", 18))
password_label.grid(row=1, column=0, padx=5, pady=5)
password_entry = tk.Entry(center_frame, show="*", font=("Arial", 18))
password_entry.grid(row=1, column=1, padx=5, pady=5)

# Login button
login_button = tk.Button(center_frame, text="Login", command=check_login, font=("Arial", 18))
login_button.grid(row=2, column=0, columnspan=2, pady=20)  # Center the button under the entries

# Start the GUI loop
root.mainloop()


