# Decoding Binary File - `decoding.py`

## Overview
`decoding.py` is a Python script that extracts **readable ASCII strings** from a binary file and writes them to a text file. It reads the content of the binary file (`file.bin`), identifies all printable ASCII strings of length 4 or more, and saves these strings in a new text file (`extracted_strings.txt`).

## Features
- Extracts human-readable strings from binary files.
- Filters out strings shorter than 4 characters.
- Saves extracted strings to a text file.
- Easy to modify and extend for further analysis of binary data.

## Requirements
- Python 3.x

No additional libraries or modules are required, as the script only uses Python's built-in `re` and `os` modules.

## Usage

### Step 1: Place your binary file (`file.bin`) in the same directory as `decoding.py`.

### Step 2: Run the script

To execute the script, open a terminal and run the following command:

```bash
python3 decoding.py

