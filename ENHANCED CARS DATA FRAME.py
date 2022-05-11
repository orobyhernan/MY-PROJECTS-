#So this time we are gonna create and improved version of the cars data frame, so we can experiment 
#and do so muchmore with our soon-to-be data frame

names = ["United States", "Spain", "Australia", "Japan", "Germany", "India", "Russia", "Morocco", 
         "Egypt", "Eslovakia", ]
dr = [True, True, False, False, True, False, True, True, True, True]
cpc = [809, 500, 731, 588, 1200, 18, 200, 70, 45, 578]
eur_union = [False, True, False, False, True, False, False, False, False, True]


#as always let´s turn our dictionary into a data frame by importing pandas library first

import pandas as pd

my_dict = {'country': names, 'drives_right': dr, 'cars_per_cap': cpc, 'belongs_to_eu': eur_union }

 

#Let´s build the data frame with the magic code

cars = pd.DataFrame(my_dict)

##also let´s get rid of those default numbers at the left side of the data frame 
#and replace it with the country abbreviation.

row_labels = [ "US", "ES", "AUS", "JPN", "GER", "IND", "RU", "MOR", "EG", "SLV"]
cars.index = row_labels

#print(cars)

#ok, let´s test your coding skill, what if your boss asks you to print the first three 
#observations from your data frame ? c'mon do it NOW !! YOU HAVE THREE SECONDS !!!

#print(cars[0:3])

#good good, that was some typing skills

#now subset only the column that belongs to cars per capita, dont't forget to print is 
#AS A DATAFRAME

cpc_column = cars[['cars_per_cap']]
#print(cpc_colum)


#and now, what if your boss asks you to print all observations that have a cars per capita
#of over 500 ? you ain't gonna select them all individually one by one right ? imaagine 
#you had millions of data, it'd take forever. 

cpc = cars["cars_per_cap"]
many_cars = cpc > 500
car_maniac = cars[many_cars]
#print(car_maniac)


#Now your boss says that they will reward with european subsidies to all those countries
#that, obviously, belong to the EU, but you have to propoerly select them. How would
#you do so ?

european_cars_only = cars['belongs_to_eu']
eu_gang = european_cars_only == True
eu_cars = cars[eu_gang]
#print(eu_cars)


#now your boss wants you to print all those countries whose cars drive in the right
#how you you make that selection ?

#well that's actually pretty easy


dr = cars['drives_right']
at_the_right = dr == True
right_driving = cars[at_the_right]
print(right_driving)













