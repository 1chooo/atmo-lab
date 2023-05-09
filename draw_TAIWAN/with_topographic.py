'''
@version: 1.0.0
@author: 1chooo
@date: 2023/05/07
@brief: Draw Taiwan

`with_color.py`
'''

import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np

minLat, maxLat = 21.75, 25.5
minLon, maxLon = 119.25, 122.5

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

m.bluemarble()
im = ax.imshow(np.zeros((4, 4)), cmap='Blues', vmin=0, vmax=1)

m.drawcoastlines(color='k')
m.drawcountries(color='k')

parallels = np.arange(21., 26.1, 1.)
m.drawparallels(
    parallels, 
    labels=[1, 0, 0, 0], 
    fontsize=14, 
    linewidth=0.5
)

meridians = np.arange(119., 123.1, 1.)
m.drawmeridians(
    meridians, 
    labels=[0, 0, 0, 1], 
    fontsize=14, 
    linewidth=0.5
)

plt.title('Taiwan')

# add colorbar
cb = plt.colorbar(im, fraction=0.046, pad=0.04)

# save and show
fig.savefig("./img/Taiwan_with_topographic.jpg", dpi=600)
plt.show()
