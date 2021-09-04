import pandas as pd

df_superm = pd.read_csv('C:/Users/Martina/Documents/Propulsion/migros_data_challange/data/GeoFeatures_Zurich_and_supermarkets.csv')
df_company = pd.read_csv('C:/Users/Martina/Documents/Propulsion/migros_data_challange/data/GeoFeatures_Zurich_and_companies.csv')

df = pd.merge(df_superm, df_company)
df.to_csv('C:/Users/Martina/Documents/Propulsion/migros_data_challange/data/GeoFeatures_Zurich_supermarkets_companies.csv', index=False)
