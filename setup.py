from setuptools import setup, find_packages
import os

data_dir = os.path.expanduser('~/astro_data')

if not os.path.exists(data_dir):
    os.mkdir(data_dir)
else:
    print('The directory "' + data_dir + '" already exists.')

## codes for data exportation
from astroquery.vizier import Vizier
import astropy.units as u
from astropy.io import fits
import requests as re

##

NAME = 'iancupy_data'
# VERSION should be PEP440 compatible (https://www.python.org/dev/peps/pep-0440/)
VERSION = '0.0.dev1'

setup(name=NAME,
      version=VERSION,
      description='Data preparation for IANCU Python exercise',
      install_requires=['astropy', 'astroquery'],
      author='Cheng-Chung Chen, PoShih Chiang, Yi-Hao Su',
      author_email='yhsu@astro.ncu.edu.tw',
      license='MIT',
      packages=find_packages(),
      url='https://github.com/Astrohackers-TW/IANCUPyData.git',
      long_description='',
      zip_safe=False,
)
