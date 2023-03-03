"""
This file will mask the global data by a lat-lon bounding box, then save the resulting mask as a .nc file in the Processed directory
"""

import netCDF4
import xarray as xr
import numpy as np
import json
import yaml
import os

def load_data():

    try:
        with open('config.yaml') as f:
            config = yaml.load(f, Loader=yaml.FullLoader)
            config = config['Processor']
        
        # Convert any single path strings to a list
        if type(config['to_process']) == str:
            config['to_process'] = [config['to_process']]
    
    except FileNotFoundError as err:
        print(f"LOAD CONFIG ERROR: {err}")
    
    # Error Conditions, check that to_process and country_code are listed in the yml file

    if config['to_process'] is None:
        print("to_process is empty in yaml file")
        raise ValueError
    elif config['country_code'] is None:
        print("country_code is empty in yaml file")
        raise ValueError
       
    # Processing the correct paths from the yaml file.
    for path in config['to_process']:
        if os.path.isdir(path):
            files = [os.path.join(path, file,) or files for file in os.listdir(path)]
        else:
            files = config['to_process']
        
    country_code = config['country_code']
    output_directory = config['output_directory']

    # Check that the output_directory exists and is not None. If it does not exist, create it.
    if output_directory is not None and os.path.isdir(output_directory):
        os.makedirs(output_directory)
    else:
        pass

    # Open the bounding box json file.
    with open("country_bounding_box.json", "r") as infile:
        bounding_box_raw = json.load(infile)

    if len(country_code) > 2:        
        country_bbox = next(bounding_box_raw[i][1] for i in bounding_box_raw if bounding_box_raw[i][0] == country_code)
    else:
        country_bbox = bounding_box_raw[country_code][1]

    return files, country_bbox, output_directory

def process_data(country_bbox: list, dataset, file_name:str, output_directory):
    output_directory = output_directory or './Processed/'

    latbounds = [country_bbox[1], country_bbox[3]]
    lonbounds = [country_bbox[0], country_bbox[2]]

    data_subset = dataset.sel(lat=slice(*latbounds), lon=slice(*lonbounds))

    sfcWind = data_subset.sfcWind

    # Write the subset data to a file
    sfcWind.to_netcdf(path= os.path.join(output_directory, file_name))

if __name__ == '__main__':

    files, country_bbox, output_directory = load_data()
    for file in files:
        dataset = xr.open_dataset(file)
        file_name = os.path.basename(file)

        process_data(country_bbox, dataset, file_name, output_directory)
