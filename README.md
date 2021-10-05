# :mag: Finding the next Migros store location

<br/> :switzerland: **Background and Task:**
<br/> Migros is one of the largest retail companies in Switzerland.
As data scientists we were tasked with finding the best places to create new Migros stores in the city and surrounding of Zurich. We should analyze the market opportunities based on the density of existing stores, presence of competitors, and general population density to inform Migros’ development strategy.
<img width="960" alt="image" src="https://user-images.githubusercontent.com/89683936/134371145-117e1d09-e608-4113-8d4d-21e62c998ba2.png">

<br/> ::thought_balloon:: **Data Collection** 
- Data provided by Urban Data Lab
- "DataExploraton": 
  - Google Places API: Locations of all Migros and competitor (Coop, Aldi, Lidl, Spar) stores in the city and surrounding of Zurich 
  - Webscaping of Yello: Locations of Businesses in the city and surrounding of Zurich 


<br/> :page_with_curl: **Feature Descriptions:** 
- Population
  - Population Density
  - Household Density
- Businesses
  - Business Density
- Public Transport
  - Public transport distance
  - Public transport quality
  - Distance to next stop
- Migros
  - Migros locations
  - Migros within 500m
- Competitors 
  - Locations of competitors
- Infrastructure
  - Noise street
  - Building footprint
  - Number of buildings within 500m
  

:pencil2: **Data Processing:** 

-Feature engineering, description of the individual engineering steps  
-combine_data: main file, assigning supermarkets and companies to the closest pre-defined geolocation
  - "assign_companies" and "assign_store" functions used in the main file "combine_data"
  - "kd_tree" function used in the "assign_companies" and "assign_store" files
-"get_some_numbers": numbers needed for our final presentation
-"Counter": This module counts all supermarkets within a distance of 500m for every row in the dataset
-"Heatmap": this notebook visualizes the analyzed data

<br/> :abacus: **Methodology/ Modelling** 

-"DataExploraton": Logistic regression. Having different geolocation with some variables describing it's characteristics and one binary variable to define if exists a migros in that location or not, gave us the idea of applying a logistic regression to try to predict how probable it is to have a migros in each one of the locations where there is not one yet.

After some feature engineering the 3 variables that looked like were relevant to predict the migros location were:

- hh_ha
- pers_ha
- pt_dis
- station_dis

<br/> :chart_with_upwards_trend: **Results & Visualizations:** 

<img width="960" alt="image" src="https://user-images.githubusercontent.com/89683936/134368103-30a03458-5e6f-4097-83d8-b0a7b4261a95.png">


As a result we saw there are more potential Migros locations. Based on the pupulation density (layering) and the results from the Logistic Regression 
Potential area: City Centre close to the ETH (student area) and Universitäts Spital (one of the biggest hospitals of Switzerland) --> Student area & Hospital, but no Coop or Migros

