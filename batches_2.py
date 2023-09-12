# split large compounds in a single sdf file into batches/junks of 500,000

import os
from rdkit import Chem
from rdkit.Chem import SDWriter

def batch_group_file(input_file, batch_size):
    # Create a batches folder in the same directory as the input file
    input_file_directory = os.path.dirname(input_file)
    batches_folder = os.path.join(input_file_directory, "batches")
    os.makedirs(batches_folder, exist_ok=True)

    # Open the input SDF file
    suppl = Chem.SDMolSupplier(input_file)

    # Initialize batch and file counters
    batch_count = 0
    compounds_in_batch = 0

    # Iterate through the molecules in the input SDF file
    for mol in suppl:
        if mol is not None:
            # Create a new batch if needed
            if compounds_in_batch == 0:
                batch_count += 1
                batch_filename = os.path.join(batches_folder, f"batch_{batch_count}.sdf")
                sdf_writer = SDWriter(batch_filename)

            # Write the molecule to the current batch
            sdf_writer.write(mol)
            compounds_in_batch += 1

            # Check if the current batch has reached the specified size
            if compounds_in_batch == batch_size:
                sdf_writer.close()
                compounds_in_batch = 0

    print(f"Splitting complete. {batch_count} batch(es) created.")

# Example usage:
batch_group_file("/path/to/input/file.sdf", 500000)
