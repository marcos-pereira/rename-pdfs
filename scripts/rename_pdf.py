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

def main():           
    print("\nScript:", sys.argv[0])
    print(f"PDF name: {sys.argv[1]}")         
    pdf_name = sys.argv[1]           
    
    reader = PdfReader(pdf_name)
        
    title = reader.metadata['/Title']
    # See what is there:
    # print(str(reader.metadata))
    
    print(f"Current title: {title}")
    new_formatted_title = title.replace(" ", "_")
    new_formatted_title = new_formatted_title.replace(":", "")
    print(f"New formatted name: {new_formatted_title}")
    
    new_file_name = new_formatted_title + ".pdf"        
    
    os.rename(pdf_name, new_file_name)

if __name__ == '__main__':
    main()