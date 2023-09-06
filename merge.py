#script to copy sdf files from several folders to a single folder

import os
import shutil

# Source folder containing subfolders with files
source_folder = "/mnt/c/MYRESE~1/split"

# Destination folder to copy all the files
destination_folder = "/mnt/c/MYRESE~1/dataset"

# Loop through each folder and copy files to the destination folder
for root, dirs, files in os.walk(source_folder):
    for file in files:
        source_file = os.path.join(root, file)
        destination_file = os.path.join(destination_folder, file)
        shutil.copy(source_file, destination_file)

print("File copying completed!")