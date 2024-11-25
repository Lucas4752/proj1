import tkinter as tk
import customtkinter as c
from tkinter import messagebox
from tkinter import ttk

#Det rigtige login
CORRECT_USERNAME = "admin"
CORRECT_PASSWORD = "password"

#Material_cost dictionary
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

#Funktion til at checke login
def check_login():
    username = username_entry.get()
    password = password_entry.get()
    
    if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
        messagebox.showinfo("Login Successful", "Welcome!")
        root.withdraw()  #Lukker login skærmen
        open_main_window()  #Åbner main_window
    else:
        messagebox.showerror("Login Failed", "Incorrect username or password")

#Funktion for tilbage knappen
def go_back(master):
    master.destroy()  #Lukker main_window
    root.deiconify()  #Genåbner loginsiden

#Funktion for at åbne hovedvinduet
def open_main_window():
    master = c.CTk()  #Laver hovedvinduet kaldt "master"
    master.title("NEXTTECH Material Calculator")
    master.geometry('2560x1600')  #Skærmstørrelse sat til mac skærmstørrelse

    #Title_label som er det navn vi har i toppen af beregneren
    title_label = c.CTkLabel(master, text="NEXTTECH Material Cost Calculator", font=("Helvetica", 36))
    title_label.pack(pady=40)

    #Dropdown menu for process og updater machine dropdown
    process_var = tk.StringVar()
    machine_var = tk.StringVar()

    def update_machine_dropdown(*args):
        process = process_var.get()
        if process in material_cost:
            machines = list(material_cost[process].keys())
            machine_dropdown['values'] = machines
            machine_var.set('')
        else:
            machine_dropdown['values'] = []
            machine_var.set('')
    #Dropdown menu for process
    process_label = c.CTkLabel(master, text="Select Process:", font=("Arial", 24))
    process_label.pack(pady=10)
    process_dropdown = ttk.Combobox(master, textvariable=process_var, state="readonly", font=("Arial", 18))
    process_dropdown['values'] = list(material_cost.keys())
    process_dropdown.pack(pady=10, ipadx=10, ipady=10)
    process_var.trace('w', update_machine_dropdown) #Updater machines når process ændres

    #Dropdown menu for machine
    machine_label = c.CTkLabel(master, text="Select Machine:", font=("Arial", 24))
    machine_label.pack(pady=10)
    machine_dropdown = ttk.Combobox(master, textvariable=machine_var, state="readonly", font=("Arial", 18))
    machine_dropdown.pack(pady=10, ipadx=10, ipady=10)

    #Input for material kvantitet
    input_label = c.CTkLabel(master, text="Enter Quantity (kg/L):", font=("Arial", 24))
    input_label.pack(pady=10)
    input_entry = c.CTkEntry(master, font=("Arial", 20), width=400)
    input_entry.pack(pady=10)

    #Funktion til pris udregning
    def calculate_cost():
        process = process_var.get()
        machine = machine_var.get()
        try:
            input_value = float(input_entry.get())
        except ValueError:
            result_label.configure(text="Error: Please enter a valid numeric quantity.")
            return

        #Determiner pris baserede på price unit
        if process and machine and machine in material_cost[process]:
            machine_data = material_cost[process][machine]
            if 'price_per_kg' in machine_data:
                cost = input_value * machine_data['price_per_kg']
            elif 'price_per_L' in machine_data:
                cost = input_value * machine_data['price_per_L']
            elif 'price_per_unit' in machine_data:
                cost = input_value * machine_data['price_per_unit']
            elif 'price_per_10kg' in machine_data:
                cost = (input_value / 10) * machine_data['price_per_10kg']
            else:
                result_label.configure(text="Error: Unsupported price format.")
                return

            #Updater resultat label
            result_label.configure(text=f"Cost: ${cost:.2f}")
        else:
            result_label.configure(text="Error: Please select valid options.")

    #Knap til at beregne
    calculate_button = c.CTkButton(master, text="Calculate Cost", command=calculate_cost, font=("Arial", 20), width=200)
    calculate_button.pack(pady=20)

    #Label til at vise resultat
    result_label = c.CTkLabel(master, text="Cost: $0.00", font=("Arial", 28), text_color="green")
    result_label.pack(pady=40)

    #Tilbage knap
    back_button = c.CTkButton(master, text="Back", command=lambda: go_back(master), font=("Arial", 20), width=200)
    back_button.pack(pady=20)

    master.mainloop()

#GUI setup for login skærmen
root = tk.Tk()
root.title("Login")

#Login skærmens skærmstørrelse
root.geometry("2560x1600")  

#Centrere login
center_frame = tk.Frame(root)
center_frame.place(relx=0.5, rely=0.5, anchor="center")

#Brugernavn label og skriftfelt
username_label = tk.Label(center_frame, text="Username:", font=("Arial", 20))
username_label.grid(row=0, column=0, padx=20, pady=20)
username_entry = tk.Entry(center_frame, font=("Arial", 20), width=20)
username_entry.grid(row=0, column=1, padx=20, pady=20)

#Kode label og skriftfelt
password_label = tk.Label(center_frame, text="Password:", font=("Arial", 20))
password_label.grid(row=1, column=0, padx=20, pady=20)
password_entry = tk.Entry(center_frame, show="*", font=("Arial", 20), width=20)
password_entry.grid(row=1, column=1, padx=20, pady=20)

#Login knap
login_button = tk.Button(center_frame, text="Login", command=check_login, font=("Arial", 20), width=10)
login_button.grid(row=2, column=0, columnspan=2, pady=30)

#Starter GUI loop
root.mainloop()


