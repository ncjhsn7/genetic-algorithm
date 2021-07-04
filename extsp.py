from random import randrange
import math
import sys

f = open("data.txt", "r")
nCity = f.readline()
listCities = [ [ 0 for i in range(3) ] for j in range(int(nCity)) ]
i = 0

for l in f:
    l = l.split()
    j = 0
    for item in l:
        if j != 2:
            item = float(item)
        listCities[i][j] = item
        j+=1
    i+=1
nCity = int(nCity)

def mutation():
    global listCities
    n1 = (randrange(nCity))
    n2 = (randrange(nCity))
    while n2 == n1:
        n2 = (randrange(nCity))
    aux = listCities[n1]
    listCities[n1] = listCities[n2]
    listCities[n2] = aux
   

def distance(x1,x2,y1,y2):
    d = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return d

distSum = 0
distSum2 = 99999999
mutations = 0


tries = int(sys.argv[1])
for t in range(tries):
    distSum = 0
    for i in range(nCity-1):
        distSum += distance(listCities[i][0], listCities[i+1][0], listCities[i][1], listCities[i+1][1])
    distSum += distance(listCities[nCity-1][0], listCities[0][0], listCities[nCity-1][1], listCities[0][1])
    if distSum < distSum2:
        distSum2 = distSum
        l2 = listCities[:]
        mutations+=1
        print("Nova melhor distância:", distSum2) 
    else:
        listCities = l2[:]
    mutation()


print("Mutações feitas: ", mutations)
print("Melhor distância", distSum2)