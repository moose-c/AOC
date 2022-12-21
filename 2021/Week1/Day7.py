input = open('input.txt', 'r').read().split(',')
input = [int(i) for i in input]
minVal, maxVal = min(input), max(input)
costLst = []
global sumDict 
sumDict = {}



def cost(val, data):
    lst = []
    for cur in data:
        lst.append(sumDict[abs(val - cur)])
    return sum(lst)

for i in range(minVal, maxVal+1):
    s = 0
    for j in range(i+1):
        s += j
    sumDict[i] = s

for i in range(minVal,maxVal+1):
    costLst.append(cost(i,input))

a = min(costLst)
print(a)