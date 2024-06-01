import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import webbrowser

# Create a Tkinter window
root = tk.Tk()
root.title("Face Recognition Attendance System")

# Function to open a new window
def open_window(window_title):
    new_window = tk.Toplevel(root)
    new_window.title(window_title)

# Function to open the main Python file
def open_main_file():
    import subprocess
    subprocess.Popen(['python', 'main.py'])  # Replace 'main.py' with your main Python file name

def open_help():
    import subprocess
    subprocess.Popen(['python', 'help.py'])  # Replace 'help.py' with the actual name of your Python help script

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create a "File" menu
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Back", command=open_main_file)

# Create a "Help" menu
help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="About", command=open_help)

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
overview_heading = tk.Label(content_frame, text="|Overview", font=("impact", 30), fg="black", justify="left", wraplength=800)
overview_heading.pack(pady=20, anchor="w")  # Set anchor to "w" (west) to align it to the left

# Add paragraphs manually using label widgets
paragraph2 = "The Smart Attendance System Using Face Recognition is a software application that automates attendance-taking using facial recognition technology. It eliminates the need for manual attendance-taking, which is time-consuming and prone to errors. This system enables the recognition of a person's identity using a camera and compares it with the database to record attendance."
paragraph_label2 = tk.Label(content_frame, text=paragraph2, font=("godey", 15), justify="left", wraplength=1300, fg="grey")
paragraph_label2.pack(pady=20, anchor="w")

# Add a heading for the "Overview" paragraph
overview_heading = tk.Label(content_frame, text="What are We Building?", font=("impact", 30), fg="black", justify="left", wraplength=800)
overview_heading.pack(pady=20, anchor="w")  # Set anchor to "w" (west) to align it to the left

# Add paragraphs manually using label widgets
paragraph2 = "We are building a Smart Attendance System Using Face Recognition that can automatically take attendance using facial recognition technology. The system will use a camera to capture the face of each person and match it with the database to identify them. The system will store attendance records for each person in an Excel file and generates a report."
paragraph_label2 = tk.Label(content_frame, text=paragraph2, font=("godey", 15), justify="left", wraplength=1300, fg="grey")
paragraph_label2.pack(pady=20, anchor="w")

# Load the image you want to add below the paragraph
image_below_paragraph = Image.open("1.png")
image_below_paragraph_photo = ImageTk.PhotoImage(image_below_paragraph)

# Create and add a label to display the image with a transparent background
image_below_paragraph_label = tk.Label(content_frame, image=image_below_paragraph_photo)
image_below_paragraph_label.image = image_below_paragraph_photo  # Keep a reference to the image
image_below_paragraph_label.pack(pady=20)

# Add a heading for the "Overview" paragraph
overview_heading = tk.Label(content_frame, text="Pre-requisites", font=("impact", 30), fg="black", justify="left", wraplength=800)
overview_heading.pack(pady=20, anchor="w")  # Set anchor to "w" (west) to align it to the left

# Add paragraphs manually using label widgets
paragraph2 = "To build this system, we need a basic understanding of programming languages such as Python and knowledge of facial recognition technology. \n Additionally, we require a computer with a webcam, internet connectivity, and a Python IDE. \n We also need to have libraries like OpenCV, face_recognition, and NumPy pre-installed on our computers."
paragraph_label2 = tk.Label(content_frame, text=paragraph2, font=("godey", 15), justify="left", wraplength=1300, fg="grey")
paragraph_label2.pack(pady=20, anchor="w")

# Add a heading for the "Overview" paragraph
overview_heading = tk.Label(content_frame, text="We Going to Build this?", font=("impact", 30), fg="black", justify="left", wraplength=800)
overview_heading.pack(pady=20, anchor="w")  # Set anchor to "w" (west) to align it to the left

