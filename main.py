import tkinter as tk
from tkinter import simpledialog
from PIL import Image, ImageTk
from tkinter import messagebox
import subprocess
import sys
import tkinter as tk
import random

def open_window(window_title):
    new_window = tk.Toplevel(root)
    new_window.title(window_title)
def open_help():
    import subprocess
    subprocess.Popen(['python', 'help.py'])  # Replace 'help.py' with the actual name of your Python help script

# Function to change label appearance when clicked
def label_click(label):
    label.config(fg="red", font=("godey", 15, "bold", "underline"))
    open_python_file(label.cget("text").lower().replace(" ", "") + ".py")

# Function to reset label appearance on hover exit
def reset_label(label):
    label.config(fg="white", font=("godey", 13, "bold"))

# Function to open a Python file
def open_python_file(file_name):
    root.withdraw() 
    try:
        subprocess.Popen(["python", file_name])
    except FileNotFoundError:
        # If the file does not exist, create it with a placeholder
        with open(file_name, "w") as placeholder:
            placeholder.write("# This is a placeholder for the module")
            root.deiconify()  

# Function to create a new main window
def create_new_main_window():
    root.withdraw()  
    root.destroy()
    main()

# Function to open the "overview.py" file
def open_overview_file():
    root.withdraw()  
    open_python_file("overview.py")

def random_color():
    return "#{:02x}{:02x}{:02x}".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Function to change label text color
def change_label_color(label):
    label.config(fg=random_color())
    root.after(200, change_label_color, label)
   
def main():
    global root
    root = tk.Tk()
    root.title("Face Recognition System")
    # Make the window fullscreen
    root.geometry("{0}x{0}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

    # Create a frame
    frame = tk.Frame(root, width=315, height=780, bg="#5a46a7")
    frame.place(x=0, y=0)

    # Load the second image
    image2 = Image.open("a.png")
    photo2 = ImageTk.PhotoImage(image2)

    # Create and add a label to display the second image with a transparent background
    image_label2 = tk.Label(frame, image=photo2)
    image_label2.place(x=10, y=10)

    # Load the second image
    image3 = Image.open("b.png")
    photo3 = ImageTk.PhotoImage(image3)

    # Create and add a label to display the second image with a transparent background
    image_label3 = tk.Label(frame, image=photo3)
    image_label3.place(x=10, y=250)

    # Load the second image
    image4 = Image.open("c.png")
    photo4 = ImageTk.PhotoImage(image4)

    # Create and add a label to display the second image with a transparent background
    image_label4 = tk.Label(frame, image=photo4)
    image_label4.place(x=10, y=317)

    # Load the second image
    image5 = Image.open("d.png")
    photo5 = ImageTk.PhotoImage(image5)

    # Create and add a label to display the second image with a transparent background
    image_label5 = tk.Label(frame, image=photo5)
    image_label5.place(x=10, y=387)

    # Add a "NEW USER!" label outside the frame
    welcome_label2 = tk.Label(frame, text="Dashboard", font=("Impact", 45, "bold"), fg="white", bg="#5a46a7")
    welcome_label2.place(x=5, y=100)

    # Load the image
    image7 = Image.open("e.png")
    photo7 = ImageTk.PhotoImage(image7)

    # Create and add a label to display the image with a transparent background
    image_label7 = tk.Label(root, image=photo7)
    image_label7.place(x=490, y=340)

    # Load the image
    image8 = Image.open("f.png")
    photo8 = ImageTk.PhotoImage(image8)
   
    # Create and add a label to display the image with a transparent background
    image_label8 = tk.Label(root, image=photo8)
    image_label8.place(x=900, y=340)

    # Add a "home page" label outside the frame
    home_label2 = tk.Label(frame, text="Home Page!", font=("Impact", 10), fg="WHITE", bg="#5a46a7", cursor="hand2")
    home_label2.place(x=50, y=15)
    home_label2.bind("<Button-1>", lambda event: create_new_main_window())

    # Create the "Face Recognition System" label with changing color
    system_label2 = tk.Label(root, text="Face Recognition System", font=("Impact", 65, "bold"), fg="white")
    system_label2.place(x=380, y=30)
    change_label_color(system_label2)

    # Create labels for "Overview," "Mark Attendance," "View Attendance Report," and "Log Out"
    labels = []
    for i, text in enumerate(["Overview", "About" , "Close"]):
        label = tk.Label(frame, text=text, font=("godey", 13, "bold"), fg="white", bg="#5a46a7", cursor="hand2")
        label.place(x=50, y=250 + i * 70)
        labels.append(label)
        if text == "Overview":
            label.bind("<Button-1>", lambda event, label=label: open_overview_file())
            root.withdraw()
        else:
            label.bind("<Button-1>", lambda event, label=label: label_click(label))
        label.bind("<Enter>", lambda event, label=label: label.config(fg="red", font=("godey", 13, "bold", "underline")))
        label.bind("<Leave>", lambda event, label=label: reset_label(label))
        
    def open_login_script():
        root.withdraw()  
        try:
            subprocess.Popen([sys.executable, 'admin_login.py'], shell=True, creationflags=subprocess.CREATE_NEW_CONSOLE)
        except Exception as e:
            messagebox.showerror("Error", "An error occurred: " + str(e))

    # Create a "admin" button
    btn_login = tk.Button(root, text="Admin", command=open_login_script, fg="white", padx=92, pady=5, font=("Arial", 15, "bold"), bg="#5a46a7")
    btn_login.place(x=490, y=550)
    root.deiconify()  

    def open_markattendance_script():
        root.withdraw()  
        try:
            subprocess.Popen([sys.executable, 'markattendance.py'], shell=True, creationflags=subprocess.CREATE_NEW_CONSOLE)
        except Exception as e:
            messagebox.showerror("Error", "An error occurred: " + str(e))

    # Create a "mark attendance" button
    btn_login = tk.Button(root, text="Mark Attendance", command=open_markattendance_script, fg="white", padx=42, pady=5, font=("Arial", 15, "bold"), bg="#5a46a7")
    btn_login.place(x=900, y=550)
    root.deiconify() 
    # Function to open a new window

    root.mainloop()

# Initial run
main()
