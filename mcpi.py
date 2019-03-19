import csv
import random

imax = int(input("How many points would like for the Monte-Carlo integration?"))
number_of_simulations = int(input("How many times would you like us to run the sim?"))

###### ask for the name of a file
name_of_file = str(input("What is the name of your file? Include .csv"))
opener=open(name_of_file , 'w')
data = []
tots = 0
with opener:
    writer = csv.writer(opener)
    for x in range (number_of_simulations):
        i = 0
        N = 0
        while i <=imax:
            x_coord = random.randint(0,1000000)
            y_coord = random.randint(0,1000000)

            if (x_coord**2 + y_coord**2)**.5 <=1000000:
                N = N+1
            i = i+1
            
        estpi = N/imax*4
        data.append(estpi)
        row = [x,estpi]
        print(estpi)
        writer.writerow(row)
for x in range(0,number_of_simulations):
    tots = data[x] + tots
print("AVERAGE=")
print(tots/number_of_simulations)
