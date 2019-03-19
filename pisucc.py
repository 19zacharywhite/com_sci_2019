import math
import random
import csv
succ = 0
dingle = 0
total = 0
point_total = int(input("How many points"))
data = []
def badboi():
    global dingle
    succ=0
    for x in range(0,point_total):
        xc = random.randint(0,1000000)
        yc = random.randint(0,1000000)
        if ((yc**2 + xc**2)**.5) <= 1000000:
            succ = succ + 1
    piapprox = succ/point_total * 4
    print(piapprox)
    data.append(piapprox)
    dingle = dingle + 1
    if dingle < 100:
        badboi()
badboi()
print(data)
for x in range(0,100):
    total = total + data[x]
    finapprox = total/100
print(finapprox)
    
