import tkinter as tk
from PIL import Image, ImageTk
import sqlite3
from datetime import datetime
import cv2
import pickle
import face_recognition
import time
from tkinter import messagebox
import sys
import os

# Create a central SQLite database connection
conn = sqlite3.connect('attendance_record.db')
cursor = conn.cursor()

# Get the current date in 'YYYY_MM_DD' format
today_date = datetime.now().strftime("%Y_%m_%d")

# Check if the table for today's date exists
table_name = f"attendance_record_{today_date}"
cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
existing_table = cursor.fetchone()

# If the table doesn't exist, create it and fetch employee data
if not existing_table:
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY,
            employee_id INTEGER,
            first_name TEXT,
            status TEXT,
            in_time DATETIME,
            out_time DATETIME,
            date DATE
        )
    ''')

    # Fetch employee data from the 'employee_data.db' and insert it into the new table
    employee_data_conn = sqlite3.connect('employee_data.db')
    employee_data_cursor = employee_data_conn.cursor()
    employee_data_cursor.execute("SELECT employee_id, first_name FROM employee_record")
    employee_data = employee_data_cursor.fetchall()
    employee_data_conn.close()

    for employee in employee_data:
        cursor.execute(f"INSERT INTO {table_name} (employee_id, first_name, status, date) VALUES (?, ?, ?, ?)",
                       (employee[0], employee[1], 'Absent', today_date))

    # Commit the changes to the central database
    conn.commit()

# Close the central database connection
conn.close()

root = tk.Tk()

 # Make the window fullscreen
root.geometry("{0}x{0}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

# Define StringVars to update Entry fields
employee_id_var = tk.StringVar()
first_name_var = tk.StringVar()
mark_button_text = tk.StringVar()

# Global variable to store the current employee's information
current_employee = None

# Dictionary to keep track of recognized employees and their status
recognized_employees = {}

# Initialize your webcam (you can also use an image file as the source)
camera = cv2.VideoCapture(0)
# Load the trained KNN model
with open("trained_knn_model.clf", 'rb') as f:
    knn_clf = pickle.load(f)
# Modify the mark_attendance_for_employee function
def mark_attendance_for_employee(employee_id_to_mark):
    global current_employee
    # Use a flag to track if the attendance for the current employee has been marked
    attendance_marked = False
    while not attendance_marked:
        # Capture a frame from the webcam
        (grabbed, frame) = camera.read()
        if not grabbed:
            return
        # Detect faces in the current frame
        face_locations = face_recognition.face_locations(frame)
        if face_locations:
            (top, right, bottom, left) = face_locations[0]  # Get the first detected face
            face = frame[top:bottom, left:right]
            # Encode the detected face
            face_encoding = face_recognition.face_encodings(frame, [(top, right, bottom, left)])[0]
            # Use the trained KNN model to predict the label (name) for the detected face
            closest_distances = knn_clf.kneighbors([face_encoding], n_neighbors=1)
            are_matches = [closest_distances[0][0][0] <= 0.5]
            if are_matches[0]:
                recognized_id = knn_clf.predict([face_encoding])[0]
                # Reconnect to the central database
                conn = sqlite3.connect('attendance_record.db')
                cursor = conn.cursor()

                # Fetch employee data from the database using recognized_id
                cursor.execute(f"SELECT employee_id, first_name, status, in_time, out_time FROM {table_name} WHERE employee_id = ?", (recognized_id,))
                employee_data = cursor.fetchone()

                if employee_data:
                    employee_id_var.set(recognized_id)
                    first_name_var.set(employee_data[1])
                    mark_button_text.set("Marked Attendance")

                    current_time = datetime.now().strftime("%I:%M:%S %p")  # 12-hour format with AM/PM

                    # Introduce a 3-second delay
                    time.sleep(3)

                    if employee_data[2] == "Absent":
                        if employee_data[3] is None:  # Check if "in time" is None
                            cursor.execute(f"UPDATE {table_name} SET in_time = ?, status = ? WHERE employee_id = ?", (current_time, "Present", recognized_id))
                    elif employee_data[2] == "Present":
                        if employee_data[3] is not None and employee_data[4] is None:  # Check if "in time" is not None and "out time" is None
                            cursor.execute(f"UPDATE {table_name} SET status = ?, out_time = ? WHERE employee_id = ?", ("Present(out)", current_time, recognized_id))
                    elif employee_data[2] == "Present(out)": 
                        if messagebox.showerror("Error", "already marked attendance"):
                          return

                    conn.commit()
                    attendance_marked = True  # Marked the attendance for the first detected face

                conn.close()
            else:
                # Face not recognized
                employee_id_var.set("Unknown")
                first_name_var.set("Unknown")

        # Display the detected face
        if len(face_locations) > 0:
            top, right, bottom, left = face_locations[0]
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, first_name_var.get(), (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Display the frame with the detected face
        cv2.imshow("Real-Time Face Recognition", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()

# Load the background image
bg_image = Image.open("m.png")  # Replace with the correct image path
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a label for the background image
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

# Function to continuously move the label
label_speed = 1  # Adjust this value to control the label movement speed
label_x = root.winfo_screenwidth()

# Function to continuously move the label
def move_label():
    global label_x
    label_x -= label_speed
    label.place(x=label_x, rely=0, anchor="n")  # Set rely to 0 for top placement
    label.lift()  # Raise the label to the top

    if label_x < -label.winfo_width():
        label_x = root.winfo_screenwidth()

    root.after(1, move_label)

# Create a label with white text
label = tk.Label(root, text="Face Recognition Attendance System", font=("impact", 70), bg="black", fg="purple")
label.place(relx=0.5, rely=0, anchor="n")  # Set rely to 0 for top placement

# Start moving the label
move_label()

# Create entry fields
entry_field1 = tk.Entry(root, font=("impact", 20, "bold"), width=30, textvariable=employee_id_var)
entry_field1.place(x=800, y=330)

entry_field2 = tk.Entry(root, font=("impact", 20, "bold"), width=30, textvariable=first_name_var)
entry_field2.place(x=800, y=430)

entry_field3 = tk.Entry(root, font=("impact", 20, "bold"), width=30, textvariable=mark_button_text)
entry_field3.place(x=800, y=530)

# Create a button to mark attendance
mark_button = tk.Button(root, text="Mark Attendance", font=("impact", 20, ), fg="purple", bg="white", command=lambda: mark_attendance_for_employee(employee_id_var.get()))
mark_button.place(x=300, y=500)

admin_label = tk.Label(root, text="Attendance Report", font=("impact", 50, "bold"), fg="purple", bg="#191919")
admin_label.place(x=730, y=200)


 # Load the second image
image3 = Image.open("b.png")
photo3 = ImageTk.PhotoImage(image3)
# Create and add a label to display the second image with a transparent background
image_label2 = tk.Label(root, image=photo3)
image_label2.place(x=1320, y=132)
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
home_label2 = tk.Label(root, text="Home Page!", font=("Impact", 13), fg="white", bg="#191919", cursor="hand2")
home_label2.place(x=1220, y=140)
home_label2.bind("<Button-1>", open_main)

# Start the Tkinter main loop
root.mainloop()
