# Plot Our Formasa

## Introduction

This project is a fun way to create a visual representation of Taiwan. The following steps outline how to replicate the project.

## Results

| No relief | With relief | Final Plot |
| :---: | :---: | :---: |
| ![](./img/Taiwan_no_topographic.jpg) | ![](./img/Taiwan_with_topographic.jpg) | ![](./img/Taiwan.jpg) |


<!-- | No relief | With relief |Final |
| :---: | :---: | :---: |
| <img src="./img/Taiwan_no_topographic.jpg" width="200"/> | <img src="./img/Taiwan_with_topographic.jpg" width="200"/> | <img src="./img/Taiwan.jpg" width="200"/> | -->

## Build Environment

`MacOS 11.5.2`  
`conda --version: 4.11.0`

### Create the virtual environment
``` vim
$ conda create --name atmpy38 python=3.8
$ conda activate atmpy38
```

### Install the package
``` vim
$ conda install numpy
$ conda install matplotlib
$ conda install -c anaconda basemap
$ conda install -c conda-forge basemap-data-hires
$ conda install -c conda-forge metpy
$ conda install pandas
$ conda install netcdf4
$ conda install -c conda-forge cartopy
```

### Verify version

``` vim
$ conda --version
conda 4.11.0

$ python --version
Python 3.8.16

$ python
>>> from mpl.toolkits.basemap import Basemap
>>> quit()
```

## Ready to Draw

```vim
$ cd draw_TAIWAN
$ python3 no_topographic.py       # draw the pure TAIWAN 
$ python3 with_topographic.py     # draw the TAIWAN with topographic relief
$ python3 main.py           # draw the complete TAIWAN
```

