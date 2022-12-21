import numpy as np
input = open('input.txt', 'r').read().splitlines()
input = np.array([[int(el) for el in row] for row in input])
res = 0

def findNeighbourhood(row, column, data):
    neighborhoodValues = []
    neighborhoodPlaces = []
    if row != 0: 
        neighborhoodValues.append(data[row-1][column])
        neighborhoodPlaces.append((row-1, column))    
    try: 
        neighborhoodValues.append(data[row+1][column])
        neighborhoodPlaces.append((row+1, column))
    except IndexError: pass
    
    if column != 0:
        neighborhoodValues.append(data[row][column-1])
        neighborhoodPlaces.append((row, column-1))
    
    try: 
        neighborhoodValues.append(data[row][column+1])
        neighborhoodPlaces.append((row, column+1))
    except IndexError: pass
    return neighborhoodValues, neighborhoodPlaces

def isLowPoint(element, row, column, data):
    bo = True
    neighbourhoodValues, neighboorhoodPlaces = findNeighbourhood(row, column, data)
    for n in neighbourhoodValues:
        if n <= element: bo = False
    return(bo)

def basinSize(value, row, column, data): #given lowPoint, calculate basis size
    size = 1
    data[row][column] = 9 
    neighbourhoodValues, neighboorhoodPlaces = findNeighbourhood(row, column, data)
    for i, n in enumerate(neighbourhoodValues):
        if value < n and n != 9:
            if data[neighboorhoodPlaces[i][0]][neighboorhoodPlaces[i][1]] != 9:
                #print(data, size, '\n')
                size += basinSize(n, neighboorhoodPlaces[i][0], neighboorhoodPlaces[i][1], data)
    return(size)





lowPointLocations = []
for rowIndex, row in enumerate(input):
    for columnIndex, element in enumerate(row):
        if (isLowPoint(element, rowIndex, columnIndex, input)): 
            lowPointLocations.append((rowIndex, columnIndex))
            res += element+1

print(res)
#1824 is too high, 491
lstBasisSizes = []
for point in lowPointLocations:
    data = input.copy()
    lstBasisSizes.append(basinSize(data[point[0]][point[1]], point[0], point[1], data))

lstBasisSizes.sort()
print(lstBasisSizes)
# first result: 1268820 is too high, 1151400 also