# Add paragraphs manually using label widgets
paragraph2 = "We will build this face detection attendance system using Python programming language and facial recognition technology. We will use the OpenCV library to capture images from a webcam, detect faces, and extract facial features. We will then use the face_recognition library to recognize faces and compare them with the database to identify people. Finally, we will store the attendance records in a database and generate reports using NumPy."
paragraph_label2 = tk.Label(content_frame, text=paragraph2, font=("godey", 15), justify="left", wraplength=1300, fg="grey")
paragraph_label2.pack(pady=20, anchor="w")

# Load the image you want to add below the paragraph
image_below_paragraph = Image.open("2.png")
image_below_paragraph_photo = ImageTk.PhotoImage(image_below_paragraph)

# Create and add a label to display the image with a transparent background
image_below_paragraph_label = tk.Label(content_frame, image=image_below_paragraph_photo)
image_below_paragraph_label.image = image_below_paragraph_photo  # Keep a reference to the image
image_below_paragraph_label.pack(pady=20)


# Add a heading for the "Overview" paragraph
overview_heading = tk.Label(content_frame, text="Requirements", font=("impact", 30), fg="black", justify="left", wraplength=800)
overview_heading.pack(pady=20, anchor="w")  # Set anchor to "w" (west) to align it to the left

# Add a heading for the "Overview" paragraph
overview_heading = tk.Label(content_frame, text="Hardware Requirements: ", font=("impact", 15), fg="grey", justify="left", wraplength=800)
overview_heading.pack(pady=20, anchor="w")  # Set anchor to "w" (west) to align it to the left
# Add paragraphs manually using label widgets
paragraph2 = " A computer with a webcam and internet connectivity is needed to run the system. The webcam should have a resolution of at least 720p to capture clear images."
paragraph_label2 = tk.Label(content_frame, text=paragraph2, font=("godey", 15), justify="left", wraplength=1300, fg="grey")
paragraph_label2.pack(pady=20, anchor="w")

# Add a heading for the "Overview" paragraph
overview_heading = tk.Label(content_frame, text="Software Requirements: ", font=("impact", 15), fg="grey", justify="left", wraplength=800)
overview_heading.pack(pady=20, anchor="w")  # Set anchor to "w" (west) to align it to the left
# Add paragraphs manually using label widgets
paragraph2 = " The system will be built using Python programming language. The required software includes a Python IDE like PyCharm or Spyder, OpenCV library, face_recognition library, and NumPy library."
paragraph_label2 = tk.Label(content_frame, text=paragraph2, font=("godey", 15), justify="left", wraplength=1300, fg="grey")
paragraph_label2.pack(pady=20, anchor="w")

# Add a heading for the "Overview" paragraph
overview_heading = tk.Label(content_frame, text="Facial Recognition Algorithm:  ", font=("impact", 15), fg="grey", justify="left", wraplength=800)
overview_heading.pack(pady=20, anchor="w")  # Set anchor to "w" (west) to align it to the left
# Add paragraphs manually using label widgets
paragraph2 = " The system will use a facial recognition algorithm to recognize faces. The algorithm should be able to detect faces and extract facial features accurately."
paragraph_label2 = tk.Label(content_frame, text=paragraph2, font=("godey", 15), justify="left", wraplength=1300, fg="grey")
paragraph_label2.pack(pady=20, anchor="w")

# Add a heading for the "Overview" paragraph
overview_heading = tk.Label(content_frame, text="User Interface:  ", font=("impact", 15), fg="grey", justify="left", wraplength=800)
overview_heading.pack(pady=20, anchor="w")  # Set anchor to "w" (west) to align it to the left
# Add paragraphs manually using label widgets
paragraph2 = "  The system should have a user-friendly interface to capture images, display results, and generate reports."
paragraph_label2 = tk.Label(content_frame, text=paragraph2, font=("godey", 15), justify="left", wraplength=1300, fg="grey")
paragraph_label2.pack(pady=20, anchor="w")

