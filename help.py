import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import webbrowser

# Create a Tkinter window
root = tk.Tk()
root.title("Help")

# Function to open a new window
def open_window(window_title):
    new_window = tk.Toplevel(root)
    new_window.title(window_title)

# Function to open the main Python file
def open_main_file():
    import subprocess
    subprocess.Popen(['python', 'main.py'])  # Replace 'main.py' with your main Python file name

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create a "File" menu
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="back", command=open_main_file)

# Create a canvas to enable scrolling
canvas = tk.Canvas(root)
canvas.pack(side="left", fill="both", expand=True)

# Add a vertical scrollbar
vsb = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
vsb.pack(side="right", fill="y")
canvas.configure(yscrollcommand=vsb.set)

# Create a frame inside the canvas to hold the content
content_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=content_frame, anchor="nw")

# Load the image
image8 = Image.open("n.png")
photo8 = ImageTk.PhotoImage(image8)

# Create and add a label to display the image with a transparent background
image_label8 = tk.Label(content_frame, image=photo8)
image_label8.image = photo8  # Keep a reference to the image
image_label8.pack()

# Add a heading for the "Overview" paragraph
overview_heading = tk.Label(content_frame, text="Introduction", font=("impact", 30), fg="black", justify="left", wraplength=800)
overview_heading.pack(pady=20, anchor="w")  # Set anchor to "w" (west) to align it to the left

# Add paragraphs manually using label widgets
paragraph2 = "Face recognition technology has revolutionized employee authentication by providing a highly secure, convenient, and contactless means of confirming individuals' identities based on their unique facial features. This cutting-edge technology offers an accurate, swift, and hygienic method for employees to access workspaces, systems, and data, eliminating the need for passwords or access cards. With robust security measures, real-time tracking, and the flexibility to support remote access, face recognition not only enhances workplace security but also improves the overall employee experience, making it a valuable addition to modern organizations seeking efficient and secure authentication methods."
paragraph_label2 = tk.Label(content_frame, text=paragraph2, font=("godey", 15), justify="left", wraplength=1300, fg="grey")
paragraph_label2.pack(pady=20, anchor="w")

# Add a heading for the "Overview" paragraph
overview_heading = tk.Label(content_frame, text="Dashboard", font=("impact", 30), fg="black", justify="left", wraplength=800)
overview_heading.pack(pady=20, anchor="w")  # Set anchor to "w" (west) to align it to the left

# Add paragraphs manually using label widgets
paragraph2 = "Upon their first interaction with the system, users will have the primary option to RegisterAfter successfully registering, they can then proceed to Mark Attendance on a daily basis. This user-centric approach allows for a straightforward registration process followed by the daily attendance marking routine.\nFor administrators, they will have access to the administrative interface, where they can effectively manage employee attendance records and make necessary corrections, ensuring the system is efficient and caters to both user and admin needs."
paragraph_label2 = tk.Label(content_frame, text=paragraph2, font=("godey", 15), justify="left", wraplength=1300, fg="grey")
paragraph_label2.pack(pady=20, anchor="w")

# Load the image you want to add below the paragraph
image_below_paragraph = Image.open("7.png")
image_below_paragraph_photo = ImageTk.PhotoImage(image_below_paragraph)

# Create and add a label to display the image with a transparent background
image_below_paragraph_label = tk.Label(content_frame, image=image_below_paragraph_photo)
image_below_paragraph_label.image = image_below_paragraph_photo  # Keep a reference to the image
image_below_paragraph_label.pack(pady=20)

# Add a heading for the "Overview" paragraph
overview_heading = tk.Label(content_frame, text="Registration", font=("impact", 30), fg="black", justify="left", wraplength=800)
overview_heading.pack(pady=20, anchor="w")  # Set anchor to "w" (west) to align it to the left

# Add paragraphs manually using label widgets
paragraph2 = "The employee registration process is simple: they input their information, capture an image for facial recognition, train the system, and click Register to securely store their data. This ensures successful registration and enables them to use the face recognition system for attendance and access control."
paragraph_label2 = tk.Label(content_frame, text=paragraph2, font=("godey", 15), justify="left", wraplength=1300, fg="grey")
paragraph_label2.pack(pady=20, anchor="w")

# Load the image you want to add below the paragraph
image_below_paragraph = Image.open("8.png")
image_below_paragraph_photo = ImageTk.PhotoImage(image_below_paragraph)

# Create and add a label to display the image with a transparent background
image_below_paragraph_label = tk.Label(content_frame, image=image_below_paragraph_photo)
image_below_paragraph_label.image = image_below_paragraph_photo  # Keep a reference to the image
image_below_paragraph_label.pack(pady=20)

# Add a heading for the "Overview" paragraph
overview_heading = tk.Label(content_frame, text="Attendance Marking process", font=("impact", 30), fg="black", justify="left", wraplength=800)
overview_heading.pack(pady=20, anchor="w")  # Set anchor to "w" (west) to align it to the left

