# Import Dependencies 
import pandas as pd

airports_df = pd.read_csv("airportDataset.csv")


airports_df.columns = ['ICAO_Code', 'IATA_Code', 'Airport_Name', 'City_Town', 'Country', 'Latitude_Degrees', 'Latitude_Minutes', 'Latitude_Seconds', 'Latitude_Direction', 'Longitude_Direction', 'Longitude_Degrees', 'Longitude_Seconds', 'Longitude_Direction', 'Altitude', 'Latitude_Decimal_Degrees', 'Longitude_Decimal_Degrees']

# Get information and shape on the data frame
airports_df.head()
airports_df.info()
airports_df.shape


# Remove Unwanted Columns 
# IATA Code is what US utilizes however does not create international unique ID 
# ICAO is the proper code to use for internation uniqueness for the airport 
airports_df = airports_df.drop(columns = ['IATA_Code','Latitude_Degrees', 'Latitude_Minutes', 'Latitude_Seconds', 'Latitude_Direction', 'Longitude_Direction', 'Longitude_Degrees', 'Longitude_Seconds', 'Longitude_Direction', 'Altitude'])

# Get information on updated data frame
airports_df.shape
print (airports_df.info())
print (airports_df.head())


# Check for Airports that have no Airport Name
# ASSUMPTION: If the airport does not have a name, we will deem it insignificant for International Travel 
print (airports_df[airports_df['Airport_Name'].isna()])


# Remove rows with no airport names 
airports_df = airports_df[airports_df['Airport_Name'].notna()]

# Check data frame
airports_df.shape
print (airports_df.info())
print (airports_df.head())


# Check for lat / long combo where we have 0.000 in both 
# No Country will have an airport at that location 
print (airports_df[(airports_df['Latitude_Decimal_Degrees'] == 0.000) & (airports_df['Longitude_Decimal_Degrees'] == 0.000)])

# Drop our 0.000 rows as we won't be able to utilize their proper locations
airports_df.drop(airports_df[(airports_df['Latitude_Decimal_Degrees'] == 0.000) & (airports_df['Longitude_Decimal_Degrees'] == 0.000)].index, inplace=True)


# Verify dropped actions 
airports_df.shape
print (airports_df.info())
print (airports_df.head())

# Data frame completed 
# -------------------------------------

# Write to csv File 
airports_df.to_csv('airports_df.csv', index=False)