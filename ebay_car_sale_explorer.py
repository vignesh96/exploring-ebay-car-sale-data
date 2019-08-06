"""
Exploring EBay Car Sales Data
Author : Vignesh Ashok Kumar

"""

import numpy as np
import pandas as pd

# Read from the CSV file
autos = pd.read_csv("autos.csv", encoding="Latin-1")

# Information about the dataframe and first 5 values
autos.info()
print(autos.head())

# Change column names from Camel Case to Snake Case

autos_cols = autos.columns
print(autos_cols)

autos_cols_correction = {"dateCrawled": "date_crawled", "offerType": "offer_type", "vehicleTest": "vehicle_test",
                         "yearOfRegistration": "registration_year", "powerPS": "power_ps", "monthOfRegistration":
                         "registration_month", "fuelType": "fuel_type", "notRepairedDamage": "unrepaired_damage",
                         "dateCreated": "ad_created", "nrOfPictures": "nr_of_pictures", "postalCode": "postal_code",
                         "lastSeen": "last_seen"}

autos.rename(autos_cols_correction, axis=1, inplace=True)

print(autos.head())

print(autos.describe(include="all"))

# Remove non-numeric characters in price column
autos["price"] = autos["price"].str.replace("$", "")
autos["price"] = autos["price"].str.replace(",", "")

autos["price"] = autos["price"].astype("int64")

#print(autos["price"].describe(include="all"))
# Remove non-numeric characters and renaming column name for odometer
#print(autos["odometer"])
autos["odometer"] = autos["odometer"].str.replace("km", "")
autos["odometer"] = autos["odometer"].str.replace(",", "")

