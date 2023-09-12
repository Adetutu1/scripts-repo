# Unpacking compounds from Zinc single file 

2 million compounds downloaded from ZINC database as a single file  ZINC-downloader-3D-sdf.gz.curl were unpacked using bash script.

Copy the downloaded ZINC-downloader-3D-sdf.gz.curl from the download directory to your preferred preferred directory or copy to the cluster to unpack the compounds.

create a bash script 'fetch.sh' file using nano on cluster or text editor in your loacal machine

chmod u+x the 'fetch.sh' file to be executable and then run the sh file.

If runing the job on the cluster you may run the script using pbs file.

# Unzip the fetched folders 

Once the file has been upacked unto their respective folders CA, CB, CC, CD,..., DA, DB,DC, DD,...EA, EB, EC, ED, ..., 

Each of these folder above contains subfolders AARN.xaa.sdf.gz, ABRN.xaa.sdf.gz ...

The subfolders will be unzip using python script 

Create a python script 'unzip.py' 

The python script will unzip the zip files in the subdirectory.

# Split the unzip files into individual zinc compounds

To split the unzip files into their individual zinc compounds is important so that each compounds would be identified using their 'ZINC ID'

Create a python script 'split.py' file 

# Merge the split zinc compounds

It would be best to merge all the zinc compounds in the different folders to a single folder for easy of accessibility while the compounds in the different folders still remain.

To do this, create a python script 'merge.py'

# Split the merge compounds in batches

The compounds in the single folder could be split into batches of 5000, 10000, 20000 depending on your preference.

To do this, create a python script 'batches.py' 


# Concatenate the compounds 

Incase you prefer to concatenate the merge compounds i.e compounds in the single folder rather than split the compounds into batches of 10,000. 

<<<<<<< HEAD
Concatenating the compounds into a single folder (e.g ligands.sdf) is easier to use for ligPrep in Maestro or for filtering based on physico-chemical properties or molecualar descriptors using scripts.gig
=======
Concatenating the compounds into a single folder (e.g ligands.sdf) is easier to use for ligPrep in Maestro or for filtering based on physico-chemical properties or molecualar descriptors using scripts.

create python script "concatenate.py"
>>>>>>> 1db7aafa6df9046468941a56020bf6a8c9a4e32d
