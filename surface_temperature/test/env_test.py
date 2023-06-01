'''
Conda environment test
'''

from netCDF4 import Dataset
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from PIL import Image
import metpy.calc as mpcalc
from metpy.plots import add_metpy_logo, SkewT
from metpy.units import units
from metpy.calc import lcl , lfc
import pandas as pd
import cartopy