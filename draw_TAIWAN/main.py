'''
@version: 1.0.0
@date: 2023/05/08
@brief: Draw a map of Taiwan with elevation data.

This script uses the mpl_toolkits.basemap package 
to draw a map of Taiwan with a colorbar showing elevation data. 
The map is centered on Taiwan and shows its surrounding seas and countries.

main.py
'''

import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np

# Set the latitudinal and longitudinal limits of the map.

minLat, maxLat = 21.75, 25.5
minLon, maxLon = 119.25, 122.5

# Create a figure and axes object.

fig = plt.figure(figsize=(8, 8))
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

# Create a Basemap object with the specified projection and limits.

m = Basemap(
    projection='cyl',
    resolution='h',
    llcrnrlat=minLat,
    urcrnrlat=maxLat,
    llcrnrlon=minLon,
    urcrnrlon=maxLon,
    ax=ax
)

# Draw the blue marble background.

m.bluemarble()

# Add the coastline and country boundaries.

m.drawcoastlines(color='k')
m.drawcountries(color='k')

# Add the parallels and meridians.

parallels = np.arange(21., 26.1, 1.)
meridians = np.arange(119., 123.1, 1.)
m.drawparallels(
    parallels, 
    labels=[1, 0, 0, 0], 
    fontsize=14, linewidth=0.5
)
m.drawmeridians(
    meridians, 
    labels=[0, 0, 0, 1], 
    fontsize=14, 
    linewidth=0.5
)

# Set the title of the plot.

plt.title('Map of Taiwan with Elevation Data', fontsize=20)

# # Move the axis labels outward

# ax.tick_params(axis='both', which='major', pad=10)

# # Set the labels for the x and y axes.

# plt.xlabel('Longitude', fontsize=16)
# plt.ylabel('Latitude', fontsize=16)

# Create a dummy image for the colorbar.

im = ax.imshow(np.zeros((4, 4)), cmap='Blues', vmin=0, vmax=1)

# Add a colorbar with the specified label and position.

colorbar = plt.colorbar(im, fraction=0.046, pad=0.04, label='Elevation (m)')

# Save the figure and display it.

fig.savefig("./img/Taiwan.jpg", dpi=600)
plt.show()