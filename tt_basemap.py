import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

m = Basemap(projection="mill")
m.drawcoastlines()
fig = plt.gcf()
plt.show()
fig.savefig("tt3",dpi=300)