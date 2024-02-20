# easi-fish-np-backend [![Picture](https://raw.github.com/janelia-flyem/janelia-flyem.github.com/master/images/HHMI_Janelia_Color_Alternate_180x40.png)](http://www.janelia.org)

[![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)](https://www.python.org/)

## EASI-FISH NP backend processing

Backend processing for EASI-FISH NP

## Setup instructions:
   python -m venv venv
   source venv/bin/activate
   pip install --upgrade pip
   pip install -r requirements.txt

## Run the program
   python3.10 czi_json.py --file my_file.czi

The file *my_file.json* will be created
