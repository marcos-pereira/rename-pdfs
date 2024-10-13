# rename-pdfs
This repository will contain a program to rename PDFs according to their metadata title.

# Install dependencies

1. Install pypdf:
```
pip install pypdf
```

2. Install [crossref-commons](https://gitlab.com/crossref/crossref_commons_py/-/tree/master?ref_type=heads), if you wish to be able to rename your PDFs to authoryear format.
```
pip install crossref-commons
```
Beware that using crossref-commons to frequently may get you blocked from using the service. Check [this discussion](https://www.crossref.org/documentation/retrieve-metadata/rest-api/tips-for-using-the-crossref-rest-api/).

# Usage

1. Go to the scripts folder and run the command:
```
cd scripts
python3 rename_pdf <name_of_file>.pdf
```
It will rename the file to its "/Title" located in its metadata. The new name will have no spaces and underscores will be put in between words. Any ":" will be removed.

2. Alternatively, if your PDF metadata has its DOI, you may want to rename the PDF to authoryear format. Add a `true` after the pdf file name:
```
cd scripts
python3 rename_pdf.py <name_of_file>.pdf true
```
Beware that we use the crossref-commons API, which blocks users if the service is used too frequently.

# Run the script from anywhere in the system
If you want to run the rename_pdf.py script from anywhere in your system without needing to change to the repository directory do the following (see [the reference](https://www.reddit.com/r/linux4noobs/comments/i0172u/adding_python_scripts_to_path_variable_without/)):

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
