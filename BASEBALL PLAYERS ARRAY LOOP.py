#So here we have different data from several baseball players.The height is in inches

baseball_height = [70, 85, 74, 72, 69, 70, 74, 72, 71, 87, 66, 67, 68, 68, 69, 
            74, 75, 96, 60, 63, 73, 88, 74]

#let´s convert it into meters (m)

import numpy as np

np_height_in = np.array(baseball_height)

np_height_m = np_height_in * 0.0254

print(np_height_m)



baseball_height_weight= [[70,185],  [85, 200], [74, 186], 
                         [72,187], [69,184], [70,188],  
                         [74,189], [72,190], [71,180],
                         [87,191], [66,170], [67,171], 
                         [68,172], [68,173], [69,174], 
                         [74,178], [75,179], [96,195], 
                         [60,167], [63,165], [73,174], 
                         [88,186]]


#the weight is expressed in inches and pounds, so we have to conver that into 
#meters and kilograms, let´s call the new list np_baseball_kg_m


np_baseball = np.array(baseball_height_weight)
conversion = [0.0254, 0.453592]
np_baseball_kg_m = np_baseball * conversion

print(np_baseball_kg_m)

#now let´s calculate the bmi (body mass index) of each player using the data
#we have from the array

bmi = np_baseball_kg_m[:,1] / np_baseball_kg_m[:,0] ** 2
print(bmi)


#Now we want to calculate the average height and weight of all players and print it on the paper

av_height = np.mean(np_baseball_kg_m[:,0])
                      
av_weight = np.mean(np_baseball_kg_m[:,1])

print(f"Players have an average weight of {av_height} kg")
print(f"Players have an average height of {av_weight} m")


#Now we want to know which players are reay for battle based on their height and weight
#If their height and weight is lower than 1.75m and 75kg or higher than 1.80 and higher than 80kg
#this is a good way to practice loops with several conditions


for elem in np_baseball_kg_m:
    if elem[0] >= 1.75 and elem[1] >= 75 and elem[0] <= 1.80 and elem[1] <= 80:
        print("This player is ready for battle")
    else:
        print("This player is NOT ready for battle")

#But wait !!! What´s the point of calculating this ? Height can´t be changed, so It would make more 
#sense to find out which players are ready to play based on their bmi (body mass index)
#let´s calculate it that way. 

for elem in bmi:
    if elem >= 23.15 and elem < 26:
        print('This player is in optimal conditions to play')
    else:
        print('This player still needs improvement')





