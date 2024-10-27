import os

def list_files_in_directory(directory):
    total_files = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith('py'):
                print(os.path.join('', filename))
                total_files += 1
    
    print(total_files)

# Call the function with the current working directory
current_directory = os.getcwd()  # Gets the current working directory
list_files_in_directory(current_directory)
