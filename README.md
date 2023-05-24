# Atmo Lab

## Intro

This is the project that observes the varing of global temperature for the first half of 2021. 

Hope you guys enjoy!!!  
And be helpful for the one who also interested in Atmospheric Science.

## Create Enviroment
`MacOS 11.5.2`  
`conda --version: 4.11.0`
``` vim
$ conda create --name atmpy38 python=3.8
$ conda activate atmpy38
```

### Build web

```shell
pip install mkdocs
pip install mkdocs-material
pip install pymdown-extensions
pip install mkdocstrings
pip install mkdocs-git-revision-date-plugin
pip install mkdocs-jupyter

mkdocs serve
mkdocs build
```

## Under atmpy38

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
jupyter nbconvert --to markdown draw_Taiwan.ipynb

## Project Showcase

| Name  | Display |
| ----------- | -------------------------------- |
| Global Surface Temperature | <a href="https://github.com/1chooo/global-climate/tree/main/surface_temperature"><img src="./assets/imgs/temperature_timelapse.gif" alt="temperature timelapse" width="200"></a> |
| Draw TAIWAN | <a href="https://github.com/1chooo/global-climate/tree/main/draw_TAIWAN"><img src="./draw_TAIWAN/img/Taiwan.jpg" alt="temperature timelapse" width="200"></a> |
| $CO_2$ Emission | <a href="https://github.com/1chooo/global-climate/tree/main/"><img src="./chem/src/imgs/watermark/monthly_mean/co2_recent_monthly_mean.jpg" alt="temperature timelapse" width="200"></a> |

<!-- <a href="<link>"><img src="./chem/src/imgs/watermark/monthly_mean/co2_recent_monthly_mean.jpg" alt="temperature timelapse" width="200"></a> -->

<!-- <img src="./draw_TAIWAN/img/Taiwan.jpg" width="200"/>  -->

## LICENSE

Released under [MIT](./LICENSE) by @1chooo.

* This software can be modified and reused without restriction.
* The original license must be included with any copies of this software.
* If a significant portion of the source code is used, please provide a link back to this repository.