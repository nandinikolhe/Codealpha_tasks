import os  # Import the os module to interact with the operating system (e.g., file and folder management)
import shutil  # Import the shutil module to move files

# Define the directory to organize
directory = '/path/to/your/folder'  # Specify the path of the folder where files need to be organized

# Create a dictionary mapping file extensions to folder names
file_types = {
    'images': ['jpg', 'jpeg', 'png', 'gif'],  # List of image file extensions
    'documents': ['pdf', 'docx', 'txt'],  # List of document file extensions
    'spreadsheets': ['xls', 'xlsx', 'csv'],  # List of spreadsheet file extensions
    'audio': ['mp3', 'wav'],  # List of audio file extensions
    'video': ['mp4', 'mkv', 'avi'],  # List of video file extensions
}

# Create folders if they don't exist
for folder in file_types.keys():  # Loop through the keys in the file_types dictionary (the folder names)
    folder_path = os.path.join(directory, folder)  # Construct the full path to the folder to create
    if not os.path.exists(folder_path):  # Check if the folder already exists
        os.makedirs(folder_path)  # Create the folder if it doesn't exist

# Move files into their respective folders
for filename in os.listdir(directory):  # Loop through each file in the directory
    file_extension = filename.split('.')[-1]  # Extract the file extension (e.g., 'jpg' from 'image.jpg')
    file_path = os.path.join(directory, filename)  # Get the full path of the file

    # Loop through each folder and its associated extensions
    for folder, extensions in file_types.items():  # Check which folder the file belongs to
        if file_extension.lower() in extensions:  # If the file extension matches one of the extensions for this folder
            # Move the file to the appropriate folder
            shutil.move(file_path, os.path.join(directory, folder, filename))
            print(f'Moved {filename} to {folder} folder')  # Print a message indicating the file was moved
            break  # Exit the loop once the file has been moved, so we don't check other folders