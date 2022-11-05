import pandas as pd
import geopandas as gpd
import requests
from pyzipcode import ZipCodeDatabase
zcdb = ZipCodeDatabase()
in_radius = [z.zip for z in zcdb.get_zipcodes_around_radius('95403', 10)] # ('ZIP', radius in miles)
radius_utf = [x.encode('UTF-8') for x in in_radius] # unicode list to utf list

# path_pre = '/Users/jonahbuckingham-cain/PycharmProjects/pythonProject/venv/static/'
# path_shape = path_pre + 'tl_2022_us_zcta520.shp'
#
# # Read shapefiles. Change paths
# zipcodes = gpd.read_file("/Users/jonahbuckingham-cain/PycharmProjects/pythonProject/venv/static/tl_2022_us_zcta520.shp")