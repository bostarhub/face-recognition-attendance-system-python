import sqlite3
import tkinter as tk
from tkinter import messagebox
import os
import sys
from PIL import Image, ImageTk

# Create or connect to the SQLite database
conn = sqlite3.connect('employee_data.db')
cursor = conn.cursor()

# Create an employees table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS admin_record(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        employee_id TEXT UNIQUE,
        first_name TEXT,
        last_name TEXT,
        email TEXT,
        password TEXT,
        mobile_number TEXT,
        address TEXT,
        image_data BLOB,
        designation TEXT,
        registration_time TEXT,
        registration_date TEXT
    )
''')

# Function to move the employee record to the admin_record table
def move_employee_to_admin_record():
    # Get values from entry fields
    id = id_entry.get()
    first_name = first_name_entry.get()

    if not id or not first_name:
        messagebox.showerror("Error", "Both fields must be filled")
        return

    # Check if the employee exists in admin_record by matching the id and first_name
    cursor.execute("SELECT * FROM admin_record WHERE id = ? AND first_name = ?", (id, first_name))
    admin_record = cursor.fetchone()

    if admin_record:
        messagebox.showinfo("Info", "Record already has admin access")
        id_entry.delete(0, 'end')  # Clear the entry fields
        first_name_entry.delete(0, 'end')
    else:
        # Check if the employee exists in employee_record by matching the id and first_name
        cursor.execute("SELECT * FROM employee_record WHERE id = ? AND first_name = ?", (id, first_name))
        employee_record = cursor.fetchone()

        if employee_record:
            # Check if the id already exists in admin_record
            cursor.execute("SELECT * FROM admin_record WHERE id = ?", (id,))
            existing_admin_record = cursor.fetchone()

            if existing_admin_record:
                messagebox.showerror("Error", "Record with the same ID already has admin access")
            else:
                # Move the record from employee_record to admin_record
                cursor.execute("INSERT INTO admin_record (employee_id, first_name, last_name, email, password, mobile_number, address, image_data, designation, registration_time, registration_date) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                               (employee_record[1], employee_record[2], employee_record[3], employee_record[4], employee_record[5], employee_record[6], employee_record[7], employee_record[8], employee_record[9], employee_record[10], employee_record[11]))
                conn.commit()

                messagebox.showinfo("Success", "Admin access granted to the employee")
                id_entry.delete(0, 'end')  # Clear the entry fields
                first_name_entry.delete(0, 'end')
        else:
            messagebox.showerror("Error", "Record not found in Source Records")

# Create a Tkinter window
window = tk.Tk()
window.geometry("{0}x{1}+0+0".format(window.winfo_screenwidth(), window.winfo_screenheight()))
window.title("Grant Admin Access")

# Load the background image
bg_image = Image.open("k.png")  # Replace with the path to your background image
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a label for the background image
bg_label = tk.Label(window, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

# Create a frame
frame = tk.Frame(window, width=450, height=440, bg="#5a46a7")
frame.place(x=610, y=240)

# Create entry fields
label = tk.Label(window, text="Admin Registration!", font=("Impact", 35), fg="white", bg="#5a46a7")
label.place(x=640, y=260)

# Create entry fields
id_label = tk.Label(window, text="Employee ID", font=("Impact", 20), fg="white", bg="#5a46a7")
id_label.place(x=640, y=350)

id_entry = tk.Entry(window, width=25, font=("Impact", 20))
id_entry.place(x=640, y=390)

first_name_label = tk.Label(window, text="First Name", font=("Impact", 17), fg="white", bg="#5a46a7")
first_name_label.place(x=640, y=450)

first_name_entry = tk.Entry(window, font=("Impact", 20), width=25)
first_name_entry.place(x=640, y=480)

# Create a button to grant admin access
grant_button = tk.Button(window, text="Grant Admin Access", font=("Impact", 15), bg="white", fg="#5a46a7", width=17, command=move_employee_to_admin_record)
grant_button.place(x=720, y=565)

 # Load the second image
image3 = Image.open("a.png")
photo3 = ImageTk.PhotoImage(image3)
# Create and add a label to display the second image with a transparent background
image_label2 = tk.Label(window, image=photo3)
image_label2.place(x=1330, y=0)
# Function to create a new main window
def create_new_main_window():
    window.withdraw()  
    window.destroy()
    # Function to open the main page
def open_main(event):
    create_new_main_window()
    os.system(sys.executable + " main.py")
    window.destroy()
# Add a "home page" label outside the frame
home_label2 = tk.Label(window, text="Home Page!", font=("Impact", 12), fg="white", bg="#191919", cursor="hand2")
home_label2.place(x=1235, y=5)
image_label2.bind("<Button-1>", open_main)

# Run the Tkinter main loop
window.mainloop()

# Close the database connection when done
conn.close()
