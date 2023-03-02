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
    
    except FileNotFoundError as err:
        print(f"LOAD CONFIG ERROR: {err}")

    # A few conditions when processing input from yaml file.
    if os.path.isdir(config['to_process'][0]):
        files = os.listdir(config['to_process'])

    else:
        files = config['to_process']

    country_code = config['country_code']

    # Open the bounding box json file.
    with open("country_bounding_box.json", "r") as infile:
        bounding_box_raw = json.load(infile)

    if len(country_code) > 2:        
        country_bbox = next(bounding_box_raw[i][1] for i in bounding_box_raw if bounding_box_raw[i][0] == country_code)
    else:
        country_bbox = bounding_box_raw[country_code][1]

    return files, country_bbox

def process_data(country_bbox: list, dataset, file_name:str):

    latbounds = [country_bbox[1], country_bbox[3]]
    lonbounds = [country_bbox[0], country_bbox[2]]

    data_subset = dataset.sel(lat=slice(*latbounds), lon=slice(*lonbounds))

    sfcWind = data_subset.sfcWind

    # Write the subset data to a file
    sfcWind.to_netcdf(path= ''.join(['./Processed/', file_name]))

if __name__ == '__main__':

    files, country_bbox = load_data()

    for file in files:
        dataset = xr.open_dataset(file)
        file_name = os.path.basename(file)

        process_data(country_bbox, dataset, file_name)
