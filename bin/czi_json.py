''' czi_json.py
    Extract metadata from CZI file and write to JSON file
'''

import argparse
import json
from pathlib import Path
import xml.etree.ElementTree as ET
from aicsimageio import AICSImage
import xmltodict

def process_czi():
    """ Read metadata from a CZI file and write to .json file
        Keyword arguments:
          None
        Returns:
          None
    """
    img = AICSImage(ARG.FILE)
    mdata = img.metadata
    # CZI stored the metadata as XML. If you want it in XML, uncomment
    # the following two commands:
    # tree = ET.ElementTree(mdata)
    # tree.write(f"{Path(ARG.FILE).stem}.xml")
    # Convert to JSON and write file
    treestr = ET.tostring(mdata)
    ddict = xmltodict.parse(treestr)
    with open(f"{Path(ARG.FILE).stem}.json", "w", encoding='utf8') as json_file:
        json_file.write(json.dumps(ddict))

# -----------------------------------------------------------------------------

if __name__ == '__main__':
    PARSER = argparse.ArgumentParser(
        description="Extract metadata from CZI file")
    PARSER.add_argument('--file', dest='FILE', action='store',
                        required=True, help='CZI file')
ARG = PARSER.parse_args()
process_czi()
