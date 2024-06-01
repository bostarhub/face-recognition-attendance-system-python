import os
import psutil

# Define the directory where your Python files are located
directory = r'C:\Users\Administrator\Favorites\Links\FaceRecognitionAttendance-master'

# Initialize variables to track success and errors
success = 0
errors = 0

# Iterate through all running processes
for process in psutil.process_iter(attrs=['pid', 'name', 'cmdline']):
    try:
        # Get process info
        process_info = process.info
        process_name = process_info['name']

        # Check if the process is a Python script
        if process_name == 'python.exe':
            cmdline = process_info['cmdline']
            if cmdline and any(directory in arg for arg in cmdline):
                # Terminate the process
                pid = process_info['pid']
                try:
                    os.kill(pid, 9)  # Use os.kill to forcefully terminate the process
                    success += 1
                except Exception as e:
                    errors += 1
    except Exception as e:
        errors += 1

# Print results
if errors > 0:
    print(f"Errors: {errors} Python processes could not be terminated.")
else:
    print("Success: All running Python processes in the directory have been terminated.")