# Add paragraphs manually using label widgets
paragraph2 = "In the attendance marking process, employees can simply scan their face using the camera to mark their attendance in real-time. The system will automatically record their in-time and out-time, along with their employee ID and name, showing their attendance status. This process is typically exclusive to registered employees, ensuring that only authorized individuals can mark their attendance using the system."
paragraph_label2 = tk.Label(content_frame, text=paragraph2, font=("godey", 15), justify="left", wraplength=1300, fg="grey")
paragraph_label2.pack(pady=20, anchor="w")

# Load the image you want to add below the paragraph
image_below_paragraph = Image.open("9.png")
image_below_paragraph_photo = ImageTk.PhotoImage(image_below_paragraph)

# Create and add a label to display the image with a transparent background
image_below_paragraph_label = tk.Label(content_frame, image=image_below_paragraph_photo)
image_below_paragraph_label.image = image_below_paragraph_photo  # Keep a reference to the image
image_below_paragraph_label.pack(pady=20)



# Add a heading for the "Overview" paragraph
overview_heading = tk.Label(content_frame, text=" Attendance Management: ", font=("impact", 30), fg="black", justify="left", wraplength=800)
overview_heading.pack(pady=20, anchor="w")  # Set anchor to "w" (west) to align it to the left
# Add paragraphs manually using label widgets
paragraph2 = "Attendance management is a robust system that diligently records and stores attendance data for every employee, meticulously documenting both the date and time of their entries and exits. Each employee's individual records are associated with their unique identification, full name, in-time, and out-time, enabling a comprehensive and detailed overview of their attendance history. This organized approach not only enhances accuracy in attendance tracking but also facilitates streamlined workforce management, ensuring that the organization runs smoothly while maintaining precise and reliable attendance records for every employee." 
paragraph_label2 = tk.Label(content_frame, text=paragraph2, font=("godey", 15), justify="left", wraplength=1300, fg="grey")
paragraph_label2.pack(pady=20, anchor="w")

# Add a heading for the "Overview" paragraph
overview_heading = tk.Label(content_frame, text=" Administration", font=("impact",30), fg="black", justify="left", wraplength=800)
overview_heading.pack(pady=20, anchor="w")  # Set anchor to "w" (west) to align it to the left

# Add paragraphs manually using label widgets
paragraph2 = "In the admin's initial login, they are required to provide their credentials, which typically include a username and password for authentication. Once logged in, the admin gains access to an array of crucial functions, such as managing the system and overseeing access control. Administrators possess the capability to manage the attendance log, including the training and termination of facial recognition profiles for all employees. They can also grant access to new employees by providing them with system privileges, ensuring efficient management of the organization's workforce and access control, all from a centralized and secure platform."
paragraph_label2 = tk.Label(content_frame, text=paragraph2, font=("godey", 15), justify="left", wraplength=1300, fg="grey")
paragraph_label2.pack(pady=20, anchor="w")



# Load the image you want to add below the paragraph
image_below_paragraph = Image.open("10.png")
image_below_paragraph_photo = ImageTk.PhotoImage(image_below_paragraph)

# Create and add a label to display the image with a transparent background
image_below_paragraph_label = tk.Label(content_frame, image=image_below_paragraph_photo)
image_below_paragraph_label.image = image_below_paragraph_photo  # Keep a reference to the image
image_below_paragraph_label.pack(pady=20)



# Add a heading for the "Overview" paragraph
overview_heading = tk.Label(content_frame, text=" Security", font=("impact", 30), fg="black", justify="left", wraplength=800)
overview_heading.pack(pady=20, anchor="w")  # Set anchor to "w" (west) to align it to the left

# Add paragraphs manually using label widgets
paragraph2 = "Security is paramount in the system, with data stored in encrypted form to safeguard sensitive information. Employee images are stored securely to ensure that only authorized personnel can access them, prioritizing data privacy and protection. This encryption and access control measures provide a robust shield against unauthorized access to employee images, upholding the integrity of the system and guaranteeing that only approved individuals can manage and interact with employee data, fostering trust and security within the organization."
paragraph_label2 = tk.Label(content_frame, text=paragraph2, font=("godey", 15), justify="left", wraplength=1300, fg="grey")
paragraph_label2.pack(pady=20, anchor="w")

# Add a heading for the "Overview" paragraph
overview_heading = tk.Label(content_frame, text=" Conclusion", font=("impact", 30), fg="black", justify="left", wraplength=800)
overview_heading.pack(pady=20, anchor="w")  # Set anchor to "w" (west) to align it to the left

