import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np

# Set the latitudinal and longitudinal limits of the map for Boston.

minLat, maxLat = 40.5, 42.5
minLon, maxLon = -71.25, -69.75

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

parallels = np.arange(40.5, 42.6, 0.5)
meridians = np.arange(-71.25, -69.74, 0.5)
m.drawparallels(
    parallels, 
    labels=[1, 0, 0, 0], 
    fontsize=10, 
    linewidth=0.5
)
m.drawmeridians(
    meridians, 
    labels=[0, 0, 0, 1], 
    fontsize=10, 
    linewidth=0.5
)

# Set the title of the plot.

plt.title('Map of Boston with Elevation Data', fontsize=20)

# Set the labels for the x and y axes.

# plt.xlabel('Longitude', fontsize=12)
# plt.ylabel('Latitude', fontsize=12)

# Create a dummy image for the colorbar.

im = ax.imshow(np.zeros((4, 4)), cmap='Blues', vmin=0, vmax=1)

# Add a colorbar with the specified label and position.

colorbar = plt.colorbar(im, fraction=0.046, pad=0.04, label='Elevation (m)')

# Save the figure and display it.

fig.savefig("../img/Boston_test4.jpg", dpi=600)
plt.show()
