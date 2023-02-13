## This file will mask the global data by a lat-lon bounding box.

import netCDF4
import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import json
from mpl_toolkits.basemap import Basemap

def load_data(country_code: str):

    file = xr.open_dataset('./CMIP6/sfcWind_day_ACCESS-ESM1-5_ssp126_r34i1p1f1_gn_20150101-20641231.nc')
    # Load the country bounding box json file.

    # Open the bounding box json file.
    with open("country_bounding_box.json", "r") as infile:
        bounding_box_raw = json.load(infile)

    if len(country_code) > 2:        
        country_bbox = next(bounding_box_raw[i][1] for i in bounding_box_raw if bounding_box_raw[i][0] == country_code)
    else:
        country_bbox = bounding_box_raw[country_code][1]

    return file, country_bbox

def process_data(country_bbox: list, file):

    latbounds = [country_bbox[1], country_bbox[3]]
    lonbounds = [country_bbox[0], country_bbox[2]]

    data_subset = file.sel(lat=slice(*latbounds), lon=slice(*lonbounds))

    sfcWind = data_subset.sfcWind

    # Write the subset data to a file
    sfcWind.to_netcdf(path= './Processed/sfcWind_day_ACCESS-ESM1-5_ssp126_r34i1p1f1_gn_20150101-20641231.nc')

if __name__ == '__main__':

    # Specify the country code or the country name to search the loaded bounding box json
    country_code = 'AU'

    file, country_bbox = load_data(country_code)

    process_data(country_bbox, file)
