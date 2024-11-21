import tkinter as tk
import customtkinter as c
from tkinter import messagebox


# Correct credentials for login
CORRECT_USERNAME = "admin"
CORRECT_PASSWORD = "password"

# Function to check login credentials
def check_login():
    username = username_entry.get()
    password = password_entry.get()
    
    if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
        messagebox.showinfo("Login Successful", "Welcome!")
        root.destroy()  # Close login window if login is successful
    else:
        messagebox.showerror("Login Failed", "Incorrect username or password")

# GUI setup
root = tk.Tk()
root.title("Login")

# Set the window to full screen for 2560x1600 resolution
window_width, window_height = 2560, 1600
root.geometry(f"{window_width}x{window_height}+0+0")  # Full-screen window

# Create a frame in the center to hold the login elements
center_frame = tk.Frame(root)
center_frame.place(relx=0.5, rely=0.5, anchor="center")  # Center the frame

# Username label and entry field
username_label = tk.Label(center_frame, text="Username:", font=("Arial", 14))
username_label.grid(row=0, column=0, padx=5, pady=5)
username_entry = tk.Entry(center_frame, font=("Arial", 14))
username_entry.grid(row=0, column=1, padx=5, pady=5)

# Password label and entry field
password_label = tk.Label(center_frame, text="Password:", font=("Arial", 14))
password_label.grid(row=1, column=0, padx=5, pady=5)
password_entry = tk.Entry(center_frame, show="*", font=("Arial", 14))
password_entry.grid(row=1, column=1, padx=5, pady=5)

# Login button
login_button = tk.Button(center_frame, text="Login", command=check_login, font=("Arial", 14))
login_button.grid(row=2, column=0, columnspan=2, pady=20)  # Center the button under the entries

# Start the GUI loop
root.mainloop()


master = c.CTk()
master.title("Main")
master.geometry('2560x1600')

label1 = c.CTkLabel(master,
               text = "Calculator",
               font = ("Helvetica",24))
label1.place(x=670,y=30)

ctkbutton = c.CTkButton(master, 
                        text = "Back",
                        command=lambda: go_back(root))
ctkbutton.place(x=30,y=30)
def go_back(root):
    master.destroy() 
    root.deiconify()

#back_button = tk.Button(second_window, text="Back", command=lambda: go_back(second_window))
#back_button.pack(pady=20)




master.mainloop()