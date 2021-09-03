import pandas as pd
import geopandas as gpd
import numpy as np
from scipy.spatial import cKDTree
from shapely.geometry import Point

# df = pd.read_csv('data/GeoFeatures_Zurich_provided_by_UrbanDataLabs.csv')
# df_dropped = df[['hh_ha', 'pers_ha', 'pt_dis', 'station_dis', 'lat', 'lng']]
# df_dropped.to_csv('data/GeoFeatures_Zurich_needed.csv', index=False)
df_geometry = pd.read_csv('data/GeoFeatures_Zurich_needed.csv')
lat_list = [Point(df_geometry['lat'][i], df_geometry['lng'][i]) for i in range(len(df_geometry['lat']))]
df_geometry['geometry'] = lat_list

print(type(df_geometry['geometry'][0]))
df_migros = pd.DataFrame({'shop': ['Migros', 'Migros Supermarkt'],
                          'lag_shop': [47.385409, 47.385509],
                          'lng_shop': [8.531639, 531649],
                          'geometry': [Point(47.385409, 8.531639), Point(47.385509, 8.531649)]})

def ckdnearest(gdA, gdB):
    nA = np.array(list(gdA.geometry.apply(lambda x: (x.x, x.y))))
    nB = np.array(list(gdB.geometry.apply(lambda x: (x.x, x.y))))
    btree = cKDTree(nB)
    dist, idx = btree.query(nA, k=1)
    gdf = pd.concat(
        [gdA.reset_index(drop=True), gdB.loc[idx, gdB.columns != 'geometry'].reset_index(drop=True),
         pd.Series(dist, name='dist')], axis=1)
    return gdf

test = ckdnearest(df_migros, df_geometry)
# test.drop('geometry')
df = df_geometry.drop('geometry', axis=1)
df_merged = pd.merge(df, test, how='outer')
print(df_merged[df_merged.shop == 'Migros'])
print(df_merged)

# #kd-tree for quick nearest-neighbor lookup
#
# gpd1 = gpd.GeoDataFrame([['John', 1, Point(1, 1)], ['Smith', 1, Point(1.25, 1.5)],
#                          ['Soap', 1, Point(1.25, 2)], ['Dani', 1, Point(1.3, 0.8)]],
#                         columns=['Name', 'ID', 'geometry'])
# gpd1 = gpd.GeoDataFrame([['John', 1, Point(1, 1)], ['Smith', 1, Point(1.25, 1.5)]],
#                         columns=['Name', 'ID', 'geometry'])
# gpd2 = gpd.GeoDataFrame([['Work', Point(0, 1.1)], ['Shops', Point(1.5, 2)],
#                          ['Home', Point(1.5, 2)]],
#                         columns=['Place', 'geometry'])
#
# def ckdnearest(gdA, gdB):
#     nA = np.array(list(gdA.geometry.apply(lambda x: (x.x, x.y))))
#     nB = np.array(list(gdB.geometry.apply(lambda x: (x.x, x.y))))
#     btree = cKDTree(nB)
#     dist, idx = btree.query(nA, k=1)
#     gdf = pd.concat(
#         [gdA.reset_index(drop=True), gdB.loc[idx, gdB.columns != 'geometry'].reset_index(drop=True),
#          pd.Series(dist, name='dist')], axis=1)
#     return gdf
#
# gdf = ckdnearest(gpd1, gpd2)
# print(gdf)