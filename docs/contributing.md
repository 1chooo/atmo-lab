# Plot Intro

## Example Code
```py
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np

# Set the latitudinal and longitudinal limits of the map.

minLat, maxLat =        # you should find the board
minLon, maxLon =        # you should find the board

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

parallels = np.arange()     # You should change the interval with the country
meridians = np.arange()     # You should change the interval with the country
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

plt.title('Map of your_country with Elevation Data', fontsize=20)

# Save the figure and display it.

plt.show()
```

以下是一些常见的colormap选项：

Sequential（顺序）colormap：适用于表示数据的连续变化，例如温度、海拔等。
- 'viridis'
- 'plasma'
- 'inferno'
- 'magma'
- 'cividis'

Diverging（发散）colormap：适用于表示数据的正负变化或对比，例如正负温度差异、正负差异等。
- 'coolwarm'
- 'bwr' (blue-white-red)
- 'RdBu' (red-blue)
  
Qualitative（定性）colormap：适用于表示离散的类别或标签，没有明显的顺序关系。
- 'tab10'
- 'Set1'
- 'Pastel1'
- 'Dark2'
  
Miscellaneous（其他）colormap：一些特殊的colormap选项。
- 'rainbow'
- 'jet'
- 'gray'

绘制州或省的边界：
```py
m.drawstates(color='k')
```
绘制河流：
```py
m.drawrivers(color='b', linewidth=0.5)
```
绘制湖泊：
```py
m.drawlakes(color='b')
绘制陆地/岛屿：
```
```py
m.fillcontinents(color='green', lake_color='blue')
```
绘制城市或地点：
```py
lats = [latitude1, latitude2, ...]
lons = [longitude1, longitude2, ...]
x, y = m(lons, lats)
m.plot(x, y, 'ro', markersize=5)
```

## Reference
[[Python] Basemap包排雷记录](https://blog.csdn.net/sinat_18665801/article/details/82356988)