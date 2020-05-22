# BIDS-Converter

BIDS-Converter is a Python script used to convert a directory of Eyelink .mat and .edf files into BIDS format.

## Installation

Clone or download this repository, and ensure all packages in requirements.txt are installed. This can be done by navigating to the directory containing requirements.txt in a terminal and entering:
```bash
pip3 install --user -r /path/requirements.txt
```

Download the **EyeLink Developers Kit for Mac OS X** from [here](https://www.sr-support.com/forum/downloads/eyelink-display-software/45-eyelink-developers-kit-for-mac-os-x-mac-os-x-display-software?15-EyeLink-Developers-Kit-for-Mac-OS-X=).


## Usage

Navigate to the directory containing BIDS_converter.py in a terminal and run the script.
```bash
python3 BIDS_converter.py
```

A prompt will appear asking for the path of the data directory.
```bash
Path name: 
```

Enter the path of the directory and return.
```bash
Path name: /Users/username/.../directory
```

A new file named 'BIDS' containing the new file structure will be created on the same level as the original directory, and this original directory will be unchanged. 
