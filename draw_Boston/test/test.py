import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np

minLat, maxLat = 40.5, 42.5
minLon, maxLon = -71.25, -69.75

fig = plt.figure(figsize=(8, 8))
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

m = Basemap(
    projection='cyl',
    resolution='h',
    llcrnrlat=minLat,
    urcrnrlat=maxLat,
    llcrnrlon=minLon,
    urcrnrlon=maxLon,
    ax=ax
)

m.drawcoastlines(color='k')
m.drawcountries(color='k')

parallels = np.arange(40., 43.1, 1.)
m.drawparallels(
    parallels,
    labels=[1, 0, 0, 0],
    fontsize=14,
    linewidth=0.5
)

meridians = np.arange(-71.5, -69.6, 1.)
m.drawmeridians(
    meridians,
    labels=[0, 0, 0, 1],
    fontsize=14,
    linewidth=0.5
)

plt.title('Boston, USA')
fig.savefig("../img/Boston_test.jpg", dpi=600)

plt.show()
