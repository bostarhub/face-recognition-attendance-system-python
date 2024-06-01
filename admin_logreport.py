import tkinter as tk
import sqlite3
from tkinter import ttk
from datetime import datetime
from tkinter import messagebox

# Function to retrieve the total count of employees
def get_total_employee_count():
    conn = sqlite3.connect('employee_data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM employee_record")
    count = cursor.fetchone()[0]
    conn.close()
    return count

# Function to get attendance data for a specific date
def get_attendance_for_date(date_str):
    try:
        conn = sqlite3.connect('attendance_record.db')
        cursor = conn.cursor()
        cursor.execute(f"SELECT id, employee_id, first_name, in_time, out_time, date FROM {date_str}")
        data = cursor.fetchall()
        conn.close()
        return data
    except sqlite3.OperationalError:
        return None

# Function to get attendance data for an entire month
def get_attendance_for_month(year, month):
    data = []
    conn = sqlite3.connect('attendance_record.db')
    cursor = conn.cursor()
    for day in range(1, 32):
        date_str = f'attendance_record_{year}_{month:02d}_{day:02d}'
        try:
            cursor.execute(f"SELECT id, employee_id, first_name, in_time, out_time, date FROM {date_str}")
            data += cursor.fetchall()
        except sqlite3.OperationalError:
            continue
    conn.close()
    return data

# Function to get attendance data for an entire year
def get_attendance_for_year(year):
    data = []
    conn = sqlite3.connect('attendance_record.db')
    cursor = conn.cursor()
    for month in range(1, 13):
        try:
            data += get_attendance_for_month(year, month)
        except sqlite3.OperationalError:
            continue
    conn.close()
    return data

# Function to handle showing daily attendance
def show_daily_attendance():
    current_date_str = datetime.now().strftime('attendance_record_%Y_%m_%d')
    data = get_attendance_for_date(current_date_str)
    if data is not None:
        display_attendance_data(data)
    else:
        messagebox.showerror("Error", f"No data available for {current_date_str}.")

# Function to handle showing monthly attendance
def show_monthly_attendance():
    current_date = datetime.now()
    data = get_attendance_for_month(current_date.year, current_date.month)
    if data:
        display_attendance_data(data)
        update_table(data)
    else:
        messagebox.showerror("Error", f"No data available for the current month.")

# Function to handle showing yearly attendance
def show_yearly_attendance():
    current_date = datetime.now()
    data = get_attendance_for_year(current_date.year)
    if data:
        display_attendance_data(data)
        update_table(data)
    else:
        messagebox.showerror("Error", f"No data available for the entire year.")

# Function to update the table with new data
def update_table(data):
    tree.delete(*tree.get_children())  # Clear existing table data
    for row in data:
        tree.insert('', 'end', values=row)

# Function to display attendance data in the table
def display_attendance_data(data):
    tree.delete(*tree.get_children())  # Clear existing table data
    if data:
        for row in data:
            tree.insert('', 'end', values=row)
    else:
        messagebox.showinfo("Attendance Report", "No data available for the selected period.")

# Create the main window
root = tk.Tk()
root.title("View Attendance Report")
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

# Create a navigation bar with an increased height
navbar = tk.Frame(root, bg='#5a46a7', height=120)
navbar.pack(fill=tk.X)

# Calculate the total employee count
total_employee_count = get_total_employee_count()

# Create a label to display the total employee count
employee_count_label = tk.Label(navbar, text=f"Total Employees: {total_employee_count}", fg='white', bg='#5a46a7', font=("impact", 50))
employee_count_label.place(x=0, y=20)

# Function to change the text color on hover
def on_enter(event):
    event.widget.config(fg='red')

# Function to reset the text color after hover
def on_leave(event):
    event.widget.config(fg='white')

# Create a custom style for the treeview column headings
style = ttk.Style()
style.configure("Custom.Treeview.Heading", font=("impact", 20))

# Create the table for displaying data and place it to fill the entire window
tree = ttk.Treeview(root, columns=("ID", "Employee ID", "Name", "In Time", "Out Time", "Date"), show="headings", style="Custom.Treeview")

# Apply the custom style to the text below the column headings
for col in ("ID", "Employee ID", "Name", "In Time", "Out Time", "Date"):
    tree.column(col, anchor="w", width=100)
    tree.heading(col, text=col, anchor="w")

# Function to update the table with new data
def update_table(data):
    tree.delete(*tree.get_children())  # Clear existing table data
    for row in data:
        tree.insert('', 'end', values=row)

# Function to display attendance data in the table
def display_attendance_data(data):
    tree.delete(*tree.get_children())  # Clear existing table data
    if data:
        for row in data:
            tree.insert('', 'end', values=row)
        tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)  # Fill and expand the table to the window
    else:
        messagebox.showinfo("Attendance Report", "No data available for the selected period.")

# Function to handle showing daily attendance
def show_daily_attendance():
    current_date_str = datetime.now().strftime('attendance_record_%Y_%m_%d')
    data = get_attendance_for_date(current_date_str)
    if data is not None:
        display_attendance_data(data)
    else:
        messagebox.showerror("Error", f"No data available for {current_date_str}.")

# Function to handle showing monthly attendance
def show_monthly_attendance():
    current_date = datetime.now()
    data = get_attendance_for_month(current_date.year, current_date.month)
    if data:
        update_table(data)
        display_attendance_data(data)
    else:
        messagebox.showerror("Error", f"No data available for the current month.")

# Function to handle showing yearly attendance
def show_yearly_attendance():
    current_date = datetime.now()
    data = get_attendance_for_year(current_date.year)
    if data:
        update_table(data)
        display_attendance_data(data)
    else:
        messagebox.showerror("Error", f"No data available for the entire year.")

# Add clickable labels for "Daily", "Monthly", and "Yearly"
daily_label = tk.Label(root, text="Daily", fg='white', bg='#5a46a7', font=("impact", 20))
daily_label.place(x=1040, y=70)
daily_label.bind("<Enter>", on_enter)
daily_label.bind("<Leave>", on_leave)
daily_label.bind("<Button-1>", lambda event: show_daily_attendance())

monthly_label = tk.Label(root, text="Monthly", fg='white', bg='#5a46a7', font=("impact", 20))
monthly_label.place(x=1140, y=70)
monthly_label.bind("<Enter>", on_enter)
monthly_label.bind("<Leave>", on_leave)
monthly_label.bind("<Button-1>", lambda event: show_monthly_attendance())

yearly_label = tk.Label(root, text="Yearly", fg='white', bg='#5a46a7', font=("impact", 20))
yearly_label.place(x=1270, y=70)
yearly_label.bind("<Enter>", on_enter)
yearly_label.bind("<Leave>", on_leave)
yearly_label.bind("<Button-1>", lambda event: show_yearly_attendance())

# Start the main loop
root.mainloop()