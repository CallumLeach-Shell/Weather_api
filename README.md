# Weather_api

This tool is two part, consisting of a downloader and netCDF processor. The downloader is a wrapper for the `acccmip6` api, which downloads data from the CMIP6 datastores given a set of parameters set in a `config.yaml` file. Onced downloaded, the processor will slice the netCDF files by a longitude and latitude bounding box saving as its own data subset.

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
