from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='airefraction',
    version='0.1.0',
    description='Artificially intelligent refractive error correction',
    long_description=long_description,
    url='https://github.com/chleibig/airefraction',
    author='Christian Leibig',
    author_email='christian.leibig@uni-tuebingen.de',
    license=None,
    keywords='neural-networks machine-learning refraction',
    packages=find_packages('src', exclude=[]),
    package_dir={'': 'src'},  # tell packages are under src
    install_requires=[
        'keras',
        'tensorflow',
        'h5py',
        'numpy',
        'pandas',
        'xlrd',
        'openpyxl'
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
        'pytest-cov'
    ],
    include_package_data=True,
    entry_points={
        'console_scripts': ['ai-refraction=airefraction.cli:main']
    },
)
