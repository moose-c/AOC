file = open('input.txt')
lines = file.readlines()

def computeNeighbours(location):
    # Return neighbours. Not necisarily 0, and can be a \n char.
    neighbours = []
    for i in range(-1,2):
        for j in range(-1,2):
            if i + j in [1,-1]:
                try:
                    row = location[1]+i
                    col = location[2]+j
                    neighbours.append([lines[row][col], row, col])
                except IndexError: 
                    pass
    return(neighbours)

def isConnected(oldLoc, newLoc):
    if newLoc[0] == '|':
        return(oldLoc[1] in [newLoc[1]+1, newLoc[1]-1])
    elif newLoc[0] == '-':
        return(oldLoc[2] in [newLoc[2]+1, newLoc[2]-1])
    elif newLoc[0] == 'L':
        return([oldLoc[1], oldLoc[2]] in [[newLoc[1]-1, newLoc[2]], [newLoc[1], newLoc[2]+1]])
    elif newLoc[0] == 'J':
        return([oldLoc[1], oldLoc[2]] in [[newLoc[1]-1, newLoc[2]], [newLoc[1], newLoc[2]-1]])
    elif newLoc[0] == '7':
        return([oldLoc[1], oldLoc[2]] in [[newLoc[1]+1, newLoc[2]], [newLoc[1], newLoc[2]-1]])
    elif newLoc[0] == 'F':
        return([oldLoc[1], oldLoc[2]] in [[newLoc[1]+1, newLoc[2]], [newLoc[1], newLoc[2]+1]])

def traverse(oldLoc, currentLoc):
    # Create new location and value based on old location and current location
    if currentLoc[0] == '|':
        if oldLoc[1] == currentLoc[1]+1:
            return [lines[currentLoc[1]-1][currentLoc[2]], currentLoc[1]-1, currentLoc[2]]
        elif oldLoc[1] == currentLoc[1]-1:
            return [lines[currentLoc[1]+1][currentLoc[2]], currentLoc[1]+1, currentLoc[2]]

        

    newLoc = ['val', 'row', 'col']
    return newLoc

for row, line in enumerate(lines):
    for col, char in enumerate(line):
        if char == 'S':
            sLocation = ['S', row, col]
            break


neighbours = computeNeighbours(sLocation)

for neighbour in neighbours:
    if neighbour[0] not in ['.', '\n']:
        if isConnected(sLocation, neighbour):
            print(neighbour)
            # works, now something that does this again, until value start to decrease or something
