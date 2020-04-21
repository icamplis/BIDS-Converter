# BIDS-Converter

BIDS-Converter is a Python script used to convert a directory of .mat and .edf files into BIDS format.

## Installation

CLone or download this repository, and ensure all packages in requirements.txt are installed. This can be done by navigating to the directory containing requirements.txt in a terminal and entering:

```bash
pip3 install --user -r /path/requirements.txt
```

## Usage

Navigate to the directory containing BIDS_converter.py in a terminal and run the script.
```bash
python3 BIDS_converter.py
```

A prompt will appear asking for the path of the raw data directory.
```bash
Path name: 
```

Enter the path of the raw directory and return.
```bash
Path name: /Users/username/.../directory
```

A new file named 'BIDS' containing the new file structure will be created in the same directory as the raw directory, and the raw directory will remain unchanged. 
