import pandas as pd

df = pd.read_csv('C:/Users/Martina/Documents/Propulsion/migros_data_challange/data/GeoFeatures_Zurich_supermarkets_companies.csv')
print('Migros: {}'.format(df.migros.sum()))
print('Coop: {}'.format(df.coop.sum()))
print('Discounter: {}'.format(df.discounter.sum()))
print('Other: {}'.format(df.other.sum()))

df_competitors = pd.read_csv('C:/Users/Martina/Documents/Propulsion/migros_data_challange/data/supermarkets_clean_data.csv')
print('Spar: {}'.format(df_competitors[df_competitors.search_name == 'SPAR'].search_name.count()))