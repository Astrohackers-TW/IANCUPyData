import os

data_dir = os.path.expanduser('~/astro_data')

if not os.path.exists(data_dir):
    os.mkdir(data_dir)
else:
    print('The directory "' + data_dir + '" already exists.')
