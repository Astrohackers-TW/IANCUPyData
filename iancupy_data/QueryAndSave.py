from astroquery.vizier import Vizier
import astropy.units as u
from astropy.io import fits

#query setup
Vizier.ROW_LIMIT = -1
target='M4'
r=0.4

#making query
tmc = Vizier.query_region(target, radius=r*u.deg, catalog='II/246/out') #2MASS catalog
ppmxl = Vizier.query_region(target, radius=r*u.deg, catalog='I/317/sample') # PPMXL proper motion

#get catalog only
jhk = tmc[0]
pm=ppmxl[0]

# retrive data only from 2MASS columns [3,4,9,11,13,15,17,19,21]
col1 = fits.Column(name=jhk.colnames[3], format=jhk.dtype[3], array=jhk[jhk.colnames[3]])
col2 = fits.Column(name=jhk.colnames[4], format=jhk.dtype[4], array=jhk[jhk.colnames[4]])
col3 = fits.Column(name=jhk.colnames[9], format=jhk.dtype[9], array=jhk[jhk.colnames[9]])
col4 = fits.Column(name=jhk.colnames[11], format=jhk.dtype[11], array=jhk[jhk.colnames[11]])
col5 = fits.Column(name=jhk.colnames[13], format=jhk.dtype[13], array=jhk[jhk.colnames[13]])
col6 = fits.Column(name=jhk.colnames[15], format=jhk.dtype[15], array=jhk[jhk.colnames[15]])
col7 = fits.Column(name=jhk.colnames[17], format=jhk.dtype[17], array=jhk[jhk.colnames[17]])
col8 = fits.Column(name=jhk.colnames[19], format=jhk.dtype[19], array=jhk[jhk.colnames[19]])
#col9 = fits.Column(name=jhk.colnames[21], format=jhk.dtype[21], array=jhk[jhk.colnames[21]])

cols = fits.ColDefs([col1, col2, col3, col4, col5, col6, col7, col8])#, col9])
tmc_hdu = fits.BinTableHDU.from_columns(cols)

tmc_hdu.writeto('~/astro_data/'+target+'_tmc.fits')
