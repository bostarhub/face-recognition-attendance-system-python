import tkinter as tk
from PIL import Image, ImageTk
import sys
import os  # Added for file path manipulation

# New global variable to track new data arrival
new_data_arrived = False

# Function to open the admin registration script
def open_admin_registration():
    root.withdraw()  # Hide the registration window
    os.system(sys.executable + " admin_registration.py")
    root.deiconify()  # Show the registration window again
    
def open_admin_logout():
    root.withdraw()
    os.system(sys.executable + " admin_logout.py")
    root.destroy()

# Function to open the admin login script
def open_admin_logreport():
    root.withdraw()
    os.system(sys.executable + " admin_logreport.py")
    root.destroy()

    # Function to open the admin login script
def open_admin_train():
    os.system(sys.executable + " admin_train.py")
    root.destroy()

def open_main():
    root.withdraw()
    os.system(sys.executable + " main.py")
    root.destroy()

root = tk.Tk()
root.title("Administration")
# Make the window fullscreen
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

frame = tk.Frame(root, width=690, height=800, bg="black")
frame.place(x=0, y=0)

# Load the first image
image1 = Image.open("o.png")
photo1 = ImageTk.PhotoImage(image1)

image_label1 = tk.Label(frame, image=photo1, bg="black")
image_label1.place(x=0, y=110)

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
    root.withdraw()
    create_new_main_window()
    os.system(sys.executable + " main.py")
    root.destroy()

def open_employee():
    root.withdraw()
    create_new_main_window()
    os.system(sys.executable + " employeeregistration.py")
    root.destroy()
# Add a "home page" label outside the frame
home_label2 = tk.Label(root, text="Home Page!", font=("Impact", 13), fg="#ff4500",  cursor="hand2")
home_label2.place(x=1230, y=15)
image_label2.bind("<Button-1>", open_main)

admin_label2 = tk.Label(root, text="Admin Panel!", font=("Impact", 43, "bold"), fg="black")
admin_label2.place(x=790, y=0)

registration_button = tk.Button(root, text="Recruit Employee", font=("goady", 18, "bold"), width=20, bg="#ff4500", fg="black", command=open_employee)
registration_button.place(x=870, y=100)

# Create a button for admin registration
registration_button = tk.Button(root, text="Recruit Admin", font=("goady", 18, "bold"), width=20, bg="#ff4500", fg="black", command=open_admin_registration)
registration_button.place(x=870, y=220)

login_button = tk.Button(root, text="Attendance Log", font=("goady", 18, "bold"), width=20, bg="#ff4500", command=open_admin_logreport)
login_button.place(x=870, y=350)
# Create a button for admin training
train_button = tk.Button(root, text="Training", font=("goady", 18, "bold"), width=20, fg="white", bg="#410179", command=open_admin_train)
train_button.place(x=870, y=480)

# Logic to toggle the "Train" button color
def check_new_data():
    global new_data_arrived
    # Check for new data here; set new_data_arrived to True if new data arrives
    # For demonstration purposes, we'll set it to True here
    new_data_arrived = True

    if new_data_arrived:
        train_button.config(fg="black", bg="#ff4500")  # Blue color
    else:
        train_button.config(fg="white", bg="#410179")  # Default color
    root.after(1000, check_new_data)  # Check for new data every 1 second
check_new_data()  # Start checking for new data

login_button = tk.Button(root, text="Terminating", font=("goady", 18, "bold"), width=20, bg="#ff4500", command=open_admin_logout)
login_button.place(x=870, y=610)

# Create a canvas for drawing lines
canvas = tk.Canvas(root, width=450, height=3, bg="black", highlightthickness=0)
canvas.place(x=800, y=190)

# Add the "OR" text
or_label = tk.Label(root, text=" OR ", font=("goady", 15, "bold"), fg="#ff4500")
or_label.place(x=1000, y=170)

# Create a canvas for drawing lines
canvas = tk.Canvas(root, width=450, height=3, bg="black", highlightthickness=0)
canvas.place(x=800, y=441)

# Add the "OR" text
or_label = tk.Label(root, text=" OR ", font=("goady", 15, "bold"), fg="#ff4500")
or_label.place(x=1000, y=425)

# Create a canvas for drawing lines
canvas = tk.Canvas(root, width=450, height=3, bg="black", highlightthickness=0)
canvas.place(x=800, y=313)

# Add the "OR" text
or_label = tk.Label(root, text=" OR ", font=("goady", 15, "bold"), fg="#ff4500")
or_label.place(x=1000, y=300)

# Create a canvas for drawing lines
canvas = tk.Canvas(root, width=450, height=3, bg="black", highlightthickness=0)
canvas.place(x=800, y=570)

# Add the "OR" text
or_label = tk.Label(root, text=" OR ", font=("goady", 15, "bold"), fg="#ff4500")
or_label.place(x=1000, y=558)

root.mainloop()
