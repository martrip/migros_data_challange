#kd-tree for quick nearest-neighbor lookup example
import pandas as pd
import geopandas as gpd
import numpy as np
from scipy.spatial import cKDTree
from shapely.geometry import Point

def ckdnearest(gdA, gdB):
    nA = np.array(list(gdA.geometry.apply(lambda x: (x.x, x.y))))
    nB = np.array(list(gdB.geometry.apply(lambda x: (x.x, x.y))))
    btree = cKDTree(nB)
    dist, idx = btree.query(nA, k=1)
    gdf = pd.concat(
        [gdA.reset_index(drop=True), gdB.loc[idx, gdB.columns != 'geometry'].reset_index(drop=True),
         pd.Series(dist, name='dist')], axis=1)
    return gdf

# #example
# gpd1 = gpd.GeoDataFrame([['John', 1, Point(1, 1)], ['Smith', 1, Point(1.25, 1.5)]],
#                         columns=['Name', 'ID', 'geometry'])
# gpd2 = gpd.GeoDataFrame([['Work', Point(0, 1.1)], ['Shops', Point(1.5, 2)],
#                          ['Home', Point(1.5, 2)]],
#                         columns=['Place', 'geometry'])
# gdf = ckdnearest(gpd1, gpd2)
# print(gdf)