import tkinter as tk
from PIL import Image, ImageTk, ImageFilter, ImageEnhance
from tkinter import messagebox
import re
import sqlite3
import os
from datetime import datetime
import sys

# Connect to the SQLite database
conn = sqlite3.connect("employee_data.db")
cursor = conn.cursor()

# Create the login_record table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS login_record (
        id INTEGER PRIMARY KEY,
        employee_id TEXT,
        admin_name TEXT,
        login_datetime DATETIME
    )
''')

# Function to check if a string is a valid password
def is_valid_password(password):
    return re.match(r'^[0-9]{6}$', password)

# Function to check if the entered username and password are valid and return employee_id
def validate_login(entered_username, entered_password):
    conn = sqlite3.connect("employee_data.db")
    cursor = conn.cursor()

    first_name = entered_username.split()[0]
    cursor.execute("SELECT employee_id FROM admin_record WHERE first_name = ? AND password = ?", (first_name, entered_password))
    result = cursor.fetchone()

    conn.close()
    return result[0] if result else None

# Function to insert login records into the login_record table
def insert_login_record(user_id, username, login_datetime):
    # Connect to the SQLite database
    conn = sqlite3.connect("employee_data.db")
    cursor = conn.cursor()

    # Insert the login record into the login_record table
    cursor.execute("INSERT INTO login_record (employee_id, admin_name, login_datetime) VALUES (?, ?, ?)",
                   (user_id, username, login_datetime))
    conn.commit()
    conn.close()

# Function to handle the login button click
def login():
    entered_username = entry_username.get()
    entered_password = entry_password.get()

    if not re.match("^[a-zA-Z ]+$", entered_username):
        messagebox.showerror("Login Failed", "Invalid username. Use only letters (a-z, A-Z) and space.")
    else:
        user_id = validate_login(entered_username, entered_password)
        if user_id is not None:
            try:
                current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                # Now that you have user_id, you can insert it into the login_record table
                insert_login_record(user_id, entered_username, current_datetime)

                # Display a successful login message
                messagebox.showinfo("Login Successful", "You have successfully logged in.")
                
                # Open the administration window
                open_administration_window()
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            if not re.match(r'^[0-9]{6}$', entered_password):
                messagebox.showerror("Login Failed", "Invalid Password. Password must be 6 digits (0-9).")
            else:
                messagebox.showerror("Login Failed", "Invalid Username or Password.")

# Function to handle the "Forget Password" button click
def forget_password(event):
    username = entry_username.get()
    
    if not re.match("^[a-zA-Z ]+$", username):  # Allow space in the username
        messagebox.showerror("Forget Password Failed", "Invalid username. Use only letters (a-z, A-Z) and space.")
    else:
        # Create a new Toplevel window for password reset
        reset_password_window = tk.Toplevel(root)
        reset_password_window.title("Reset Password")
        reset_password_window.configure()  # Set background color
        
        # Set the initial size of the window
        reset_password_window.geometry("500x300")  # You can adjust the size as needed
        # Disable window resizing
        reset_password_window.resizable(0, 0)

        # Entry field for new password
        new_password_label = tk.Label(reset_password_window, text=f"Enter a new password:", font=("godey", 18), fg="#5a46a7")
        new_password_label.pack(pady=20)
        
        new_password_entry = tk.Entry(reset_password_window, show='*', font=("godey", 15))
        new_password_entry.pack(pady=20)
        
        # Button to update password
        update_password_button = tk.Button(reset_password_window, text="Update Password", command=lambda: update_password(username, new_password_entry.get()), padx=10, pady=10, font=("godey", 15, "bold"), bg="#5a46a7", fg="white")
        update_password_button.pack(pady=20)
        
        def update_password(username, new_password):
            if new_password:
                # Update the password in the database
                conn = sqlite3.connect("employee_data.db")
                cursor = conn.cursor()
                first_name = username.split()[0]
                cursor.execute("UPDATE admin_record SET password = ? WHERE first_name = ?", (new_password, first_name))
                conn.commit()
                conn.close()
                messagebox.showinfo("Password Updated", "Password updated successfully!")
                reset_password_window.destroy()
            else:
                messagebox.showerror("Update Password Failed", "New password cannot be empty.")

                root.destroy()

# Function to open the administration.py script in a new window
def open_administration_window():
    root.withdraw()  # Hide the login window
    # Define the path to the administration.py script
    administration_script = "administration.py"

    # Check if the administration.py script exists
    if os.path.exists(administration_script):
        # Open the administration.py script in the new window
        os.system(sys.executable + " " + administration_script)
    else:
        messagebox.showerror("Error", "administration.py not found!")

# Create the main Tkinter window
root = tk.Tk()

# Create labels and entry fields for username and password
label_username = tk.Label(root, text="User (First Name):",padx=20, pady=20, font=("impact", 20), fg="#5a46a7" )
label_username.place( x=20, y=280 )
entry_username = tk.Entry(root, font=("goder", 20, "bold"), fg="black")
entry_username.place(x=250, y=300)

label_password = tk.Label(root, text="Password:",padx=20, pady=20, font=("impact", 20), fg="#5a46a7")
label_password.place(x=20, y=360)

# Add the "Forget Password" text above the password entry field
forget_password_text = tk.Label(root, text="Forget Password?", font=("godey", 13 ), fg="black", cursor="hand2")
forget_password_text.place(x=420,y=430)
forget_password_text.bind("<Button-1>", forget_password)  # Bind the click event to the forget_password function

entry_password = tk.Entry(root, show='*', font=("godey", 20), fg="black")
entry_password.place(x=250, y=385)

# Create a login button
btn_login = tk.Button(root, text="Login", command=login, width=10, font=("godey", 20, "bold"), bg="#5a46a7", fg="white")
btn_login.place(x=210, y=520)

root.title("Admin Login page")

# Make the window fullscreen
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

# Load the first image and apply a blur effect
image1 = Image.open("g.png")
image1 = image1.filter(ImageFilter.GaussianBlur(5))  # Adjust the blur factor as needed
photo1 = ImageTk.PhotoImage(image1)

image_label1 = tk.Label(root, image=photo1)
image_label1.place(x=850, y=110)

# Load the second image and apply a 3D effect
image2 = Image.open("h.png")

# Apply a 3D effect
image2 = image2.filter(ImageFilter.EDGE_ENHANCE_MORE)  # Apply an edge enhancement filter

# Enhance color (return to original state)
enhancer = ImageEnhance.Color(image2)
image2 = enhancer.enhance(1.0)

photo2 = ImageTk.PhotoImage(image2)

image_label2 = tk.Label(root, image=photo2)
image_label2.place(x=940, y=220)

 # Load the second image
image3 = Image.open("a.png")
photo3 = ImageTk.PhotoImage(image3)
# Create and add a label to display the second image with a transparent background
image_label2 = tk.Label(root, image=photo3)
image_label2.place(x=1320, y=10)
# Function to create a new main window
def create_new_main_window():
    root.withdraw()  
    root.destroy()
    # Function to open the main page
def open_main(event):
    create_new_main_window()
    os.system(sys.executable + " main.py")
    root.destroy()
# Add a "home page" label outside the frame
home_label2 = tk.Label(root, text="Home Page!", font=("Impact", 12), fg="#410179",  cursor="hand2")
home_label2.place(x=1235, y=15)
# Bind the image label to the open_main function when clicked
image_label2.bind("<Button-1>", open_main)

admin_label3 = tk.Label(root, text="Admin Login Panel!", font=("Impact", 44, "bold"), fg="#5a46a7")
admin_label3.place(x=80, y=78)



root.mainloop()
