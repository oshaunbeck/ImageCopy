import psutil as ps
import os
import platform

# check_os is to identify Mac (return true) or something else probs windows (return false)

def mac_os():

    operating_system = platform.platform()

    if "macOS" in operating_system:

        return True

    return False


def retrieve_target():
    # Create a list of potential drives to choose from.

    if mac_os():

        drives = os.listdir("/Volumes")

    else:

        drives = [partition.mountpoint for partition in ps.disk_partitions()]

    num_of_drives = len(drives)

    print(f"{num_of_drives} drives have been found!\n")

    print("LIST OF AVAILABLE DRIVES:\n")

    # Print items in the drive list so the user knows which drives are available to choose from.

    #                               NOTE: 
    # I tried to use the enumerate function but it was changing the list 
    # to contain only its last element, not sure why. Have to use this gross index variable

    index = 1

    for drive in drives:
        print(index, drive)
        index += 1

    print(f"\nPlease select a target destination where the images will be copied to. (a number between 1 and {num_of_drives})\n")


    # Receive user input

    target = input()


    # Check to see if the user has inputted a digit, else tell user to input a digit

    while not target.isdigit():

        target = input(f"\nInput a whole-number between 1 and {num_of_drives} please!\n")


    # Once the user enters a valid digit, they are allowed to break out of this loop.
    # The target variable may now exist as an integer.

    target = int(target) - 1


    # The next thing to check is the size of the input.
    # Input CANNOT be less than 1 or more than the length of the list of available drives.

    while (target < 0 or target > num_of_drives - 1):

            target = input(f"\nThe number you have selected is not between 1 and {num_of_drives}.\n\n" +
            f"Please select a number between 1 and {num_of_drives}.\n")

            if not target.isdigit():

                while not target.isdigit():

                    target = input(f"\nInput a whole-number digit between 1 and {num_of_drives} please!\n")

                target = int(target) - 1

            else:
                target = int(target) - 1

    return os.path.join("/Volumes", drives[target])

def create_folder(target_path):
    
    name = "Copied Images"

    path = os.path.join(target_path, name)

    print("trying to create" + path)

    try:

        os.mkdir(path)
        print(f"Successfully created 'Copied Images folder in {target_path}")
    
    except Exception as e:
        print("Couldnt create folder for images to be copied into.")
        print(e)

    return path

def retrieve_image_paths(directory):

    accepted_extensions = ['.jpg', '.png']

    image_path_list = []

    for subdir, dirs, files in os.walk(directory):
        for file in files:

            for extension in accepted_extensions:
                if file.endswith(extension):

                    image_directory = os.path.join(subdir, file)

                    image_path_list.append(image_directory)

    return image_path_list