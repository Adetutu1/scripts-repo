# split large compounds in a folder into batches/junks of 10,000

import os
import shutil

def batch_group_files(folder_path, batch_size):
    # Create a batches folder outside the folder_path
    parent_folder = os.path.dirname(folder_path)
    batches_folder = os.path.join(parent_folder, "batches")
    os.makedirs(batches_folder, exist_ok=True)

    # Get a list of all files in the folder
    files = os.listdir(folder_path)
    num_files = len(files)

    # Calculate the number of batches required
    num_batches = num_files // batch_size
    if num_files % batch_size != 0:
        num_batches += 1

    # Create subfolders for each batch and move files into them
    for i in range(num_batches):
        batch_folder = os.path.join(batches_folder, f"batch_{i+1}")
        os.makedirs(batch_folder, exist_ok=True)

        # Calculate the start and end indices of the current batch
        start_index = i * batch_size
        end_index = min(start_index + batch_size, num_files)

        # Move files into the current batch folder
        for j in range(start_index, end_index):
            file_name = files[j]
            file_path = os.path.join(folder_path, file_name)
            shutil.move(file_path, batch_folder)
            print(f"Moved file '{file_name}' to '{batch_folder}'.")
	        
batch_group_files("/path/to/file/directory", 10000)