# Add paragraphs manually using label widgets
paragraph2 = "In conclusion, the Smart Attendance Management System using Face Recognition is a highly innovative and efficient solution for attendance management in various institutions.\nThe system uses state-of-the-art computer vision and deep learning algorithms to recognize individuals accurately and mark their attendance in real time.\nThis eliminates the need for manual attendance management, which is prone to errors and can be time-consuming.\nThe project also offers a user-friendly interface that displays live video streams and attendance logs, making it easy to use and understand.\nOverall, this project has great potential to revolutionize attendance management systems in various institutions and improve their efficiency and accuracy."
paragraph_label2 = tk.Label(content_frame, text=paragraph2, font=("godey", 15), justify="left", wraplength=1300, fg="grey")
paragraph_label2.pack(pady=20, anchor="w")


# Create a frame with a colored background for the content below the main text
extra_content_frame = tk.Frame(content_frame, bg="#5a46a7", width=1400, height=300)
extra_content_frame.pack(pady=0, anchor="w")

# Load the second image
image1 = Image.open("youtube.png")
image1_photo = ImageTk.PhotoImage(image1)

# Create a label for the second image and adjust its position
image_label2 = tk.Label(extra_content_frame, image=image1_photo, bg="#5a46a7")
image_label2.image = image1_photo
image_label2.place(x=260, y=200)  # Adjust the coordinates as needed

# Load the second image
image2 = Image.open("instagram.png")
image2_photo = ImageTk.PhotoImage(image2)

# Create a label for the second image and adjust its position
image_label2 = tk.Label(extra_content_frame, image=image2_photo, bg="#5a46a7")
image_label2.image = image2_photo
image_label2.place(x=510, y=200)  # Adjust the coordinates as needed

# Load the third image
image3 = Image.open("facebook.png")
image3_photo = ImageTk.PhotoImage(image3)

# Create a label for the third image and adjust its position
image_label3 = tk.Label(extra_content_frame, image=image3_photo, bg="#5a46a7")
image_label3.image = image3_photo
image_label3.place(x=760, y=200)  # Adjust the coordinates as needed

# Load the third image
image3 = Image.open("call.png")
image3_photo = ImageTk.PhotoImage(image3)

# Create a label for the third image and adjust its position
image_label3 = tk.Label(extra_content_frame, image=image3_photo, bg="#5a46a7")
image_label3.image = image3_photo
image_label3.place(x=1005, y=200)  # Adjust the coordinates as needed

def open_youtube():
    webbrowser.open("https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwibnNWg3KKCAxU_c_EDHSS3BggQtwJ6BAgOEAI&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3Dsz25xxF_AVE&usg=AOvVaw0ekhKXi-nfyUv7tOTR-D_b&opi=89978449")  # Replace with the desired Facebook URL

# Create a label with a colored background that represents the Facebook link
facebook_link_label = tk.Label(content_frame, text="https://www.youtube.com", fg="white", bg="#5a46a7", cursor="hand2")
facebook_link_label.place(x=310, y=4090)

# Bind the click event to open the Facebook link
facebook_link_label.bind("<Button-1>", lambda event: open_youtube())

def open_instagram():
    webbrowser.open("https://www.instagram.com/attendancekeeper/")  # Replace with the desired Facebook URL

# Create a label with a colored background that represents the Facebook link
facebook_link_label = tk.Label(content_frame, text="https://www.instagram.com", fg="white", bg="#5a46a7", cursor="hand2")
facebook_link_label.place(x=560, y=4090)

# Bind the click event to open the Facebook link
facebook_link_label.bind("<Button-1>", lambda event: open_instagram())

def open_facebook():
    webbrowser.open("https://m.facebook.com/yoursmartstaff/videos/smartstaffs-facial-recognition-attendance-system/405974608049455/")  # Replace with the desired Facebook URL

# Create a label with a colored background that represents the Facebook link
facebook_link_label = tk.Label(content_frame, text="https://www.facebook.com", fg="white", bg="#5a46a7", cursor="hand2")
facebook_link_label.place(x=810, y=4090)

# Bind the click event to open the Facebook link
facebook_link_label.bind("<Button-1>", lambda event: open_facebook())

# Create a label with a colored background that represents the Facebook link
facebook_link_label = tk.Label(content_frame, text="03086633693\n03067148720", fg="white", bg="#5a46a7")
facebook_link_label.place(x=1050, y=4085)

# Create a label with a colored background that represents the Facebook link
facebook_link_label = tk.Label(content_frame, text="Contact Us", fg="white", bg="#5a46a7", font=("impact", 50))
facebook_link_label.place(x=50, y=3920)

# Make the window fullscreen
root.geometry("{0}x{0}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

root.update_idletasks()  # Update the window idle tasks to properly set the canvas size
canvas.config(scrollregion=canvas.bbox("all"))  # Set the scroll region based on the canvas content
# You can replace "your_color" with the color you want to use, e.g., "blue" or a hexadecimal color code.

root.mainloop()
