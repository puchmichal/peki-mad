import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

przedszkola = pd.read_csv('dane.csv')
wsp = przedszkola.apply(lambda z: Point(z.X, z.Y), axis=1)
crs = {'init': 'epsg:2263'}
przedszkola = gpd.GeoDataFrame(przedszkola)