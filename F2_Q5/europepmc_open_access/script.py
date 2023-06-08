import os
import re
from xml.dom import minidom

# Define the folder path containing the XML files and the regex pattern
folder_path = '.'
pattern = r'([OPQ][0-9][A-Z0-9]{3}\d)'

# Loop through each file in the folder
for file_name in os.listdir(folder_path):
    if file_name.endswith('.xml'):  # Check if the file is an XML file
        file_path = os.path.join(folder_path, file_name)
        xml_doc = minidom.parse(file_path)  # Parse the XML file using minidom
        text = xml_doc.article.body
        matches = re.findall(pattern, text)
        
        # Print the matches found in the file
        print(f'Matches found in {file_name}:')
        for match in matches:
            print(f"{file_name},{match}")