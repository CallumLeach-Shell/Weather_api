import cdsapi
import requests
from functools import partial

session = requests.Session()

# Setting proxy settings, changing requests.get to work with the proxy (bug in cdsapi package (v0.2.7))
session.proxies = {
    'https': 'http://proxy-eu.shell.com:8080',
    'http': 'http://proxy-eu.shell.com:8080',
}

requests.get = partial(requests.get, proxies=session.proxies)

c = cdsapi.Client(session = session, verify=True)

c.retrieve("insitu-glaciers-elevation-mass",
{
"variable": "all",
"product_type": "elevation_change",
"file_version": "20170405",
"format": "tgz"
},
"download.tar.gz")
