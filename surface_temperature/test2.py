'''
@version: 1.0.0
@date: 2023/05/09
@brief: This script generates a time-lapse GIF of global surface temperature for the year 2021.

test2.py
'''

from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from PIL import Image

# Set up the Basemap instance
mp = Basemap(projection='mill', llcrnrlon=0., llcrnrlat=-90., urcrnrlon=360., urcrnrlat=90., resolution='c')

# Read in the data
with Dataset('./data/air.sfc.2021.nc') as data:
    lats, lons, time = data.variables['lat'][:], data.variables['lon'][:], data.variables['time'][:]
    temp = data.variables['air'][:]

# Loop through all days and create image frames
for day in range(169):
    fig, ax = plt.subplots(figsize=(12, 9))
    c_scheme = mp.pcolor(*mp(lons, lats), np.squeeze(temp[day, :, :]), cmap='jet')
    mp.drawcoastlines()
    mp.drawstates()
    mp.drawcountries()
    cbar = mp.colorbar(c_scheme, location='bottom', pad='10%')
    ax.set_title('Global Surface Temperature (K) Day {} of 2021'.format(day+1))
    plt.clim(200., 310.)
    fig.savefig('./imgs/jpg/{}.jpg'.format(day+1), dpi=680)
    plt.close()

# Create animated GIF
image_frames = [Image.open('./imgs/jpg/{}.jpg'.format(day+1)) for day in range(169)]
image_frames[0].save('./imgs/gif/temperature_timelapse.gif', format='gif', append_images=image_frames[1:], save_all=True, duration=150, loop=0)
