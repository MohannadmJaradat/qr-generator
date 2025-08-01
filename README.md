# QR Code Generator

A simple Python script that generates QR codes from URLs or text input.

## Description

This script creates QR codes using the `pyqrcode` library and displays them using the PIL (Python Imaging Library). The generated QR code is saved as a PNG file and automatically opened for viewing.

## Requirements

- Python 3.x
- Required packages:
  - pillow
  - pypng
  - pyqrcode

## Installation

1. Clone this repository or download the files
2. Install the required packages:
```sh
pip install -r requirements.txt
```

## Usage

1. Run the script:
```sh
python qr-generator.py
```
2. Enter the URL or text when prompted
3. The QR code will be generated as 'qr_code.png' and displayed automatically

## Output

The script generates a QR code image file named `qr_code.png` in the same directory.

## License

Feel free to use and modify this
