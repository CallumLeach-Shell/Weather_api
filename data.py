### This file will be to gather the data from relevant sources and perform the relevant transformations.

from acccmip6.access_cm import SearchCmip6
from acccmip6.download_dat import DownloadCmip6
import yaml

def config_loader():
    try:

        # Here we load the configuration file, which passes the parameters into the downloader.
        with open('config.yaml') as f:
            config = yaml.load(f, Loader=yaml.FullLoader)

        # With lists specified in the yaml file, the acccmip6 api requires it to be comma seperated variables.
        for key, value in config.items():
            if type(value) is list:
                config[key] = ','.join(config[key])
            else:
                continue
        
        return config
    
    except FileNotFoundError as err:
        print(f'ERROR: {err}')

def downloader():

    # download the data to .nc files given the specified arguments
    DownloadCmip6(model = config['model'], variable = config['variable'], experiment = config['experiment'], rlzn = config['rlzn'], dl_dir = config['data_directory'])

# This command with search the database given specified arguments
#SearchCmip6(model = "ACCESS-ESM1-5", variable = "sfcWind", experiment = "ssp126", rlzn = "1, 2, 3")


if __name__ == "__main__":
    config = config_loader()
