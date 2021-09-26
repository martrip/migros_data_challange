# migros_data_challange

<br/> :switzerland: **Background and Task:**
<br/> Migros is one of the largest retail companies in Switzerland.
As data scientists we were tasked with finding the best places to create new Migros stores in the city and surrounding of Zurich. We should analyze the market opportunities based on the density of existing stores, presence of competitors, and general population density to inform Migros’ development strategy.
<img width="960" alt="image" src="https://user-images.githubusercontent.com/89683936/134371145-117e1d09-e608-4113-8d4d-21e62c998ba2.png">

<br/> ::thought_balloon:: **Data Collection** @Ruben and @Lisa (Python Modules and short description)
- Data provided by Urban Data Lab
- Google Places API: Locations of all Migros and competitor (Coop, Aldi, Lidl, Spar) stores in the city and surrounding of Zurich 
- Webscaping of Yello: Locations of Businesses in the city and surrounding of Zurich 
- 
<br/> :page_with_curl: **Feature Descriptions:** @lisa
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
  

:pencil2: **Data Processing:** @Martina and @Mario (Python Modules and short description)

-To do: Names of python modules
-Feature engineering, description of the individual engineering steps  

<br/> :abacus: **Methodology/ Modelling** @Ruben (Python Modules and short description)

-Logistic regression: Input variables, description what we did

<br/> :chart_with_upwards_trend: **Results & Visualizations:** @Mario (Python Modules and short description)

<img width="960" alt="image" src="https://user-images.githubusercontent.com/89683936/134368103-30a03458-5e6f-4097-83d8-b0a7b4261a95.png">


As a result we saw there are more potential Migros locations. Based on the pupulation density (layering) and the results from the Logistic Regression 
Potential area: City Centre close to the ETH (student area) and Universitäts Spital (one of the biggest hospitals of Switzerland) --> Student area & Hospital, but no Coop or Migros

