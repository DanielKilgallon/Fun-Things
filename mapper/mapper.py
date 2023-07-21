import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
from shapely.geometry import Point

# https://towardsdatascience.com/geopandas-101-plot-any-data-with-a-latitude-and-longitude-on-a-map-98e01944b972
# https://catalog.data.gov/dataset/tiger-line-shapefile-2019-county-philadelphia-county-pa-topological-faces-polygons-with-all-geo/resource/fe480d21-760c-4893-b813-32255ab0c194

street_map = gpd.read_file('./faces/tl_2019_42101_faces.shp')
fig, ax = plt.subplots(figsize=(15,15))
street_map.plot(ax=ax)

df = pd.read_csv('./residential_parking_permit_blocks.csv')

# Convert to points
geometry = [Point(xy) for xy in zip(df['longitude'], df['latitude'])]
print(len(geometry) == 1342)

# Get geometry
geo_df = gpd.GeoDataFrame(df, crs=street_map.crs,
                          geometry=geometry) #specify the geometry list we created

# Plot data
fig, ax = plt.subplots(figsize=(15,15))
street_map.plot(ax=ax, alpha=1)
geo_df.plot(ax=ax,
    markersize=20,
    color='red',
    marker='^',
    label='Parking')
plt.legend(prop={'size':15})
plt.show()