import os

def list_files_in_directory(directory):
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            print(os.path.join(dirpath, filename))

# Call the function with the current working directory
current_directory = os.getcwd()  # Gets the current working directory
list_files_in_directory(current_directory)