# Add a heading for the "Overview" paragraph
overview_heading = tk.Label(content_frame, text=" Attendance Management: ", font=("impact", 15), fg="grey", justify="left", wraplength=800)
overview_heading.pack(pady=20, anchor="w")  # Set anchor to "w" (west) to align it to the left
# Add paragraphs manually using label widgets
paragraph2 = "The system should be able to manage attendance records for each person, including the date and time of attendance." 
paragraph_label2 = tk.Label(content_frame, text=paragraph2, font=("godey", 15), justify="left", wraplength=1300, fg="grey")
paragraph_label2.pack(pady=20, anchor="w")

# Add paragraphs manually using label widgets
paragraph2 = " Overall, the Smart Attendance System Using Face Recognition should be reliable, efficient, and easy to use. It should automate attendance-taking and provide accurate and timely attendance records"
paragraph_label2 = tk.Label(content_frame, text=paragraph2, font=("godey", 15), justify="left", wraplength=1300, fg="grey")
paragraph_label2.pack(pady=20, anchor="w")

# Add a heading for the "Overview" paragraph
overview_heading = tk.Label(content_frame, text="Building the Smart Attendance Management System Using Face Recognition", font=("impact", 30), fg="black", justify="left", wraplength=800)
overview_heading.pack(pady=20, anchor="w")  # Set anchor to "w" (west) to align it to the left

# Add paragraphs manually using label widgets
paragraph2 = "Here's a sample code for building the Smart Attendance Management System Using Face Recognition step by step:"
paragraph_label2 = tk.Label(content_frame, text=paragraph2, font=("godey", 15), justify="left", wraplength=1300, fg="grey")
paragraph_label2.pack(pady=20, anchor="w")

# Add a heading for the "Overview" paragraph
overview_heading = tk.Label(content_frame, text="Data Acquisition", font=("impact", 30), fg="black", justify="left", wraplength=800)
overview_heading.pack(pady=20, anchor="w")  # Set anchor to "w" (west) to align it to the left

# Add paragraphs manually using label widgets
paragraph2 = "In this section, we will cover the process of acquiring data for building a Smart Attendance Management System using Face Recognition.\nThis code captures an image using the webcam and displays it in a window."
paragraph_label2 = tk.Label(content_frame, text=paragraph2, font=("godey", 15), justify="left", wraplength=1300, fg="grey")
paragraph_label2.pack(pady=20, anchor="w")

# Load the image you want to add below the paragraph
image_below_paragraph = Image.open("3.png")
image_below_paragraph_photo = ImageTk.PhotoImage(image_below_paragraph)

# Create and add a label to display the image with a transparent background
image_below_paragraph_label = tk.Label(content_frame, image=image_below_paragraph_photo)
image_below_paragraph_label.image = image_below_paragraph_photo  # Keep a reference to the image
image_below_paragraph_label.pack(pady=20)

# Add a heading for the "Overview" paragraph
overview_heading = tk.Label(content_frame, text="Methodology", font=("impact", 30), fg="black", justify="left", wraplength=800)
overview_heading.pack(pady=20, anchor="w")  # Set anchor to "w" (west) to align it to the left

# Add paragraphs manually using label widgets
paragraph2 = "The overall method combines several computer vision and deep learning techniques to perform real-time face recognition and attendance marking. It uses OpenCV's face detection algorithm and a pre-trained deep learning model for face recognition. The attendance log is stored in database for easy access and manipulation. The code provides a user-friendly interface by displaying the video stream with the recognized names of individuals and a bounding box around their faces.The entire process is automated and requires minimal manual intervention. By using face recognition technology, the system can accurately recognize individuals and mark their attendance, reducing the chances of errors or malpractices. It is a reliable and efficient way of managing attendance in various settings."
paragraph_label2 = tk.Label(content_frame, text=paragraph2, font=("godey", 15), justify="left", wraplength=1300, fg="grey")
paragraph_label2.pack(pady=20, anchor="w")

