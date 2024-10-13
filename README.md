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