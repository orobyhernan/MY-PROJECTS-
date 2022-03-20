#So I am rich and I am building my new house, I decided to make a list with all
#the parts from the new house and their corresponding areas

areas = ["hallway", 11.25, "kitchen", 18.0,]

#oops !! looks like the list is incomplete, I won´t be able
# to throw parties with such a small house. Let´s add more elements with the add function

bigger_areas = areas + ["living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]


#o no !!! how are we gonna throw parties with such a small living room ? plus,
#we need a cooler name for that part of the house, "chill zone" will definitely attract more people

bigger_areas[5] = 40.0
bigger_areas[4] = "Chill zone"

#in order to throw parties, there will be placards on each door, indicating
#which room has an area bigger than 15 square meters. if it´s bigger the placard will say "party friendly"
#if it´s not the placard will say "no party here"

bigger_areas_copy = list(bigger_areas)

bigger_areas_copy[1] = "no party here"
bigger_areas_copy[3] = "party friendly"
bigger_areas_copy[5] = "party friendly"
bigger_areas_copy[7] = "no party here"
bigger_areas_copy[9] = "no party here"
print(bigger_areas_copy)
print(bigger_areas)

