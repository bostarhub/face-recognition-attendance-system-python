import tkinter as tk
from tkinter import ttk 
from tkinter import messagebox
from PIL import Image, ImageFilter, ImageEnhance
import os
import re
import sqlite3
from datetime import datetime
import sys
import cv2
from imutils import face_utils
from PIL import ImageTk
import dlib
import imutils
import time
import shutil

# Initialize the face detector
detector = dlib.get_frontal_face_detector()

# Create or connect to the SQLite database
conn = sqlite3.connect('employee_data.db')
cursor = conn.cursor()

# Create an employees table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS employee_record(
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

# Global variables to track image capture and training success
image_capture_successful = False
training_successful = False

# Function to validate input fields
def validate_input():
    employee_id = entry_employee_id.get()
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    email = entry_email.get()
    password = entry_password.get()
    mobile_number = entry_mobile_number.get()
    address = entry_address.get()
    designation = entry_designation.get()

    if not re.match("^[0-9a-zA-Z]+$", employee_id):
        messagebox.showerror("Error", "Invalid Employee ID (Only alphanumeric characters allowed)")
        return False

    if not (re.match("^[a-zA-Z]+$", first_name) and re.match("^[a-zA-Z]+$", last_name)):
        messagebox.showerror("Error", "Invalid First Name or Last Name (Only letters allowed)")
        return False

    if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zAZ0-9-.]+$', email):
        messagebox.showerror("Error", "Invalid Email Format")
        return False

    if len(password) < 6:
        messagebox.showerror("Error", "Password must be at least 6 characters long")
        return False

    if not re.match("^[0-9]{11}$", mobile_number):
        messagebox.showerror("Error", "Invalid Mobile Number (11 digits allowed)")
        return False

    if not re.match("^[0-9a-zA-Z]+$", address):
        messagebox.showerror("Error", "Invalid Address (Only alphanumeric characters allowed)")
        return False

    if not re.match("^[0-9a-zA-Z]+$", designation):
        messagebox.showerror("Error", "Invalid Designation (Only alphanumeric characters allowed)")
        return False

    return True

# Function to generate a unique employee ID
def generate_employee_id():
    timestamp = int(time.time())
    employee_id = f"EMP{timestamp}"
    entry_employee_id.delete(0, tk.END)
    entry_employee_id.insert(0, employee_id)
    entry_employee_id.config(state='readonly')  # Disable the entry widget

