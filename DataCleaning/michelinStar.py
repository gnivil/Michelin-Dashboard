# Import Dependencies 
import numpy as np
import pandas as pd 

# Read-in csv files 
oneStardf = pd.read_csv("oneStars.csv")
twoStardf = pd.read_csv("twoStars.csv")
threeStardf = pd.read_csv("threeStars.csv")

# Data Frame information 
"""oneStardf.info()
twoStardf.info()
threeStardf.info()
"""
# Create columns for each data frame 
oneStardf['michelin_stars'] = 1
twoStardf['michelin_stars'] = 2 
threeStardf['michelin_stars'] = 3

# Check info / null values in columns 
""" oneStardf.info()
twoStardf.info()
threeStardf.info()
"""

# Drop unwanted columns 
oneStardf = oneStardf.drop(columns = ['year', 'zipCode', 'price'])
twoStardf = twoStardf.drop(columns = ['year', 'zipCode', 'price'])
threeStardf = threeStardf.drop(columns = ['year', 'zipCode', 'price'])

"""
print (oneStardf.head())
oneStardf.info()

print (twoStardf.head())
twoStardf.info()

print(threeStardf.head())
threeStardf.info()
"""

# Append data frame 
combineddf = oneStardf.append(twoStardf, ignore_index= True)
combineddf = combineddf.append(threeStardf, ignore_index= True)
print (combineddf.head())
print (combineddf.tail(20))
combineddf.info()

# Find null values 
print (combineddf[combineddf['city'].isna()])

# Update null values for Hong Kong [City]
combineddf.at[152, 'city'] = 'Hong Kong'
combineddf.at[166, 'city'] = 'Hong Kong'

# Verify nulls have been removed / Hong Kong 'city' and 'region' are the same 
print (combineddf[combineddf['city'].isna()])


combineddf.to_csv('michelinStars_df.csv')