import os
import shutil
from pathlib import Path

def copy_desktop_icons():
    # Get the path to the desktop
    desktop_path = Path.home() / 'Desktop'

    # Get the path to the script
    script_path = Path(__file__).resolve().parent

    # Create a folder named 'icons' in the script directory
    icons_folder = script_path / 'icons'
    icons_folder.mkdir(exist_ok=True)

    # Variable to track if any icons were copied
    icons_copied = False

    # Iterate over the files on the desktop
    for file_name in os.listdir(desktop_path):
        # Get the full path to the file
        file_path = desktop_path / file_name

        # Check if it's a file (not a directory) and it's not the script itself
        if file_path.is_file() and file_path != script_path:
            # Copy the file to the icons folder
            shutil.copy2(file_path, icons_folder)
            icons_copied = True

    if icons_copied:
        print('Icons copied successfully.')
    else:
        print("Error: Couldn't find any desktop icons to copy.")
    
    input("Press enter to continue...")

if __name__ == '__main__':
    copy_desktop_icons()