# Add a heading for the "Overview" paragraph
overview_heading = tk.Label(content_frame, text="Algorithm", font=("impact", 30), fg="black", justify="left", wraplength=800)
overview_heading.pack(pady=20, anchor="w")  # Set anchor to "w" (west) to align it to the left

# Add paragraphs manually using label widgets
paragraph2 = "In the realm of face detection and recognition, K-Nearest Neighbors (KNN) emerges as a valuable tool. In the initial stage of face detection, KNN can assist in identifying potential faces within an image or video stream by comparing local features or image patches with known face patterns. Once potential faces are detected, KNN can be employed for face recognition. In this phase, KNN considers facial features or embeddings and leverages the 'nearest neighbors' concept. It measures the similarity between the facial characteristics of an individual and those in a reference dataset. The K nearest neighbors to the individual's features contribute to a collective decision regarding the person's identity. KNN's ability to adapt to different face variations and its simplicity make it a useful component in building face recognition systems. However, it's important to note that KNN may be combined with other techniques for improved accuracy and efficiency in complex face detection and recognition scenarios."
paragraph_label2 = tk.Label(content_frame, text=paragraph2, font=("godey", 15), justify="left", wraplength=1300, fg="grey")
paragraph_label2.pack(pady=20, anchor="w")
# Load the image you want to add below the paragraph
image_below_paragraph = Image.open("4.png")
image_below_paragraph_photo = ImageTk.PhotoImage(image_below_paragraph)

# Create and add a label to display the image with a transparent background
image_below_paragraph_label = tk.Label(content_frame, image=image_below_paragraph_photo)
image_below_paragraph_label.image = image_below_paragraph_photo  # Keep a reference to the image
image_below_paragraph_label.pack(pady=20)

# Add a heading for the "Overview" paragraph
overview_heading = tk.Label(content_frame, text="Image Acquisition", font=("impact", 30), fg="black", justify="left", wraplength=800)
overview_heading.pack(pady=20, anchor="w")  # Set anchor to "w" (west) to align it to the left

# Add paragraphs manually using label widgets
paragraph2 = "The first step is to acquire the images to recognize the faces. The below code represents the mechanism to perform this."
paragraph_label2 = tk.Label(content_frame, text=paragraph2, font=("godey", 15), justify="left", wraplength=1300, fg="grey")
paragraph_label2.pack(pady=20, anchor="w")
# Load the image you want to add below the paragraph
image_below_paragraph = Image.open("5.png")
image_below_paragraph_photo = ImageTk.PhotoImage(image_below_paragraph)

# Create and add a label to display the image with a transparent background
image_below_paragraph_label = tk.Label(content_frame, image=image_below_paragraph_photo)
image_below_paragraph_label.image = image_below_paragraph_photo  # Keep a reference to the image
image_below_paragraph_label.pack(pady=20)

# Add paragraphs manually using label widgets
paragraph2 = "This code captures multiple images using the webcam and stores them in a directory called dataset."
paragraph_label2 = tk.Label(content_frame, text=paragraph2, font=("godey", 15), justify="left", wraplength=1300, fg="grey")
paragraph_label2.pack(pady=20, anchor="w")

# Add a heading for the "Overview" paragraph
overview_heading = tk.Label(content_frame, text="Storing the Face Embeddings", font=("impact", 30), fg="black", justify="left", wraplength=800)
overview_heading.pack(pady=20, anchor="w")  # Set anchor to "w" (west) to align it to the left

# Add paragraphs manually using label widgets
paragraph2 = "In this section, we will focus on how to store the face embeddings generated by the face recognition model. Face embeddings are a compact numerical representation of a face that can be used to compare and recognize faces."
paragraph_label2 = tk.Label(content_frame, text=paragraph2, font=("godey", 15), justify="left", wraplength=1300, fg="grey")
paragraph_label2.pack(pady=20, anchor="w")
# Load the image you want to add below the paragraph
image_below_paragraph = Image.open("6.png")
image_below_paragraph_photo = ImageTk.PhotoImage(image_below_paragraph)

