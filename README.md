# Weather_api

This is a api to download data from CMIP6 and load into the api.

-- Aims:
    - Access GCM: access-esm1.5
    - 40 ensemble members
    - Daily Surface Winds "sfcWind"

## Requirements
To run this script, there are a few python requirements.
Firstly we add the conda-forge channel.

```
conda config --env --add channels conda-forge
```
Then install the `acccmip6` and `cmpdata` packages respectivly.
```
conda install -c thassan acccmip6
```
```
conda install -c thassan cmpdata
```
