import pandas
import math
import numpy as np

epsilon = 10**(-6)

def isOne(x):
   return (x + epsilon >= 1.)

N = 6
Data = 'Add'+str(N)+'.csv'
def rate(k):
    return math.log(k,2)/N

df = pandas.read_csv(Data)
results = df.values

# PLOT
data = [[0. for k2 in range(2**N)] for k1 in range(2**N)]

for res in results:
    data[int(res[0])-1][int(res[1])-1] = res[2]
 
print(data)

def findStart():
    y = 0
    while(y < len(data) and isOne(data[0][y])):
        y+=1
    return y-1
    
x = 0
y = findStart()
result = [(x,y)]
while(x < len(data)-1):
    x+=1
    while(not(isOne(data[x][y]))):
       y-=1
    if y < 0: break
    while(isOne(data[x][y])):
       x+=1
       if x >= len(data): break
    x-=1 
    result.append((x,y))
print(result)

import csv
with open('ZEBorder'+str(N)+'.csv', 'w') as outcsv:   
    #configure writer to write standard csv file
    writer = csv.writer(outcsv, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
    writer.writerow(['R1','R2'])
    for (k1,k2) in result:
        R1 = rate(k1+1)
        R2 = rate(k2+1)
        writer.writerow([R1, R2])
