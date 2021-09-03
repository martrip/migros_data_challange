import pandas as pd
import geopandas as gpd
import numpy as np
from scipy.spatial import cKDTree
from shapely.geometry import Point

#remove unneccessary columns from raw data
# df = pd.read_csv('C:/Users/Martina/Documents/Propulsion/migros_data_challange/data/GeoFeatures_Zurich_provided_by_UrbanDataLabs.csv')
# df_dropped = df[['hh_ha', 'pers_ha', 'pt_dis', 'station_dis', 'lat', 'lng']]
# df_dropped.to_csv('C:/Users/Martina/Documents/Propulsion/migros_data_challange/data/GeoFeatures_Zurich_needed.csv', index=False)

#add new column with both coordinates as type point in dataframes that need to be compared for closest neighbours
df_geometry = pd.read_csv('C:/Users/Martina/Documents/Propulsion/migros_data_challange/data/GeoFeatures_Zurich_needed.csv')
coordinates_list = [Point(df_geometry['lat'][i], df_geometry['lng'][i]) for i in range(len(df_geometry['lat']))]
df_geometry['geometry'] = coordinates_list
df_competitors = pd.read_csv('C:/Users/Martina/Documents/Propulsion/migros_data_challange/data/supermarkets_clean_data.csv')
df_competitors = df_competitors.rename(columns={'geometry.viewport.northeast.lat': 'lat_shop', 'geometry.viewport.northeast.lng': 'lng_shop'})
coordinates_shop_list = [Point(df_competitors['lat_shop'][i], df_competitors['lng_shop'][i]) for i in range(len(df_competitors['lat_shop']))]
df_competitors['geometry'] = coordinates_shop_list

#calculate nearest neighbour
#kd-tree for quick nearest-neighbor lookup function
def ckdnearest(gdA, gdB):
    nA = np.array(list(gdA.geometry.apply(lambda x: (x.x, x.y))))
    nB = np.array(list(gdB.geometry.apply(lambda x: (x.x, x.y))))
    btree = cKDTree(nB)
    dist, idx = btree.query(nA, k=1)
    gdf = pd.concat(
        [gdA.reset_index(drop=True), gdB.loc[idx, gdB.columns != 'geometry'].reset_index(drop=True),
         pd.Series(dist, name='dist')], axis=1)
    return gdf
assigned_df = ckdnearest(df_competitors, df_geometry)

#make df with number of supermarkets for each coordinate point in original geofeatures file
#need to get rid of geometry in one df so it won't be in the new df twice
assigned_df = assigned_df.drop('geometry', axis=1)
#new column to compare closest coordinates of supermarkets and take them together
assigned_df['lat, lng'] = assigned_df['lat'].astype(str) + ', ' + assigned_df['lng'].astype(str)
#new df to drop duplicates of coordinates
new_df = assigned_df[['lat, lng', 'lat', 'lng']]
new_df = new_df.drop_duplicates('lat, lng')
list_lat_lng = new_df['lat, lng'].tolist()
#make lists of new columns wanted in the new df to keep count of supermarkets per point
migros = []
coop = []
discounter = []
other = []
sup_columns = [migros, coop, discounter, other]
distance_limit = 1 #to make sure no supermarket outside of our region of interest is accidently included
for i in range(len(list_lat_lng)):
    lat_lng = list_lat_lng[i]
    for k in range(len(sup_columns)):
        sup_columns[k].append(0)
    df_same = assigned_df[assigned_df['lat, lng'] == lat_lng]
    count = df_same['search_name'].count()
    for c in range(count):
        distance = df_same.iloc[c].dist
        if distance > distance_limit:
            continue
        brand = df_same.iloc[c].search_name.lower()
        if brand in ['migros']:
            migros[i] += 1
        elif brand in ['coop']:
            coop[i] += 1
        elif brand in ['lidl', 'aldi']:
            discounter[i] += 1
        elif brand in ['denner']: #exclude denner since next to nearly every migros is a denner and they are the same
            continue
        else:
            other[i] += 1

df = pd.DataFrame({'lat': new_df['lat'].tolist(),
                   'lng': new_df['lng'].tolist(),
                   'migros': migros,
                   'coop': coop,
                   'discounter': discounter,
                   'other': other,})
df['competitors'] = df['coop'] + df['discounter'] + df['other'] #count all competitor supermarkets per coordinate
df['all_supermarkets'] = df['migros'] + df['coop'] + df['discounter'] + df['other'] #count all supermarkets per coordinate
df_merged = pd.merge(df_geometry, df, how='outer')
df_merged = df_merged.fillna(0)
df_merged.to_csv('C:/Users/Martina/Documents/Propulsion/migros_data_challange/data/GeoFeatures_Zurich_and_supermarkets.csv', index=False)

