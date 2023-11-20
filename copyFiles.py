import os
import shutil

def copy_files(source_directory, destination_directory):
    """
    Copy all files from the source directory to the destination directory.
    
    Args:
        source_directory (str): The path to the source directory.
        destination_directory (str): The path to the destination directory.
        
    Returns:
        None
    """
    try:
        # Get a list of files in the source directory
        file_list = os.listdir(source_directory)

        # Iterate through the files and copy them to the destination directory
        for file_name in file_list:
            source_path = os.path.join(source_directory, file_name)
            destination_path = os.path.join(destination_directory, file_name)

            # Use shutil.copy() to copy the file
            shutil.copy(source_path, destination_path)

        print("Files copied successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    source_directory      = '/home/robsteele49/git/gmnSoftware/testSource'
    destination_directory = '/home/robsteele49/git/gmnSoftware/testDestination'
    
    # Call the copy_files function with the specified directories
    copy_files(source_directory, destination_directory)

if __name__ == "__main__":
    main()
