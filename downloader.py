"""
Using the acccmip6 api, we load configuration parameters from a config.yaml file and parse them into a downloader. Which will download relevent data from the ESGF CMIP6 datastores.
"""

from acccmip6.access_cm import SearchCmip6
from acccmip6.download_dat import DownloadCmip6
import yaml

def config_loader():
    try:
        # Here we load the configuration file, which passes the parameters into the downloader.
        with open('config.yaml') as f:
            config = yaml.load(f, Loader=yaml.FullLoader)
            config = config['Downloader']

    except FileNotFoundError as err:
        print(f'LOAD CONFIG ERROR: {err}')

    # With lists specified in the yaml file, the acccmip6 api requires it to be comma seperated variables. We convert here.
    for key, value in config.items():
        if type(value) is list:
            config[key] = ','.join(map(str, config[key]))
        else:
            continue

    return config


def downloader(config):
    try:
        # download the data to .nc files given the specified arguments from the configuration file.
        DownloadCmip6(model = config['model'], variable = config['variable'], experiment = config['experiment'], frequency = config['frequency'], realm = config['realm'], rlzn = config['rlzn'], path = config['data_directory'], year = config['year'])
    except Exception as ex:
        print(f'DOWNLOADER ERROR: {ex}')

def search(config):
    try:
        # search the database given specified arguments
        SearchCmip6(model = config['model'], variable = config['variable'], experiment = config['experiment'], year = config['year'], time='yes')
    except Exception as ex:
        print(f'SEARCH ERROR: {ex}')


if __name__ == "__main__":

    # Load the configurations, the azure env and the cmip6 yaml file.
    config = config_loader()

    if config['output'] == 'S':
        search(config)
    elif config['output'] == 'D':
        downloader(config)
