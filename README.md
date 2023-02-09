# Weather_api

This tool is two part, consisting of a downloader and netCDF processor. The downloader is a wrapper for the `acccmip6` api, which downloads data from the CMIP6 datastores given a set of parameters set in a `config.yaml` file. Onced downloaded, the processor will slice the netCDF files by a longitude and latitude bounding box saving as its own data subset.

## Requirements
To run this script, there are a few python requirements.

### Running the Script
Running the script is achived with the use of a 'config.yaml' yaml file to determine all the downloading parameters. These parameters do not differ much from the original [acccmip6 Documentation](https://acccmip6.readthedocs.io/en/latest/index.html)

#### Options:
Look at [acccmip6 Documentation](https://acccmip6.readthedocs.io/en/latest/index.html) for a comprehensive list of all the parameters to specify. One thing to note is on specifying a list of arguments for a parameter. This is done in the following way, for example, to specify multiple models for download one could write the following:
```yaml
model: 
  - ACCESS-ESM1-5
  - UKESM1-0-LL
  - ACCESS-CM2 
  - CAMS-ESM1-0 
```


### Development Environment
Firstly we add the conda-forge channel, then create a conda env from which to work.

```
conda config --env --add channels conda-forge
```
Then install the `acccmip6` and `cmpdata` packages respectivly.
```
conda install -c thassan acccmip6
```

### Processing
This section concerns the processing of netCDF files, and subsetting them by longitude and latitude.