# Create and add a label to display the image with a transparent background
image_below_paragraph_label = tk.Label(content_frame, image=image_below_paragraph_photo)
image_below_paragraph_label.image = image_below_paragraph_photo  # Keep a reference to the image
image_below_paragraph_label.pack(pady=20)

# Add a heading for the "Overview" paragraph
overview_heading = tk.Label(content_frame, text="Attendance marking process ", font=("impact", 30), fg="black", justify="left", wraplength=800)
overview_heading.pack(pady=20, anchor="w")  # Set anchor to "w" (west) to align it to the left

# Add paragraphs manually using label widgets
paragraph2 = "The attendance marking process begins with capturing an individual's face, which is then processed using a pre-trained K-nearest neighbors (KNN) model. This model loads the encoded facial features to identify the individual, and if the recognition is successful, attendance is marked for that person. The attendance record includes the date and time, ensuring accurate tracking of attendance history. This automated process minimizes manual intervention and enhances the reliability and efficiency of attendance management."
paragraph_label2 = tk.Label(content_frame, text=paragraph2, font=("godey", 15), justify="left", wraplength=1300, fg="grey")
paragraph_label2.pack(pady=20, anchor="w")
# Load the image you want to add below the paragraph
image_below_paragraph = Image.open("6.png")
image_below_paragraph_photo = ImageTk.PhotoImage(image_below_paragraph)

# Create and add a label to display the image with a transparent background
image_below_paragraph_label = tk.Label(content_frame, image=image_below_paragraph_photo)
image_below_paragraph_label.image = image_below_paragraph_photo  # Keep a reference to the image
image_below_paragraph_label.pack(pady=20)

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
facebook_link_label.place(x=310, y=7310)

# Bind the click event to open the Facebook link
facebook_link_label.bind("<Button-1>", lambda event: open_youtube())

def open_instagram():
    webbrowser.open("https://www.instagram.com/attendancekeeper/")  # Replace with the desired Facebook URL

# Create a label with a colored background that represents the Facebook link
facebook_link_label = tk.Label(content_frame, text="https://www.instagram.com", fg="white", bg="#5a46a7", cursor="hand2")
facebook_link_label.place(x=560, y=7310)

# Bind the click event to open the Facebook link
facebook_link_label.bind("<Button-1>", lambda event: open_instagram())

def open_facebook():
    webbrowser.open("https://m.facebook.com/yoursmartstaff/videos/smartstaffs-facial-recognition-attendance-system/405974608049455/")  # Replace with the desired Facebook URL

# Create a label with a colored background that represents the Facebook link
facebook_link_label = tk.Label(content_frame, text="https://www.facebook.com", fg="white", bg="#5a46a7", cursor="hand2")
facebook_link_label.place(x=810, y=7310)

# Bind the click event to open the Facebook link
facebook_link_label.bind("<Button-1>", lambda event: open_facebook())

# Create a label with a colored background that represents the Facebook link
facebook_link_label = tk.Label(content_frame, text="03086633693\n03067148720", fg="white", bg="#5a46a7")
facebook_link_label.place(x=1050, y=7310)

# Create a label with a colored background that represents the Facebook link
facebook_link_label = tk.Label(content_frame, text="Contact Us", fg="white", bg="#5a46a7", font=("impact", 50))
facebook_link_label.place(x=50, y=7160)






# Make the window fullscreen
root.geometry("{0}x{0}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

root.update_idletasks()  # Update the window idle tasks to properly set the canvas size
canvas.config(scrollregion=canvas.bbox("all"))  # Set the scroll region based on the canvas content
# You can replace "your_color" with the color you want to use, e.g., "blue" or a hexadecimal color code.

root.mainloop()
