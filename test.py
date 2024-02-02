import os
import time
from datetime import datetime, timedelta

def is_file_updated_within_last_n_minutes(file_path, n_minutes):
    """
    Check if the file at the specified path is updated within the last n minutes.
    """
    # Get the modification time of the file
    modification_time = datetime.fromtimestamp(os.path.getmtime(file_path))
    
    # Calculate the current time
    current_time = datetime.now()
    
    # Calculate the time difference
    time_difference = current_time - modification_time
    
    # Check if the file is updated within the last n minutes
    return time_difference <= timedelta(minutes=n_minutes)

def get_last_line(file_path):
    """
    Get the last line of the file at the specified path.
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()
        return lines[-1].strip() if lines else None

# File path
file_path = 'temp_log'

# Check if the file is updated within the last 3 minutes
if is_file_updated_within_last_n_minutes(file_path, 3):
    # Get the last line of the file
    last_line = get_last_line(file_path)
    
    # Check if the last line contains the pattern "success"
    if last_line and 'success' in last_line.lower():
        print("Pattern 'success' found in the last line of the file.")
    else:
        print("Pattern 'success' not found in the last line of the file.")
else:
    print("File is not updated within the last 3 minutes.")
