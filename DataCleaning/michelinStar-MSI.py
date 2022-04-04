# Import Dependencies 
import numpy as np
import pandas as pd 

# Read-in csv files 
oneStardf = pd.read_csv("oneStars.csv")

twoStardf = pd.read_csv("twoStars.csv")

threeStardf = pd.read_csv("threeStars.csv")

# Data Frame information 
"""
oneStardf.info()
twoStardf.info()
threeStardf.info()
"""
# Create columns for each data frame 
oneStardf['michelin_stars'] = 1
twoStardf['michelin_stars'] = 2 
threeStardf['michelin_stars'] = 3

# Check info / null values in columns 
""" 
oneStardf.info()
twoStardf.info()
threeStardf.info()
"""

# Drop unwanted columns 
oneStardf = oneStardf.drop(columns = ['year', 'zipCode', 'price'])
twoStardf = twoStardf.drop(columns = ['year', 'zipCode', 'price'])
threeStardf = threeStardf.drop(columns = ['year', 'zipCode', 'price'])

# Info Update 
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
combineddf.info()
print (combineddf.head())
print (combineddf.tail())

# Write to new .csv file for SQL use 
combineddf.to_csv("michelinStarDF.csv")
