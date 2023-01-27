## This file will mask the global data by a lat-lon bounding box.

import netCDF4
import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import json

def load_data(country_code: str):
    file = netCDF4.Dataset('./CMIP6/sfcWind_day_ACCESS-ESM1-5_ssp126_r34i1p1f1_gn_20150101-20641231.nc')

    # Load the country boundign box json file.
    with open("country_bounding_box.json", "r") as infile:
        bounding_box_raw = json.load(infile)

    # Integrate the config.yaml to specify a bounding box, either manually or using country codes.
    if len(country_code) > 2:        
        country_bbox = next(bounding_box_raw[i][1] for i in bounding_box_raw if bounding_box_raw[i][0] == country_code)
    else:
        country_bbox = bounding_box_raw[country_code][1]

    return file, country_bbox


def process_data(country_bbox: list):

    latbounds = [country_bbox[1], country_bbox[3]]
    lonbounds = [country_bbox[0], country_bbox[2]]

    lats = file.variables["lat"][:]
    lons = file.variables["lon"][:]
    time = file.variables["time"]

    # latitude lower and upper index
    latli = np.argmin( np.abs( lats - latbounds[0] ))
    latui = np.argmin( np.abs( lats - latbounds[1] )) 

    # longitude lower and upper index
    lonli = np.argmin( np.abs( lons - lonbounds[0] ))
    lonui = np.argmin( np.abs( lons - lonbounds[1] ))  

    sfcWindSubset = file.variables['sfcWind']

    # The +1 will add the next nearest observation, removes problems with only a single observation.
    sfcWind = sfcWindSubset[1, latli:(latui) , lonli:(lonui)]

    # Have north pointing upwards on the map.
    sfcWind = sfcWind[:,::-1]

    # Write the subset data to a file
    sfcWind.to_netcdf(path= './Processed/sfcWind_day_ACCESS-ESM1-5_ssp126_r34i1p1f1_gn_20150101-20641231.nc')

    plt.contourf(sfcWind)
    plt.show(block=True)

if __name__ == '__main__':

    # Specify the country code or the country name to search the loaded bounding box json
    country_code = 'AU'

    file, country_bbox = load_data(country_code)

    process_data(country_bbox)
