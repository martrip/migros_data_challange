
def assign_store(df_features, df_stores):
    from shapely.geometry import Point
    from kd_tree import ckdnearest
    # add new column with both coordinates as type point in dataframes that need to be compared for closest neighbours
    df_features['geometry'] = [Point(df_features['lat'][i], df_features['lng'][i]) for i in
                               range(len(df_features['lat']))]
    df_stores['geometry'] = [Point(df_stores['lat_shop'][i], df_stores['lng_shop'][i]) for i in
                             range(len(df_stores['lat_shop']))]
    # calculate nearest neighbour
    assigned_df = ckdnearest(df_stores, df_features)
    distance_limit = 0.01
    supermarkets_geo = {}
    for index, row in assigned_df.iterrows():
        if row['dist'] > distance_limit:
            continue
        key = (row['lat'], row['lng'])
        if not key in supermarkets_geo:
            supermarkets_geo[key] = {'migros': 0,
                                     'coop': 0,
                                     'discounter': 0,
                                     'other': 0}
        brand = row['search_name'].lower()
        if brand == 'migros':
            supermarkets_geo[key]['migros'] += 1
        elif brand == 'coop':
            supermarkets_geo[key]['coop'] += 1
        elif brand in ['lidl', 'aldi']:
            supermarkets_geo[key]['discounter'] += 1
        elif brand == 'denner':  # exclude denner since next to nearly every migros is a denner and they are the same
            continue
        else:
            supermarkets_geo[key]['other'] += 1
    new_df = df_features.copy(deep=True)
    for key in list(supermarkets_geo.values())[0].keys():
        new_df[key] = 0
    for index, row in new_df.iterrows():
        key = (row['lat'], row['lng'])
        if key in supermarkets_geo:
            for store, count in supermarkets_geo[key].items():
                new_df.loc[index, store] = count
    new_df['competitors'] = new_df['coop'] + new_df['discounter'] + new_df['other']  # count all competitor supermarkets per coordinate
    new_df['all_supermarkets'] = new_df['migros'] + new_df['competitors']  # count all supermarkets per coordinate
    return new_df


#df = assign_store(df_geofeatures, df_competitors)

