# Michelin-Dashboard

**Proposal**

We have decided to pursue a “Michelin Map” that will consist of one, two, and three Michelin Star restaurants worldwide. Using this interactive map, we want our users to have access to destination estimates. 

Our original [dataset](https://www.kaggle.com/jackywang529/michelin-restaurants) includes basic information on each michelin star restaurant in CSVs. Initially we will clean our data using pandas in a jupyter notebook. We will then create a SQL database to house all of that information, which will feed into our Python Flask API. We will deploy our dashboard through this Flask App, utilizing leaflet layers to add interactive and user-friendly elements to the Michelin Map. Our interactive map will essentially be the one-stop shop for a travel guide to michelin star restaurants. We will webscrape data for each restaurant such that when our app is deployed, you will be able to click each restaurant and know relevant details (price, cuisine type etc) and travel information. This webscrape will be coming directly from the Michelin guide website- where we will store in a MongoDB. This dictionary format will be convenient for the MongoDB storage and JavaScript implementation. The interactive map will include a drop down with multiple views, including a layer for each star level, in case users want to only look at one star level at a time. 







See below for examples on how the Michelin Map looks:

*City Input Example*

![Restaurant Map](https://github.com/Bgood524/Michelin-Dashboard/blob/main/Proposal_Data/Images/Deploy_2.JPG)


*Zip Code input with dark mode*

![Restaurant Info to Scrape](https://github.com/Bgood524/Michelin-Dashboard/blob/main/Proposal_Data/Images/Deploy_3.JPG)

*Filters and Legend view*

![Visualization](https://github.com/Bgood524/Michelin-Dashboard/blob/main/Proposal_Data/Images/Deploy_1.JPG)

