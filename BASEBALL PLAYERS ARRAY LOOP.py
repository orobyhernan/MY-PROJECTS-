#So here we have different data from several baseball players.The height is in inches

baseball_height = [70, 85, 74, 72, 69, 70, 74, 72, 71, 87, 66, 67, 68, 68, 69, 
            74, 75, 96, 60, 63, 73, 88, 74]

#let´s convert it into meters (m)

import numpy as np

np_height_in = np.array(baseball_height)

np_height_m = np_height_in * 0.0254

print(np_height_m)



baseball_height_weight= [[70,185],  [85, 200], [74, 186], 
                         [72,187], [69,184], [70,188],  [74,189], [72,190], [71,180],
                         [87,191], [66,170], [67,171], [68,172], [68,173], [69,174], 
                         [74,178], [75,179], [96,195], 
                         [60,167], [63,165], [73,174], [88,186]]


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

av_height = np.median(np_baseball_kg_m[:,1])
                      
av_weight = np.median(np_baseball_kg_m[:,0])

print(f"Players have an average weight of {av_height} kg")
print(f"Players have an average height of {av_weight} m")

def baseball_ready(np_baseball_kg_m):
    for [key,key] in np_baseball_kg_m.keys:
        if np_baseball_kg_m[key,key] > [75, 180]:
            print("This player is ready for battle")
        if np_baseball_kg_m[key,key] < [75,180]:
            print("This player ain't ready for battle yet")
            
print(baseball_ready(np_baseball_kg_m))








