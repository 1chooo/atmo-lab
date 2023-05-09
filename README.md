# Atmospheric-map

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

## Project Showcase

| Name  | Display |
| ----------- | -------------------------------- |
| Global Surface Temperature | <a href="<link>"><img src="./assets/imgs/temperature_timelapse.gif" alt="temperature timelapse" width="200"></a> |
| Draw TAIWAN | <a href="<link>"><img src="./draw_TAIWAN/img/Taiwan.jpg" alt="temperature timelapse" width="200"></a> |
| $CO_2$ Emission | <a href="<link>"><img src="./chem/src/imgs/watermark/monthly_mean/co2_recent_monthly_mean.jpg" alt="temperature timelapse" width="200"></a> |

<!-- <a href="<link>"><img src="./chem/src/imgs/watermark/monthly_mean/co2_recent_monthly_mean.jpg" alt="temperature timelapse" width="200"></a> -->

<!-- <img src="./draw_TAIWAN/img/Taiwan.jpg" width="200"/>  -->

## LICENSE

Released under [MIT](./LICENSE) by @1chooo.

* This software can be modified and reused without restriction.
* The original license must be included with any copies of this software.
* If a significant portion of the source code is used, please provide a link back to this repository.