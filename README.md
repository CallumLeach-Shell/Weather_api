# Weather_api

This tool is a wrapper using the 'acccimp6' python api to download data effectivly from the CMIP6 datastores.

-- Aims:
    - Access GCM: access-esm1.5
    - 40 ensemble members
    - Daily Surface Winds "sfcWind"

## Requirements
To run this script, there are a few python requirements.

### Running the Script
Running the script is achived with the use of a 'config.yaml' yaml file to determine all the downloading parameters. These parameters do not differ much from the original [acccmip6 Documentation](https://acccmip6.readthedocs.io/en/latest/index.html)




### Development Environment
Firstly we add the conda-forge channel, then create a conda env from which to work.

```
conda config --env --add channels conda-forge
```
Then install the `acccmip6` and `cmpdata` packages respectivly.
```
conda install -c thassan acccmip6
```
