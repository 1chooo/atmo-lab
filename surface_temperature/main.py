'''
@version: 1.0.0
@date: 2023/05/09
@brief: This script generates a time-lapse GIF 
of global surface temperature for the year 2021.

main.py
'''

from netCDF4 import Dataset
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from PIL import Image

mpl.use('TKAgg')

# read in the data
data = Dataset('./data/air.sfc.2021.nc')
lats = data.variables['lat'][:]
lons = data.variables['lon'][:]
time = data.variables['time'][:]
temp = data.variables['air'][:]

# set up Basemap instance
mp = Basemap(
    projection='mill', 
    llcrnrlon=0., 
    llcrnrlat=-90., 
    urcrnrlon=360., 
    urcrnrlat=90., 
    resolution='c'
)
lon, lat = np.meshgrid(lons, lats)
x, y = mp(lon, lat)

# loop through all days and create image frames
for day in range(169):
    
    c_scheme = mp.pcolor(x, y, np.squeeze(temp[day, :, :]), cmap='jet')
    mp.drawcoastlines()
    mp.drawstates()
    mp.drawcountries()
    cbar = mp.colorbar(c_scheme, location='bottom', pad='10%')
    plt.title('Global Surface Temperature (K) Day {} of 2021'.format(day+1))
    plt.clim(200., 310.)
    fig = plt.gcf()
    fig.set_size_inches(12, 9)
    fig.savefig('./imgs/jpg/{}.jpg'.format(day+1), dpi=680)
    plt.close()

# create animated GIF
image_frames = [Image.open('./imgs/jpg/{}.jpg'.format(day+1)) for day in range(169)]
image_frames[0].save(
    './imgs/gif/temperature_timelapse.gif', 
    format='gif', 
    append_images=image_frames[1:], 
    save_all=True, 
    duration=150, 
    loop=0
)
