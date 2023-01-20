### This file will be to gather the data from relevant sources and perform the relevant transformations.

from acccmip6.access_cm import SearchCmip6
from acccmip6.download_dat import DownloadCmip6


### Arguments ###
model = "ACCESS-ESM1-5"
variable = "sfcWind"
experiment = "ssp126"
rlzn = "34"

dl_dir = ""

# This command with search the database given specified arguments
#SearchCmip6(model = "ACCESS-ESM1-5", variable = "sfcWind", experiment = "ssp126", rlzn = "34")

# download the data to .nc files given the specified arguments
DownloadCmip6(model = model, variable = variable, experiment = experiment, rlzn = rlzn, dl_dir=dl_dir)

