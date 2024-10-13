# rename-pdfs
This repository will contain a program to rename PDFs according to their metadata title.

# Install dependencies

1. Install pypdf:
```
pip install pypdf
```

# Usage

1. Go to the scripts folder and run the command:
```
cd scripts
python main <name_of_file>.pdf
```
It will rename the file to its "/Title" located in its metadata. The new name will have no spaces and underscores will be put in between words. Any ":" will be removed.

# Run the script from anywhere in the system
If you want to run the rename_pdf.py script from anywhere in your system without needing to change to the repository directory do the following:

1. Go to the scripts folder and change the file permissions to enable it to be executed:
```
cd scripts
chmod +x rename_pdf.py
```

2. Add the `rename_pdf.py` script to the path by exporting it to the path in the `.bashrc` file. First, go to the scripts folder and type `pwd` to get the path to the folder in your system:
```
cd scripts
pwd
```
It will print a path similar to:
```
/path_to_repo/rename_pdf/scripts
```

3. Open the `.bashrc` file with any text editor (e.g: `gedit ~/.bashrc`) and add the following line to it (note that you must use the output from the `pwd` command in step 2):
```
export PATH="${PATH}:/path_to_repo/rename_pdf/scripts"
```
Save the `.bashrc` file and close the terminal.

4. Open a new terminal and we are ready to go. Go to the folder of your PDF and type:
```
rename_pdf.py name_of_your_file.pdf
```
and it will be renamed to the title in the PDF metadata.
