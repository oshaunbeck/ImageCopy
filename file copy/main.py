import shutil
from pathlib import Path
import os
import image_mods
from progress.bar import IncrementalBar

# Welcome the user to the program and prompt them to select a target-drive from the list.

print("\nThis program will copy any images found on this computer to a target destination of your choosing.\n")

# target_path will prompt the user to choose from available drives. it will then return the path chosen by the user.

target_path = image_mods.retrieve_target()

selection = input(f"\nThe destination drive you have chosen is {target_path} is this correct? (yes/no)\n")

while selection == 'no':

    target_path = image_mods.retrieve_target()

    selection = input(f"\nThe destination drive you have chosen is {target_path} is this correct? (yes/no)\n")


while selection != 'yes' and selection != 'no':

    selection = input("\nPlease respond with 'yes' or 'no'.\n")

    if selection == 'yes':
        break

    else:
         while selection == 'no':

            target_path = image_mods.retrieve_target()

            selection = input(f"\nThe destination drive you have chosen is {target_path} is this correct? (yes/no)\n")

# destination_path is the file pathway for the newly created "Copied Images" folder within the target_path.
destination_path = image_mods.create_folder(target_path=target_path)


# Find a home directory to begin the search from.
#home = str(Path.home())

directory = "/Users/oceanbeck/Desktop/PROJECTS"

image_path_list = image_mods.retrieve_image_paths(directory=directory)

bar = IncrementalBar("Copying Images", max = len(image_path_list))

input(f"\n{len(image_path_list)} images have been found! would you like to copy these over? (enter to continue)")

for image in image_path_list:

    shutil.copy2(src=image, dst=destination_path)
    bar.next()

bar.finish()

print(f"Successfully copied all images found within the directory {directory} into the target directory {destination_path}")