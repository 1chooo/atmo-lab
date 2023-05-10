'''
@version: 1.0.0
@date: 2023/05/09
@brief: 

test.py
'''


from netCDF4 import Dataset
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from PIL import Image

mpl.use('TKAgg')

#read in the data
data = Dataset(r'./data/air.sfc.2021.nc')
print(data.variables)
print(data.variables.keys())

lats = data.variables['lat'][:]
lons = data.variables['lon'][:]
time = data.variables['time'][:]
print(lats)
print(lons)
print(time)


temp = data.variables['air'][:]
fig = plt.figure(figsize=(12, 9))
mp = Basemap(
    projection='mill',
    llcrnrlon = 0., 
    llcrnrlat = -90., 
    urcrnrlon = 360., 
    urcrnrlat = 90.,
    resolution = 'c'
)
lon, lat = np.meshgrid(lons, lats)
x, y =mp(lon, lat)
days = np.arange(0, 169)
print(days)
day = 0

for i in days:
    
    c_scheme = mp.pcolor(x, y, np.squeeze(temp[i, :, :]), cmap = 'jet')
    mp.drawcoastlines()
    mp.drawstates()
    mp.drawcountries()
    cbar = mp.colorbar(c_scheme, location='bottom', pad = '10%')
    day += 1
    plt.title('Global Surface Temperature (K) ' + 'Day' + str(day) + 'of 2021')
    plt.clim(200., 310.)

    # plt.show()
    #fig.savefig('global_surface_temperature', dpi = 680)
    fig.savefig(r'./imgs/jpg/' + str(day)+ '.jpg')

image_frames = []

days = np.arange(1,169)

for k in days:
    new_frame = Image.open(r'./imgs/jpg/' + str(k) + '.jpg')
    image_frames.append(new_frame)

image_frames[0].save(
    './imgs/gif/temperature_timelapse.gif', 
    format = 'gif',
    append_images = image_frames[1:],
    save_all = True, 
    duration = 150,
    loop = 0
)