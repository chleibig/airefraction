# airefraction
Neural network based prescription of subjectively optimal refractive error corrections from Zernike coefficients.

## Quickstart

### Installation

A convenient way to get `airefraction` running in an isolated environment, that is without affecting your system's python installation (if you are familiar with Python just go ahead with step 3, optionally in a virtual environment) is as follows:
1. Get the [Anaconda Distribution](https://www.continuum.io/downloads) for **Python 3.6** and your operating system.
2. Optionally create a conda environment `<name>` with `pip` installed into it:
    ```
    conda create -n <name> pip
    ```
    Activate the environment by typing:
    ```
    source activate <name>
    ```
3. Install the `airefraction` package:
  ```
  pip install git+https://github.com/chleibig/airefraction.git
  ```
This will create a command line application `ai-refraction` that is accessible from anywhere, given that the environment from (2) is activated.

### Example usage

Usage is explained by calling `ai-refraction -h`:
```
usage: ai-refraction [-h] infile outfile

Compute refractive error corrections.

positional arguments:
  infile      Excel file with pupil diameters and Zernike coefficients. Each
              row describes one eye. The header must be as follows: ('pd',
              'Z00', 'Z1-1', 'Z11', 'Z2-2', 'Z20', 'Z22', 'Z3-3', 'Z3-1',
              'Z31', 'Z33', 'Z4-4', 'Z4-2', 'Z40', 'Z42', 'Z44', 'Z5-5',
              'Z5-3', 'Z5-1', 'Z51', 'Z53', 'Z55', 'Z6-6', 'Z6-4', 'Z6-2',
              'Z60', 'Z62', 'Z64', 'Z66', 'Z7-7', 'Z7-5', 'Z7-3', 'Z7-1',
              'Z71', 'Z73', 'Z75', 'Z77')
  outfile     For saving the refractive error corrections.

optional arguments:
  -h, --help  show this help message and exit
```

Hence if your features are stored in `pd_and_zernike.xlsx` you could compute and save the corrections to `corrections.xlsx`:

```
ai-refraction pd_and_zernike.xlsx corrections.xlsx
```

### Testing

To check that everything works correctly on your system you can as well clone the repository:
```
git clone https://github.com/chleibig/airefraction.git
```
Go to the folder `airefraction` that contains the setup.py file and install the package via: 
```
pip install .
```
And run the tests:
```
python setup.py test
```
