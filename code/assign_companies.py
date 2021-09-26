
def assign_companies(df_features, df_companies):
    from kd_tree import ckdnearest
    from shapely.geometry import Point
    df_companies['geometry'] = [Point(df_companies['lat_company'][i], df_companies['lng_company'][i]) for i in
                                range(len(df_companies['lng_company']))]
    df_features['geometry'] = [Point(df_features['lat'][i], df_features['lng'][i]) for i in
                               range(len(df_features['lat']))]
    assigned_df = ckdnearest(df_companies, df_features)
    companies = {}
    for index, row in assigned_df.iterrows():
        key = (row['lat'], row['lng'])
        if not key in companies:
            companies[key] = 1
        else:
            companies[key] += 1
    number_company = []
    for index, row in df_features.iterrows():
        key = (row['lat'], row['lng'])
        if key in companies:
            number_company.append(companies[key])
        else:
            number_company.append(0)
    new_df = df_features.copy(deep=True)
    new_df['number_companies'] = number_company
    # new_df.to_csv(
    #     'C:/Users/Martina/Documents/Propulsion/migros_data_challange/data/GeoFeatures_Zurich_and_companies.csv',
    #     index=False)
    return new_df


#assign_companies(df_geofeatures, df_companies)