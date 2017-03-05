import os
import requests as re
import shutil

# Create the download file directory.
data_dir = os.path.expanduser('~/astro_data/')
if not os.path.exists(data_dir):
    os.mkdir(data_dir)

# Download fits from web.
urlroot = 'https://archive.stsci.edu/cgi-bin/dss_search?'
v = 'poss2ukstu_red'
e = 'J2000'
ra = str(1) + '%3A' + str(2) + '%3A' + str(03.3)
de = '%2B' + str(0) + '%3A' + str(1) + '%3A' + str(02.2)
h = str(10)
w = str(10)
f = 'fits'
urlend = '&c=none&s=on&fov=NONE&v3='
result = re.get(urlroot+'v='+v+'&r='+ra+'&d='+de+'&e='+e+'&h='+h+'&w='+w+'&f='+f+urlend 
                , stream=True)

# Save result and delete tmp file.
with open(data_dir + 'img2.fits', 'wb') as out_file:
    shutil.copyfileobj(result.raw, out_file)
del result
