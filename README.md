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
In production this application will require only 4 files. Both the `downloader.exe`, `process.exe` scripts and their respective configuration files `config.yaml` `country_bounding_box.json`. These files are to be placed in the same directory and can be run from anywhere. Simply alter the parameters in `config.yaml` to your liking and reach each `.exe` file.


## Downloader Script

### Running the Script
To run the `downloader.py` script simply enter the **Weather_API** directory and run the following command:
```python
python downloader.py
```

There is no need to pass any arguments to the script, as they are all specified from within the `config.yaml` file.

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
The processor script `process.py` is designed to take the downloaded netCDF files and subset the data by specified latitude-longitude bounding boxes.

### Running the Script
To run the `process.py` script simply enter the **Weather_API** directory and run the following command:
```python
python process.py
```

Like the `downloader.py` script there is no need to pass any arguments when running.

#### Required Arguments
* `to_process`: Either a list of specifc file paths, or the path of a directory you want to run the processor. (Note that you can only specify a single directory at this time.)
* `country_code`: Either a country code or the country name, which will be used to subset the data based on pre-defined latitude-longitude bounding boxes.

#### Optional Arguments
* `output_directory`: This is optional and will default to `./Processed/`. If the directory specified does not exist, then one shall be created.

## Additional Links:
[acccmip6 Documentation](https://acccmip6.readthedocs.io/en/latest/index.html)