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
python3 rename_pdf.py <name_of_file>.pdf
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

# Common problems
The following problems can occurr depending on your PDF file metadata:
1. If your PDF file does not contain the `/doi` field in its metadata, it is not possible to use the authoryear option. If you try to use it, it should throw a runtime error explaining the problem.
2. If your PDF file does not contain the `/Title` field in its metadata, the `rename_pdf.py` script will not be able to rename your PDF file. If you try to rename it, it should throw a runtime error explaining the problem.
3. If your PDF file has the `/Title` field in its metadata, but it is empty (e.g. has zero length), the `rename_pdf.py` script will not be able to rename your PDF file. If you try to rename it, it should throw a runtime error explaining the problem.
4. If you run the `rename_pdf.py` script without any parameter, it will throw a runtime error explaining no PDF file was specified.
5. If you want to run the script from anywhere in your system and you have followed the instructions above, then run it using `rename_pdf.py <your_pdf>.pdf`. However, if you did not configured everything to run the scripts from anywhere, then you need to place your PDF file in the scripts folder and run `python3 rename_pdf.py <your_pdf>.pdf` inside the scripts folder.

# Did you have any trouble to install or use the `rename_pdf.py`? Please, submit an issue.
You are welcome to submit an issue to the repository explaining what did not work and the error messages you had. Do not hesitate to ask. Hopefully, we will find a solution to the problem.

# Would you like to contribute to the repository?
You are welcome to open a pull request with your contribution. 

