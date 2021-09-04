import pandas as pd
import geopandas as gpd
import numpy as np
from scipy.spatial import cKDTree
from shapely.geometry import Point
from kd_tree import ckdnearest

#data cleaning
df_companies = pd.read_csv('C:/Users/Martina/Documents/Propulsion/migros_data_challange/data/companies_raw_data.csv')
df_companies = df_companies.drop(['company_ltd', 'company_lng'], axis=1)
df_companies = df_companies.drop_duplicates()
df_companies = df_companies.dropna(subset=['company_coordinates']).reset_index()
coordinates = [i for i in df_companies['company_coordinates'].str.replace('m', '').str.replace('s', '').str.split(' ')]
df_companies['lat_company'] = [float(i[0])+float(i[1])/60+float(i[2])/3600 for i in coordinates]
df_companies['lng_company'] = [float(i[4])+float(i[5])/60+float(i[6])/3600 for i in coordinates]
df_companies['geometry'] = [Point(df_companies['lat_company'][i], df_companies['lng_company'][i]) for i in range(len(df_companies['lng_company']))]

df_geofeatures = pd.read_csv('C:/Users/Martina/Documents/Propulsion/migros_data_challange/data/GeoFeatures_Zurich_needed.csv')
df_geofeatures['geometry'] = [Point(df_geofeatures['lat'][i], df_geofeatures['lng'][i]) for i in range(len(df_geofeatures['lat']))]

assigned_df = ckdnearest(df_companies, df_geofeatures)
companies = {}
for index, row in assigned_df.iterrows():
    key = (row['lat'], row['lng'])
    if not key in companies:
        companies[key] = 1
    else:
        companies[key] += 1
print(companies)


number_company = []
for index, row in df_geofeatures.iterrows():
    key = (row['lat'], row['lng'])
    if key in companies:
        number_company.append(companies[key])
    else:
        number_company.append(0)

df_geofeatures['number_companies'] = number_company
df_geofeatures.to_csv('C:/Users/Martina/Documents/Propulsion/migros_data_challange/data/GeoFeatures_Zurich_and_companies.csv', index=False)
print(df_geofeatures[df_geofeatures['number_companies'] == 2])