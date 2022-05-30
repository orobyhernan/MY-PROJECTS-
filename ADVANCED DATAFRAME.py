#THE ADVANCED DATA FRAME

#So this time we are going to loop over certain data from our cars data frame
#first let´s re-build our data frame from scratch (cause we need to keep practicing 
#how to build data frames.... right ? )



names = ["United States", "Spain", "Australia", "Japan", "Germany", "India", "Russia",
         "Morocco", "Egypt", "Slovakia"]

dr = [True, True, False, False, True, False, False, True, True, True]

cpc = [809, 400, 731, 588, 1200, 18, 200, 70, 45, 478]

eur_union = [False, True, False, False, True, False, False, False, False, True]

eligible = [False, True, False, False, True, False, False, False, False, True]

#aight aight let´s create the bloody dataframe, but first of all, it´s dictionary time
#(again)

import pandas as pd

cars_dict = {"country": names, "drives right": dr, "cars per capita": cpc,
             "European Union": eur_union, "Elligible for EU money": eligible }


cars = pd.DataFrame(cars_dict)

row_labels = [ "US", "ES", "AUS", "JPN", "GER", "IND", "RU", "MOR", "EG", "SLV"]

cars.index = row_labels

#print(cars)

#Our boss is now asking to print all the countries that belong to the European Union
#and those that don't propoerly classified. Let´s do it. 

for car, row in cars.iterrows():
    if row["European Union"] == False:
     print(car + " doesn't belong to the European Union")
    else:
     print(car + " belongs to the European Union")
     
     
#Now our boss ias asking us to print all the countries that belong to the EU 
#and if they are eliggible to European Union subsidies. Of course, those that will 
#be can only be the ones who are "True" on the eligible variable

for car, row in cars.iterrows():
    if row["European Union"] == False:
        print(car + " doesn't belong to the European Union and is NOT eligible for EU money")
    else:
        print(car + " belongs to the EU and IS elligible for EU money ")

#Now the European Union is giving subsidies to all European countries that 
#have less than 500 cars per capita to help them pump those numbers up
#and our boss wants to know which European countries are eligible for that. 



for car, row in cars.iterrows():
    if row["European Union"] == False:
        print(car + " doesn't belong to the European Union and is NOT eligible for EU money")
    if row["European Union"] == True and row["cars per capita"] < 500:
        print(car + " belongs to the European Union and IS elligible for EU money")
    if row["European Union"] == True and row["cars per capita"] > 500:
        print(car + " belongs to the EU and is NOT elligible for EU money")
    


    
        



















      

