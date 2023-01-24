### This file will be to gather the data from relevant sources and perform the relevant transformations.

from acccmip6.access_cm import SearchCmip6
from acccmip6.download_dat import DownloadCmip6
import yaml

# Here we load the configuration file, which passes the parameters into the downloader.
with open('config.yaml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

# the model parameter can be passed as a list of comma seperated variables, this checks for that.
if type(config['model']) is list:
    model = ','.join(config['model'])
else:
    model = config['model']

# download the data to .nc files given the specified arguments
DownloadCmip6(model = model, variable = config['variable'], experiment = config['experiment'], rlzn = config['rlzn'], dl_dir = config['data_directory'])

# This command with search the database given specified arguments
#SearchCmip6(model = "ACCESS-ESM1-5", variable = "sfcWind", experiment = "ssp126", rlzn = "34")
