import tkinter as tk
from tkinter import ttk

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
    else:
        result_label['text'] = "Error: Invalid selection or input."

# Create the main window
root = tk.Tk()
root.title("Material Cost Calculator")
root.geometry("500x400")

# Dropdown for process selection
process_var = tk.StringVar()
process_var.trace('w', update_machine_dropdown)  # Update machines when process changes
process_label = tk.Label(root, text="Select Process:")
process_label.pack(pady=5)
process_dropdown = ttk.Combobox(root, textvariable=process_var, state="readonly")
process_dropdown['values'] = list(material_cost.keys())
process_dropdown.pack(pady=5)

# Dropdown for machine selection
machine_var = tk.StringVar()
machine_label = tk.Label(root, text="Select Machine:")
machine_label.pack(pady=5)
machine_dropdown = ttk.Combobox(root, textvariable=machine_var, state="readonly")
machine_dropdown.pack(pady=5)

# Input for material quantity
input_label = tk.Label(root, text="Enter Quantity (kg/L):")
input_label.pack(pady=5)
input_entry = tk.Entry(root)
input_entry.pack(pady=5)

# Button to calculate cost
calculate_button = tk.Button(root, text="Calculate Cost", command=calculate_cost)
calculate_button.pack(pady=10)

# Label to display the result
result_label = tk.Label(root, text="Cost: $0.00", font=("Arial", 14))
result_label.pack(pady=20)

# Run the application
root.mainloop()
