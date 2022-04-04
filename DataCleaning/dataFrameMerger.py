# Import Dependencies 
from typing import Dict
from numpy.lib.stride_tricks import _maybe_view_as_subclass
import pandas as pd 
import json
import pprint as pp
from pymongo import collection
import requests
from pymongo import MongoClient


# Import CSVs 

# One Side of Merge (Kaggle DF)
oneStar_df = pd.read_csv("oneStars.csv")
twoStars_df = pd.read_csv("twoStars.csv")
threeStars_df = pd.read_csv("threeStars.csv")

# One Side of Merge (Webscrape DF)
oneStarScrape_df = pd.read_csv("OneStarMichelinScrape.csv")
twoStarsScrape_df = pd.read_csv("TwoStarsMichelinScrape.csv")
threeStarsScrape_df = pd.read_csv("ThreeStarsMichelinScrape.csv")
# --------------- END OF IMPORT ------------------- 

# Begin Merging of Data Frames 
# One Star Merge 

# merge our data frames on matching names 
mergedOneStar = oneStar_df.merge(oneStarScrape_df, how='left', left_on="name", right_on="Restaurant Name")

# Drop unecessary columns 
mergedOneStar = mergedOneStar.drop(columns = ['year', 'zipCode', 'price', "url", "Restaurant Name"])

# Add Michelin Star column 
mergedOneStar ['michelin_stars'] = 1

# Drop duplicate rows (entire row is duplicate)
mergedOneStar = mergedOneStar.drop_duplicates()


# Get shape of dataframe 
# print (mergedOneStar.shape)
# print (mergedOneStar.info())
# print (mergedOneStar.head(10))

print ('--------------')

print (mergedOneStar[mergedOneStar.duplicated(subset = ['name'])])

print ('--------------')
print ('--------------')
# Manually intensive -- must be completed by hand as table engineering did not consists of unique id's from the webscrape
# Remove index values that we know are not the restaurants 

# Create list of unwanted index values 
oneStarIndexDrop = [52, 62, 69, 169, 190, 212, 378, 610]

# Drop the manual duplicate rows (these we have deemed to be the incorrect merge)
mergedOneStar = mergedOneStar.drop(oneStarIndexDrop)

print (mergedOneStar[mergedOneStar.duplicated(subset= ['name'])])

print (mergedOneStar.shape)
print (mergedOneStar.info())
print (mergedOneStar.head(10))

# Find our 2 nulls in city column
print (mergedOneStar[mergedOneStar['city'].isna()])


# Add our hong kong city 
mergedOneStar.loc[177, 'city'] = "Hong Kong"
mergedOneStar.loc[192, 'city'] = "Hong Kong"

print (mergedOneStar[mergedOneStar['city'].isna()])

mergedOneStar.reset_index(drop=True)

print (mergedOneStar.info())

# ----------END OF ONE STAR MERGE----------

# TWO STAR MERGE

# Merge two star data frames 
mergedTwoStars = twoStars_df.merge(twoStarsScrape_df, how='left', left_on="name", right_on="Restaurant Name")

# Drop unecessary columns 
mergedTwoStars = mergedTwoStars.drop(columns = ['year', 'zipCode', 'price', "url", "Restaurant Name"])

# Add Michelin Star column 
mergedTwoStars ['michelin_stars'] = 2

# Remove Duplicates 
mergedTwoStars = mergedTwoStars.drop_duplicates()

# Visualize Data 
# print (mergedTwoStars.shape)
# print (mergedTwoStars.info())
# print (mergedTwoStars.head(10))


# Locate Duplicates 
# print (mergedTwoStars[mergedTwoStars.duplicated(subset = ['name'])])


# Create list of unwanted index values 
# 50, 51 we need to find locations - til then, drop 
twoStarIndexDrop = [50, 51, 53, 73]


# Drop unwanted index values (rows)
mergedTwoStars = mergedTwoStars.drop(twoStarIndexDrop)

# print (mergedTwoStars.shape)
# print (mergedTwoStars.info())
# print (mergedTwoStars.head(10))

# Verify duplicate process 
mergedTwoStars = mergedTwoStars.reset_index(drop=True)
print (mergedTwoStars[mergedTwoStars.duplicated(subset = ['name'])])
print(mergedTwoStars)

# ---------END OF TWO STAR MERGE-------------

# Merge our Three Star Data Frames 
mergedThreeStars = threeStars_df.merge(threeStarsScrape_df, left_on="name", right_on="Restaurant Name")

# Drop unnecessary 
mergedThreeStars = mergedThreeStars.drop(columns = ['year', 'zipCode', 'price', "url", "Restaurant Name"])

# Add Michelin Star column
mergedThreeStars ['michelin_stars'] = 3

# Drop duplicates 
mergedThreeStars = mergedThreeStars.drop_duplicates()

# Visualize Data 
# print (mergedThreeStars.shape)
# print (mergedThreeStars.info())
# print (mergedThreeStars.head(10))

# print (mergedThreeStars[mergedThreeStars.duplicated(subset = ['name'])])

# -------------END OF THREE STAR MERGE -----------------

# Note: Nulls are in "restaruant website" column- which is ok! 
# END HERE FOR INDIVIDUAL DATA CLEAN

# Write to CSV file 
mergedOneStar.to_csv("mergedOneStar_df.csv", index= False)
mergedTwoStars.to_csv("mergedTwoStars_df.csv", index= False)
mergedThreeStars.to_csv("mergedThreeStars_df.csv", index = False)

"""# -------------COMBINE DATA FRAMES------------------
print ('-------------')
print ('-------------')
print ('-------------')
print ('-------------')
combinedMerge = mergedOneStar.append(mergedTwoStars, ignore_index= True)
combinedMerge = combinedMerge.append(mergedThreeStars, ignore_index= False)
combinedMerge.rename(columns={"Price Range": "price_range", "Restauarant Website": 'restaurant_website'}, inplace= True)
print (combinedMerge.head())


# ------------COMBINED MERGE COMPLETE -----------

#Get combined Merge into Dictionary format 
combinedMerge_dict = combinedMerge.to_dict('records')
pp.pprint (combinedMerge_dict)
"""

# Iterate through list to fix column headers 
star_df = [mergedOneStar, mergedTwoStars, mergedThreeStars]

# Fix column headers for mongoDB transfer 
for s in star_df:
    s.rename(columns={"Price Range": "price_range", "Restauarant Website": 'restaurant_website'}, inplace= True)

mergedOneStar = mergedOneStar.fillna('N/A')
mergedTwoStars = mergedTwoStars.fillna('N/A')
mergedThreeStars = mergedThreeStars.fillna('N/A')

print (mergedOneStar.head(25))


mergedOneStar_dict = mergedOneStar.to_dict('records')
pp.pprint (mergedOneStar_dict) 

mergedTwoStars_dict = mergedTwoStars.to_dict('records')
pp.pprint (mergedTwoStars_dict) 

mergedThreeStars_dict = mergedThreeStars.to_dict('records')
pp.pprint (mergedThreeStars_dict) 


print('---------------------------------------------')


# Create connection to MongoDB
client = MongoClient('localhost', 27017)
db = client['michelinStars']
collection1 = db['oneStars']
collection2 = db['twoStars']
collection3 = db['threeStars']

# Build a basic dictionary
one = mergedOneStar_dict
two = mergedTwoStars_dict
three = mergedThreeStars_dict

# Insert the dictionary into Mongo
collection1.insert(one)
collection2.insert(two)
collection3.insert(three)