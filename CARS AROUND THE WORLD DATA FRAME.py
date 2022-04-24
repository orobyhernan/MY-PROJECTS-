#so we have data regarding several countries and their motor vehicle statistics
#names of the countries, if those countries cars drive on the left or right and the no. of 
#cars per capita (cars per 1000 inhabitants)


names = ["United States", "Spain", "Australia", "Japan", "Germany", "India", "Russia", "Morocco", 
         "Egypt", "Eslovakia", ]
dr = [True, True, False, False, True, False, True, True, True, True]
cpc = [809, 500, 731, 588, 1200, 18, 200, 70, 45, 578]
eur_union = [False, True, False, False, True, False, False, False, False, True]

#─well seems like we ain't getting anywhere with a list like that if we want to manipulate
#values, let´s turn it into a data frame using the panda plug in.

import pandas as pd

#Now let´s create a dictiornary with the data we have from before

cars_dict = {"country": names, "drives right": dr, "cars per capita": cpc, 
             "European Union":eur_union }


#now let´s build a data frame with the cars dictionary

cars = pd.DataFrame(cars_dict)
#print(cars)


#Aalso let´s get rid of those default numbers at the left side of the data frame 
#and replace it with the country abbreviation.

row_labels = [ "US", "ES", "AUS", "JPN", "GER", "IND", "RU", "MOR", "EG", "SLV"]

cars.index = row_labels
print(cars)


















