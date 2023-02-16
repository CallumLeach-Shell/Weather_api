import os
from dotenv import load_dotenv
from azure.storage.fileshare import ShareFileClient

# Load the env file
env_file = "./.env"
load_dotenv(dotenv_path=env_file)

connection_string = os.environ.get("CONNECTION_STRING")
container_name = os.environ.get("CONTAINER_NAME")

http_proxy: str = "http://proxy-eu.shell.com:8080"
https_proxy: str = "http://proxy-eu.shell.com:8080"

#Add this proxy by passing 'proxies = proxy_dict()' as an argument into the from_connection_string function.

def proxy_dict() -> dict:
        """dict: Create a dictionary of the proxy settings to be used in other methods of this class"""
        return dict(http=http_proxy, https=https_proxy)

file_client = ShareFileClient.from_connection_string(conn_str=connection_string, proxies= proxy_dict(), share_name="stats", file_path="project/Methane/DivergenceMethod/Gradient_based_method.png")

data = file_client.download_file()

# get full path of file.
with open(data.name, "wb") as file_handle:
        file_handle.write(data.content_as_bytes())