# Function to capture employee images
def capture_image_callback():
    global image_capture_successful
    name = entry_employee_id.get()
    first_name = entry_first_name.get()
    number = 0
    folder_name = "dataset1/" + name

    if not validate_input():
        messagebox.showerror("Error", "Please fill in all the fields correctly before capturing images.")
        return
    if os.path.exists(folder_name):
        print("Folder exists")
    else:
        os.makedirs(folder_name)
    camera = cv2.VideoCapture(0)
    while True:
        (grabbed, image) = camera.read()
        if grabbed:
            if image is not None and image.shape[0] > 0 and image.shape[1] > 0:
                image = imutils.resize(image, width=500)
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                rects = detector(gray, 1)
                for (i, rect) in enumerate(rects):
                    (x, y, w, h) = face_utils.rect_to_bb(rect)
                    cro = image[y: y + h, x: x + w]
                    out_image = cv2.resize(cro, (108, 108))
                    image_name = f"{name}_{first_name}_{number}.jpg"
                    fram = os.path.join(folder_name, image_name)
                    number += 1
                    cv2.imwrite(fram, out_image)
                    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            else:
                print("Failed to grab a frame")
            # Display a progress bar on the camera feed
            progress_value = (number / 10) * 100  # Calculate progress value
            cv2.rectangle(image, (10, 10), (int(10 + progress_value * 2), 20), (0, 255, 0), -1)  # Draw the progress bar
            cv2.putText(image, f"Progress: {int(progress_value)}%", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            cv2.imshow("Camera Feed", image)  # Display the camera feed
        if number >= 10:
            break
        # Introduce a delay of 500 milliseconds between capturing each image
        cv2.waitKey(500)
    camera.release()
    cv2.destroyAllWindows()

    if number > 0:
        image_capture_successful = True
        messagebox.showinfo("Image Capture Successful", "Images captured successfully")

# Function to open the face training script
def open_face_train():
    global training_successful
    if not image_capture_successful:
        messagebox.showerror("Error", "Please ensure image capture was successful before training.")
    else:
        if os.system(sys.executable + " face_train.py") == 0:
            training_successful = True
            messagebox.showinfo("Training Successful", "Face training successful.")
        else:
            messagebox.showerror("Error", "Face training failed.")

# Function to open the main application
def open_main():
    root.withdraw() 
    os.system(sys.executable + " main.py")
    root.destroy()

# Function to save employee data
def save_employee_data():
    global image_capture_successful  # Declare the variable as global

    if not (image_capture_successful and training_successful and validate_input()):
        messagebox.showerror("Error", "Ensure successful image capture and training before registering.")
        return

    employee_id = entry_employee_id.get()
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    email = entry_email.get()
    password = entry_password.get()
    mobile_number = entry_mobile_number.get()
    address = entry_address.get()
    designation = entry_designation.get()
    registration_date = datetime.now().date()
    registration_time = datetime.now().time().strftime('%H:%M:%S')

 # Insert the employee data and image data into the database
    with open(f"dataset1/{employee_id}/{employee_id}_{first_name}_0.jpg", "rb") as image_file:
        image_data = image_file.read()

    cursor.execute('''
        INSERT INTO employee_record (
            employee_id, first_name, last_name, email, password, mobile_number, address, designation,
            registration_date, registration_time, image_data
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (employee_id, first_name, last_name, email, password, mobile_number, address, designation, registration_date, registration_time, sqlite3.Binary(image_data)))

    # Move the entire folder from "dataset1" to "dataset"
    source_folder = f'dataset1/{employee_id}'
    target_folder = 'dataset'
    shutil.move(source_folder, target_folder)
    conn.commit()

    messagebox.showinfo("Success", "Employee data registered successfully.")

# Create the main tkinter window
root = tk.Tk()
root.title("Employee Registration Page")
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

# Create and place the input fields with labels
label_employee_id = tk.Label(root, text="Employee ID", fg="#512da8", font=("impact", 17))
label_employee_id.place(x=115, y=117)
entry_employee_id = tk.Entry(root, width=20, font=("godey", 15, "bold"))
entry_employee_id.place(x=235, y=120)


btn_generate_id = tk.Button(root, text="Generate ID", fg="white", bg="#512da8", command=generate_employee_id, padx=20, pady=2)
btn_generate_id.place(x=345, y=155)

label_first_name = tk.Label(root, text="First Name", fg="#512da8", font=("impact", 17))
label_first_name.place(x=115, y=190)
entry_first_name = tk.Entry(root, width=20, font=("godey", 15, "bold"))
entry_first_name.place(x=235, y=195)

label_last_name = tk.Label(root, text="Last Name", fg="#512da8", font=("impact", 17))
label_last_name.place(x=115, y=250)
entry_last_name = tk.Entry(root, width=20, font=("godey", 15, "bold"))
entry_last_name.place(x=235, y=255)

label_email = tk.Label(root, text="Email", fg="#512da8", font=("impact", 17))
label_email.place(x=115, y=305)
entry_email = tk.Entry(root, width=20, font=("godey", 15, "bold"))
entry_email.place(x=235, y=310)

label_password = tk.Label(root, text="Password", fg="#512da8", font=("impact", 17))
label_password.place(x=115, y=365)
entry_password = tk.Entry(root, width=20, show='*', font=("godey", 15, "bold"))
entry_password.place(x=235, y=370)

label_mobile_number = tk.Label(root, text="Mobile No", fg="#512da8", font=("impact", 17))
label_mobile_number.place(x=115, y=435)
entry_mobile_number = tk.Entry(root, width=20, font=("godey", 15, "bold"))
entry_mobile_number.place(x=235, y=435)

label_address = tk.Label(root, text="Address", fg="#512da8", font=("impact", 17))
label_address.place(x=115, y=495)
entry_address = tk.Entry(root, width=20, font=("godey", 15, "bold"))
entry_address.place(x=235, y=500)

label_designation = tk.Label(root, text="Designation", fg="#512da8", font=("impact", 17))
label_designation.place(x=115, y=555)
entry_designation = tk.Entry(root, width=20, font=("godey", 15, "bold"))
entry_designation.place(x=235, y=560)

# Create the "Capture Image" button
btn_capture_image = tk.Button(root, text="Capture Image", fg="white", bg="#512da8", padx=15, pady=4, font=("godey", 15, "bold"), command=capture_image_callback)
btn_capture_image.place(x=805, y=620)

# Create the "Face Train" button
btn_face_train = tk.Button(root, text="Face Train", fg="white", bg="#512da8", padx=20, pady=4, font=("godey", 15, "bold"), command=open_face_train)
btn_face_train.place(x=1050, y=620)

# Create the "Register" button
btn_register = tk.Button(root, text="Register", fg="white", bg="#512da8", padx=100, pady=4, font=("godey", 15, "bold"), command=save_employee_data)
btn_register.place(x=130, y=620)

 # Load the second image
image3 = Image.open("a.png")
photo3 = ImageTk.PhotoImage(image3)
# Create and add a label to display the second image with a transparent background
image_label2 = tk.Label(root, image=photo3)
image_label2.place(x=1320, y=10)
# Function to create a new main window
def create_new_main_window():
    root.withdraw()  
    # Function to open the main page
def open_main(event):
    create_new_main_window()
    os.system(sys.executable + " main.py")
    root.destroy()
# Add a "home page" label outside the frame
home_label2 = tk.Label(root, text="Home Page!", font=("Impact", 13), fg="#512da8",  cursor="hand2")
home_label2.place(x=1230, y=15)
image_label2.bind("<Button-1>", open_main)

root.title("Employee Registration Page")
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

image1 = Image.open("i.png")
image1 = image1.filter(ImageFilter.GaussianBlur(5))
photo1 = ImageTk.PhotoImage(image1)

image_label1 = tk.Label(root, image=photo1)
image_label1.place(x=805, y=70)

image2 = Image.open("j.png")
image2 = image2.filter(ImageFilter.EDGE_ENHANCE_MORE)
enhancer = ImageEnhance.Color(image2)
image2 = enhancer.enhance(1.0)
photo2 = ImageTk.PhotoImage(image2)

image_label2 = tk.Label(root, image=photo2)
image_label2.place(x=850, y=140)

admin_label3 = tk.Label(root, text="Employee Registration Panel!", font=("Impact", 30, "bold"), fg="#512da8")
admin_label3.place(x=40, y=25)

root.mainloop()


