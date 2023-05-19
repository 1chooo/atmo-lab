# Usage

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