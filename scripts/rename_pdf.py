#!/usr/bin/env python3

#    This code is distributed WITHOUT ANY WARRANTY, without the implied
#   warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#   See the GNU Lesser General Public License for more details.
  
#   The license is distributed along with this repository or you can check
#   <http://www.gnu.org/licenses/> for more details.

# Contributors: 
# marcos-pereira (https://github.com/marcos-pereira)

import os
import sys

from pypdf import PdfReader
import crossref_commons.retrieval

def main():           
    print("\nScript:", sys.argv[0])    
    
    try:
        sys.argv[1]   
    except:
        raise RuntimeError("You did not specify any PDF file with name formatt my_file.pdf.\
            \nPlease run again with the file specified:\n rename_pdf.py my_file.pdf \nOR \npython3 rename_pdf.py my_file.pdf")
    
    print(f"PDF name: {sys.argv[1]}")      
    pdf_name = sys.argv[1]        
    
    rename_to_authoryear = False
    try: 
        sys.argv[2]
        print(f"Rename to authoryear.pdf format")       
        rename_to_authoryear = True
    except:
        pass    
    
    reader = PdfReader(pdf_name)
    
    # See what is there:
    # print(str(reader.metadata))
    
    # Rename file to authoryear.pdf format
    if rename_to_authoryear == True:
        if '/doi' not in reader.metadata:
            raise RuntimeError("PDF file does not have its doi in its metadata. You can try calling only:\n rename_pdf your_pdf.pdf \n OR \n python3 rename_pdf your_pdf.pdf\n to rename the PDF to its title.")
        
        # Get publication data
        publication_data = crossref_commons.retrieval.get_publication_as_json(reader.metadata['/doi']) 
        
        first_author_name = publication_data['author'][0]['family']
        publication_year = publication_data['published-print']['date-parts'][0][0]
        print(f"Publication first author name:\n {first_author_name}")   
        print(f"Publication year: {publication_year}")
        
        new_file_name = str(first_author_name) + str(publication_year)
        new_file_name += ".pdf"
    
    # Rename file to the title in its metadata
    else:
        if '/Title' not in reader.metadata:
            raise RuntimeError("Sorry, but your PDF metadata does not contain the paper title.")
        title = reader.metadata['/Title']
        
        if len(title) == 0:
            raise RuntimeError("The title in the PDF metadata is empty.")                            
        
        print(f"Current title: {title}")
        new_formatted_title = title.replace(" ", "_")
        new_formatted_title = new_formatted_title.replace(":", "")
        print(f"New formatted name: {new_formatted_title}")
        
        new_file_name = new_formatted_title + ".pdf"        
    
    os.rename(pdf_name, new_file_name)

if __name__ == '__main__':
    main()