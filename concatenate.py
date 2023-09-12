# concatenate sdf compounds in a single folderinto a single sdf file (.sdf)

#script to concatenate sdf files in a single folder into a single sdf file
import os
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import SDWriter

def concatenate_sdf_files(input_folder, output_file):
    # Create a writer to the output file
    writer = SDWriter(output_file)

    # Iterate through all files in the input folder
    for root, _, files in os.walk(input_folder):
        for file_name in files:
            file_path = os.path.join(root, file_name)

            # Check if the file is an SDF file
            if file_name.endswith(".sdf"):
                # Read the SDF file and write each molecule to the output file
                suppl = Chem.SDMolSupplier(file_path)
                for mol in suppl:
                    if mol is not None:
                        writer.write(mol)

    # Close the writer
    writer.close()

if __name__ == "__main__":
    # Replace 'input_folder' with the path to the folder containing your SDF files
    input_folder = "/mnt/lustre/users/aakinnuwesi/TB_Project/ligands"
    # Replace 'output_file.sdf' with the desired name of the output file
    output_file = "/mnt/lustre/users/aakinnuwesi/TB_Project/ligands.sdf"

    concatenate_sdf_files(input_folder, output_file)