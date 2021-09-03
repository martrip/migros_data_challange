import pandas as pd
import geopandas as gpd
import numpy as np
from scipy.spatial import cKDTree
from shapely.geometry import Point

df_companies = pd.read_csv('C:/Users/Martina/Documents/Propulsion/migros_data_challange/data/companies_raw_data.csv')
df_companies = df_companies.dropna(subset=['company_ltd', 'company_lng'])

df_geometry = pd.read_csv('C:/Users/Martina/Documents/Propulsion/migros_data_challange/data/GeoFeatures_Zurich_needed.csv')
coordinates_list = [Point(df_geometry['lat'][i], df_geometry['lng'][i]) for i in range(len(df_geometry['lat']))]
df_geometry['geometry'] = coordinates_list