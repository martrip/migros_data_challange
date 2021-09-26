import pandas as pd
from assign_store import assign_store
from assign_companies import assign_companies

#remove unneccessary columns from raw GeoFeatures data
df = pd.read_csv('C:/Users/Martina/Documents/Propulsion/migros_data_challange/data/GeoFeatures_Zurich_provided_by_UrbanDataLabs.csv')
df = df[['hh_ha', 'pers_ha', 'pt_dis', 'station_dis', 'lat', 'lng']]
#df.to_csv('C:/Users/Martina/Documents/Propulsion/migros_data_challange/data/GeoFeatures_Zurich_needed.csv', index=False)

# import and prepare supermarket data
df_competitors = pd.read_csv('C:/Users/Martina/Documents/Propulsion/migros_data_challange/data/supermarkets_clean_data.csv')
df_competitors = df_competitors.rename(columns={'geometry.viewport.northeast.lat': 'lat_shop', 'geometry.viewport.northeast.lng': 'lng_shop'})

# assign store data to GeoFeature data
df_assigned_stores = assign_store(df, df_competitors)
# df_assigned_stores.to_csv(
#     'C:/Users/Martina/Documents/Propulsion/migros_data_challange/data/GeoFeatures_Zurich_and_supermarkets.csv',
#     index=False)

# import and prepare company data
df_companies = pd.read_csv('C:/Users/Martina/Documents/Propulsion/migros_data_challange/data/companies_raw_data.csv')
df_companies = df_companies.drop(['company_ltd', 'company_lng'], axis=1)
df_companies = df_companies.drop_duplicates()
df_companies = df_companies.dropna(subset=['company_coordinates']).reset_index()
coordinates = [i for i in df_companies['company_coordinates'].str.replace('m', '').str.replace('s', '').str.split(' ')]
df_companies['lat_company'] = [float(i[0])+float(i[1])/60+float(i[2])/3600 for i in coordinates]
df_companies['lng_company'] = [float(i[4])+float(i[5])/60+float(i[6])/3600 for i in coordinates]

# assign company data to GeoFeature data
df_assigned_companies = assign_companies(df, df_companies)
# df_assigned_companies.to_csv(
#     'C:/Users/Martina/Documents/Propulsion/migros_data_challange/data/GeoFeatures_Zurich_and_companies.csv',
#     index=False)

#combine geofeature store and geofeature company data
df = pd.merge(df_assigned_stores, df_assigned_companies)
df.to_csv('C:/Users/Martina/Documents/Propulsion/migros_data_challange/data/GeoFeatures_Zurich_supermarkets_companies.csv', index=False)
