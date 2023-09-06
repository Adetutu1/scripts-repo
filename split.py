#script to split thousands of compounds in single sdf file in a folder
import os
from rdkit import Chem
from rdkit.Chem import SDWriter

def is_sdf_file(filename):
    return filename.lower().endswith('.sdf')

def split_sdf(input_folder, output_folder):
    for sdf_file in os.listdir(input_folder):
        if not is_sdf_file(sdf_file):
            continue
        
        input_file_path = os.path.join(input_folder, sdf_file)
        try:
            suppl = Chem.SDMolSupplier(input_file_path)
        except Exception as e:
            print(f"Error processing {sdf_file}: {str(e)}")
            continue
        
        folder_name = os.path.splitext(sdf_file)[0]
        output_folder_path = os.path.join(output_folder, folder_name)
        os.makedirs(output_folder_path, exist_ok=True)
        
        for mol in suppl:
            if mol is not None:
                compound_id = mol.GetProp("_Name")
                output_file = os.path.join(output_folder_path, f"{compound_id}.sdf")
                writer = SDWriter(output_file)
                writer.write(mol)
                writer.close()

if __name__ == "__main__":
    input_directory = "/path/to/input/folder"    # Replace with the path to the input folder containing SDF files
    output_directory = "/path/to/output/folder"  # Replace with the path to the output folder where individual compounds will be saved
    
    split_sdf(input_directory, output_directory)
