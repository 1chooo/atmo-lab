# Atmospheric-map

## Intro

This is the project that observes the varing of global temperature for the first half of 2021. 

Hope you guys enjoy!!! 

And be helpful for the one who also interested in Atmospheric Science.

![](./temperature_timelapse.gif)

## Create Enviroment
> MacOS 11.5.2
> 
> conda --version: 4.11.0
> ``` shell
> $ conda create --name atmpy37 python=3.7
> $ conda activate atmpy37
> ```

## Under atmpy37

>``` shell
> $ conda install numpy
> $ conda install matplotlib
> $ conda install basemap
> $ conda install netcdf4
> ```

### Verify version

> ``` shell
> $ conda --version
> conda 4.11.0
> 
> $ python --version
> Python 3.7.6
> 
> $ python
> 
> >>> from mpl.toolkits.basemap import Basemap
> >>> quit()
> ```

### Steps
#### 1. Through app1 to test.
> ``` shell
> $ cd basemap
> 
> $ python3 app1.py
> 
> $ python3 SaveFig.py
> 
> $ python3 ToGif.py
> ```

#### 2. Run app2 to generate the formal status.
> ``` shell
> $ cd basemap
> 
> $ python3 app2.py
> ```


#### 3. Well done ^_^, but it still an additional try. we can try to draw a Taiwan Map.
> ``` shell
> $ cd basemap
> 
> $ python3 DrawTW.py
> ```