import os
import shutil
import requests as re
import astropy.units as u
from astropy.io import fits
from astroquery.vizier import Vizier


# Create the download file directory.
data_dir = os.path.expanduser('~/astro_data/')
if not os.path.exists(data_dir):
    os.mkdir(data_dir)


## Download digital sky survey fits.
urlroot = 'https://archive.stsci.edu/cgi-bin/dss_search?'
v = 'poss2ukstu_red'
e = 'J2000'
ra = str(1) + '%3A' + str(2) + '%3A' + str(03.3)
de = '%2B' + str(0) + '%3A' + str(1) + '%3A' + str(02.2)
h = str(10)
w = str(10)
f = 'fits'
urlend = '&c=none&s=on&fov=NONE&v3='
result = re.get(urlroot+'v='+v+'&r='+ra+'&d='+de+'&e='+e+'&h='+h+'&w='+w+'&f='+f+urlend, stream=True)

with open(data_dir + 'dss_image.fits', 'wb') as out_file:
    shutil.copyfileobj(result.raw, out_file)
del result


## Query on vizier and save to FITS bin table
# Query setup
Vizier.ROW_LIMIT = -1
target = 'NGC6121' # Another name: M4
r = 0.4

# Making query
# 2MASS catalog
tmc = Vizier.query_region(target, radius=r*u.deg, catalog='II/246/out') 
# PPMXL proper motion
ppmxl = Vizier.query_region(target, radius=r*u.deg, catalog='I/317/sample') 

# Get catalog only
jhk = tmc[0]
pm = ppmxl[0]

# Retrive data only from 2MASS columns [3,4,9,11,13,15,17,19,21]
col1 = fits.Column(name=jhk.colnames[3], format=jhk.dtype[3], array=jhk[jhk.colnames[3]])
col2 = fits.Column(name=jhk.colnames[4], format=jhk.dtype[4], array=jhk[jhk.colnames[4]])
col3 = fits.Column(name=jhk.colnames[9], format=jhk.dtype[9], array=jhk[jhk.colnames[9]])
col4 = fits.Column(name=jhk.colnames[11], format=jhk.dtype[11], array=jhk[jhk.colnames[11]])
col5 = fits.Column(name=jhk.colnames[13], format=jhk.dtype[13], array=jhk[jhk.colnames[13]])
col6 = fits.Column(name=jhk.colnames[15], format=jhk.dtype[15], array=jhk[jhk.colnames[15]])
col7 = fits.Column(name=jhk.colnames[17], format=jhk.dtype[17], array=jhk[jhk.colnames[17]])
col8 = fits.Column(name=jhk.colnames[19], format=jhk.dtype[19], array=jhk[jhk.colnames[19]])

cols = fits.ColDefs([col1, col2, col3, col4, col5, col6, col7, col8])
tmc_hdu = fits.BinTableHDU.from_columns(cols)
tmc_hdu.writeto(data_dir + '/' + target + '_tmc.fits')
