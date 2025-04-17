import xml.etree.ElementTree as ET

from .startup import *  # Imports the pre-processed command-line arguments
from .filter import Filter

class Convert(Filter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def convert_hydrogen_pattern(self, old_file, new_file="output.h2pattern", drumkit_name="GMRockKit", author="hydrogen", license_text="undefined license"):
        # Parse old XML
        tree = ET.parse(old_file)
        old_root = tree.getroot()
    
        # Build new XML structure
        ET.register_namespace('', "http://www.hydrogen-music.org/drumkit_pattern")
        ET.register_namespace('xsi', "http://www.w3.org/2001/XMLSchema-instance")
        new_root = ET.Element(
            "{http://www.hydrogen-music.org/drumkit_pattern}drumkit_pattern",
        )
    
        ET.SubElement(new_root, "drumkit_name").text = drumkit_name
        ET.SubElement(new_root, "author").text = author
        ET.SubElement(new_root, "license").text = license_text
    
        # Copy pattern data
        pattern_elem = ET.SubElement(new_root, "pattern")
        pattern_elem.append(old_root.find("name") or ET.Element("name"))
        pattern_elem.append(old_root.find("info") or ET.Element("info"))
        
        category_elem = ET.Element("category")
        category_elem.text = "not_categorized"
        pattern_elem.append(category_elem)
    
        pattern_elem.append(old_root.find("size") or ET.Element("size"))
        
        denominator_elem = ET.Element("denominator")
        denominator_elem.text = "4"
        pattern_elem.append(denominator_elem)
    
        note_list = old_root.find("noteList")
        if note_list is not None:
            pattern_elem.append(note_list)
        else:
            pattern_elem.append(ET.Element("noteList"))
    
        # Write new XML to file
        tree = ET.ElementTree(new_root)
        tree.write(new_file, encoding="UTF-8", xml_declaration=True)
    
        print(f"Converted: {old_file} -> {new_file}")

    def process(self, s):
        self.convert_hydrogen_pattern(s)
        
# Example usage:
# convert_hydrogen_pattern("old_pattern.h2pattern", "converted_pattern.h2pattern")
