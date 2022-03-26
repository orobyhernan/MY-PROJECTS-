#WARNING: ALL PRINT AND EXECUTABLE FUNCTIONS WILL BE NAMED WITH AN # IF YOU WANT TO COPY THE CODE ANT RUN IT ON YOUR
#IDE, JUST DELETE THE # AND RUN IT.
#So I am rich and I am building my new house, I decided to make a list with all
#the parts from the new house and their corresponding areas

areas = ["hallway", 11.25, "kitchen", 18.0,]

#oops !! looks like the list is incomplete, I won´t be able
# to throw parties with such a small house. Let´s add more elements with the add function

bigger_areas = areas + ["living room", 20.0, "bedroom", 10.75, "bathroom", 9.50, "attic", 14]


#oH no !!! how are we gonna throw parties with such a small living room ? plus,
#we need a cooler name for that part of the house, "chill zone" will definitely attract more people

bigger_areas[5] = 40.0
bigger_areas[4] = "Chill zone"

#in order to throw parties, there will be placards on each door, indicating
#which room has an area bigger than 15 square meters. if it´s bigger the placard will say "party friendly"
#if it´s not the placard will say "no party here"
#first of all let´s create a dictionary with the same list

bigger_areas = {"hallway": 11.25, "kitchen": 18.0, "living room": 20.0, "bedroom": 10.75, "bathroom": 9.50, "attic": 14,
                "garden": 45}

#now let´s make a loop in order to display in which rooms can we party (or not) and how much we´ll have to
#pay to party in each room, the price will vary depending on the surface

def is_party_allowed():
    for key in bigger_areas.keys():
        if bigger_areas[key] > 15 and bigger_areas[key] < 20:
           print(f"The {key} is party friendly and you´ll have to pay 40$ to party here")
        if bigger_areas[key] >= 20 and bigger_areas[key] < 30:
           print(f"The {key} is party friendly and you´ll have to pay 50$ to party here")
        if bigger_areas[key] >= 30:
           print(f"The {key} is party friendly and you´ll have to pay 60$ to party here")
        elif bigger_areas[key] < 15:
           print(f"You CANNOT party in the {key} so you won´t have to pay a dime")

print(is_party_allowed())










