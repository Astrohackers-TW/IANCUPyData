'''
example of DSS URL
https://archive.stsci.edu/cgi-bin/dss_search?
    v=poss2ukstu_red&   => type of data (poss2, red for instance)
    r=01%3A02%3A03.3&   => ra in hex decimal
    d=%2B00%3A01%3A02.2& => dec in hex decimal
    e=J2000&             => epoch (J2000 for instance)
    h=30&                => height of the image (30 arcmin)
    w=30&                => width of the image (30 arcmin)
    f=fits&              => types of the image (fits or gif)
    c=none&              => compress 
    s=on&                
    fov=NONE&
    v3=
'''

import requests as re
import shutil
urlroot='https://archive.stsci.edu/cgi-bin/dss_search?'
v='poss2ukstu_red'
e='J2000'
ra=str(1)+'%3A'+str(2)+'%3A'+str(03.3)
de='%2B'+str(0)+'%3A'+str(1)+'%3A'+str(02.2)
h=str(10)
w=str(10)
f='fits'
urlend='&c=none&s=on&fov=NONE&v3='
result = re.get(urlroot+'v='+v+'&r='+ra+'&d='+de+'&e='+e+'&h='+h+'&w='+w+'&f='+f+urlend,stream=True)

with open('img2.fits', 'wb') as out_file:
    shutil.copyfileobj(result.raw, out_file)
del result

