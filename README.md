# Lomographic Filter

This project applies a lomography filter to an inputted picture, and saves the output as a new file. 

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)

## Installation

### Prerequisites
To run the project, you'll need the following:

- Python 3.9 or higher

Required libraries:
- `opencv-python~=4.10.0.84`
- `numpy~=2.1.0`

Additionally, the `argparse` library is used to handle command-line arguments, which is part of the Python standard library.

### Installing

To install and set up the project:
```bash
git clone https://github.com/patrick-jennewein/CMPSCI_5420_Project5
cd CS5420-Project-5
pip install -r requirements.txt
```

## Usage
The program can be run using the following command:

```
python main.py [-h] IMAGE
```
### Arguments
Positional Arguments:
* IMAGE (required): Path to the input image file. 

Optional Arguments:
* -h : Show help message and exit.

### Example Usage:
```
python main.py my_image.jpg
```
This command will process the input image `my_image.jpg`,