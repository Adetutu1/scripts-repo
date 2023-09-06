#To unzip zip folders from the unpacked single raw ZINC files
#For example, CAAARN.xaa.sdf.gz or CAAARN.xaa.pdbqt.gz
#into CAAARN.xaa.sdf or CAAARN.xaa.pdbqt

import os
import gzip

def unpack_gz(source_dir, destination_dir):
    if not os.path.exists(destination_dir):
        os.mkdir(destination_dir)
    extensions_to_extract = [".gz"]
    for root, directories, files in os.walk(source_dir):
        for file in files:
            file_path = root + '/' + file
            for extension in extensions_to_extract:
                if file.endswith(extension):
                    with gzip.open(file_path, 'rb') as f_in:
                        loc=(destination_dir+"/"+file).replace(".gz","")
                        try:
                            with open(loc,"wb") as f_out:
                                try:
                                    f_out.write(f_in.read())
                                    print("Extracting file from ",file_path," to ",loc)
                                except:
                                    print("Error extracting ",file_path)
                        except:
                            print("Error extracting ",file_path)

unpack_gz("/path/to/zip/folder", "/path/to/output/folder")
