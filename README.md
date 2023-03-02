# Weather_api

This tool is two part, consisting of a downloader and netCDF processor. The downloader is a wrapper for the `acccmip6` api, which downloads data from the CMIP6 datastores given a set of parameters set in a `config.yaml` file. Onced downloaded, the processor will slice the netCDF files by a longitude and latitude bounding box saving as its own data subset.

## Development Environment Setup
When running locally in a Development environment, there are a few things to note about the setup.

### Requirements
It is recommended to setup a virtual environment (not covered here), then install the dependencies as follows:
```python
pip install -r requirements.txt
```

## Production Environment Setup
WIP, need to write this section when setup in the VM


## Downloader Script

### Running the Script
Running the script is achived with the use of a 'config.yaml' yaml file to determine all the downloading parameters. These parameters do not differ much from the original [acccmip6 Documentation](https://acccmip6.readthedocs.io/en/latest/index.html)

#### Options:
For a full list of options, please look at the documentation link listed at the bottom of this page.

#### Required Arguments:
* `output`: Takes an output type. `S` for search functionality and `D` for downloading from the database.
* `data_directory`: This is hard coded to be a Azure file share location.
* `to_process`: This is only required for processing, dont worry about it for the downloader.

#### Optional Arguments:
* `model`: Model names (you can specify multiple model names)
* `experiment`: Experiment names (you can specify multiple experiments)
* `frequency`: CMIP6 output frequency (day, mon, etc)
* `variable`: Variable names
* `realm`: Realm names (e.g. atmos, ocean etc)
* `rlzn`: Select specified realisation. (this will download all variants)
* `node`: Select specific data node (multiple selections allowed)
* `skip`: skip any item (model/experiment/realisations) from your download.
* `year`: Select data which fits to a certain time period (number of years, i.e use -5 to select final 5 years)

From the above options, you can specify multiple parameters for variables `model`, `experiment`, `variable`, `frequency`, `realm`, `rlzn`, `node` and `year`. Below is an example of specifying multiple models:

```yaml
model: 
  - ACCESS-ESM1-5
  - UKESM1-0-LL
  - ACCESS-CM2 
  - CAMS-ESM1-0 
```

## Processor Script

### Processing
This section concerns the processing of netCDF files, and subsetting them by longitude and latitude.

## Additional Links:
[acccmip6 Documentation](https://acccmip6.readthedocs.io/en/latest/index.html)