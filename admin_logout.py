import sqlite3
import tkinter as tk
import os
from datetime import datetime
from tkinter import messagebox
from PIL import Image, ImageTk
import sys

# Create or connect to the SQLite database
conn = sqlite3.connect('employee_data.db')
cursor = conn.cursor()

# Create a logout_records table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS logout_records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        employee_id TEXT,
        first_name TEXT,
        last_name TEXT,
        email TEXT,
        password TEXT,
        mobile_number TEXT,
        address TEXT,
        image_data BLOB,
        designation TEXT,
        registration_time TEXT,
        registration_date TEXT,
        logout_time TEXT,
        logout_date TEXT
    )
''')

# Function to move image data to the "logoutdataset" folder and delete from source
def move_image_data(employee_id):
    source_folder = 'dataset'  # Folder where all image data is currently stored
    target_folder = 'logoutdataset'  # Folder where image data will be moved

    # Ensure the target folder exists or create it
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    # List all files in the source folder
    files = os.listdir(source_folder)

    for filename in files:
        if filename.startswith(employee_id):
            source_path = os.path.join(source_folder, filename)
            target_path = os.path.join(target_folder, filename)
            
            # Move the image data to the "logoutdataset" folder
            os.rename(source_path, target_path)

# Function to move the employee record to the logout_records table and delete from source/admin_record
def move_employee_to_logout_records():
    # Get values from entry fields
    employee_id = id_entry.get()
    first_name = first_name_entry.get()

    if not employee_id or not first_name:
        messagebox.showerror("Error", "Both fields must be filled")
        return

    current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Get the current date and time

    # Check if the employee exists in employee_record by matching the id
    cursor.execute("SELECT * FROM employee_record WHERE employee_id = ? AND first_name = ?", (employee_id, first_name))
    employee_record = cursor.fetchone()

    if employee_record:
        # Move the image data to the "logoutdataset" folder and delete from source
        move_image_data(employee_id)

        # Move the record from employee_record to logout_records and set the current date and time
        cursor.execute("INSERT INTO logout_records (employee_id, first_name, last_name, email, password, mobile_number, address, image_data, designation, registration_time, registration_date, logout_time, logout_date) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                       (employee_record[1], employee_record[2], employee_record[3], employee_record[4], employee_record[5], employee_record[6], employee_record[7], employee_record[8], employee_record[9], employee_record[10], employee_record[11], current_datetime, current_datetime))
        conn.commit()

        # Delete the record from employee_record
        cursor.execute("DELETE FROM employee_record WHERE employee_id = ?", (employee_id,))
        conn.commit()

        # Check if the employee_id exists in admin_record
        cursor.execute("SELECT * FROM admin_record WHERE employee_id = ?", (employee_id,))
        admin_record = cursor.fetchone()

        if admin_record:
            # Delete the record from admin_record
            cursor.execute("DELETE FROM admin_record WHERE employee_id = ?", (employee_id,))
            conn.commit()

        messagebox.showinfo("Success", "Record Moved to Logout Records and Images Deleted from Source Records")
        id_entry.delete(0, 'end')  # Clear the entry fields
        first_name_entry.delete(0, 'end')
    else:
        messagebox.showerror("Error", "Record not found in Source Records")

# Create a Tkinter window
window = tk.Tk()
window.geometry("{0}x{1}+0+0".format(window.winfo_screenwidth(), window.winfo_screenheight()))
window.title("Employee Log-Out")

# Load the background image
bg_image = Image.open("l.png")  # Replace with the path to your background image
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a label for the background image
bg_label = tk.Label(window, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

# Create a frame in the center with a white background
frame = tk.Frame(window, bg="white", height=500, width=470)
frame.place(x=50, y=80,)

admin_label2 = tk.Label(window, text="Employee Logout!", font=("Impact", 35, "bold"), bg="white", fg="#5a46a7")
admin_label2.place(x=70, y=100)

# Create entry fields
id_label = tk.Label(window, text="Employee ID", font=("Impact", 20), fg="#5a46a7", bg="white")
id_label.place(x=120, y=200)

id_entry = tk.Entry(window, width=20, font=("Impact", 20))
id_entry.place(x=120, y=240)

first_name_label = tk.Label(window, text="First Name", font=("Impact", 20), fg="#5a46a7", bg="white")
first_name_label.place(x=120, y=300)

first_name_entry = tk.Entry(window, font=("Impact", 20), width=20)
first_name_entry.place(x=120, y=340)

# Create a button to move the record
move_button = tk.Button(window, text="Logout", font=("Impact", 15), fg="white", bg="#5a46a7", width=15, command=move_employee_to_logout_records)
move_button.place(x=170, y=420)

 # Load the second image
image3 = Image.open("a.png")
photo3 = ImageTk.PhotoImage(image3)
# Create and add a label to display the second image with a transparent background
image_label2 = tk.Label(window, image=photo3)
image_label2.place(x=1320, y=0)
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
home_label2 = tk.Label(window, text="Home Page!", font=("Impact", 13), fg="white", bg="#191919", cursor="hand2")
home_label2.place(x=1220, y=10)
home_label2.bind("<Button-1>", open_main)

# Run the Tkinter main loop
window.mainloop()

# Close the database connection when done
conn.close()
