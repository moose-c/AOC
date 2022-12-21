#import matplotlib.pyplot as plt
raw_input = open('input.txt', 'r').read().splitlines()
input = [[[int(i) for i in el.split(',')] for el in twoCor.split(' -> ')] for twoCor in raw_input]
## input[0] = [[x1,y1], [x2,y2]], input[0][0] = [x1,y1], input[0][0][0] = x1 as integers.
grid = [[0 for i in range(1000)] for i in range(1000)]
print(input[0][0][0])

def sort(x,y):
    if x > y:
        return(y, x)
    else:
        return(x, y)

count = 0
for line in input:
    x1, y1, x2, y2 = line[0][0], line[0][1], line[1][0], line[1][1]
    if x1 == x2:
        y1, y2 = sort(y1, y2)
        for i in range(y1,y2+1): 
            grid[x1][i] += 1
            if grid[x1][i] == 2:
                count += 1
    elif y1 == y2:
        x1, x2 = sort(x1, x2)
        for i in range(x1,x2+1): 
            grid[i][y1] += 1
            if grid[i][y1] == 2:
                count += 1
    else:
        if (x1 > x2 and y1 > y2) or (x1 < x2 and y1 < y2):
            for i in range(abs(x2-x1)+1):
                x1, x2 = sort(x1,x2)
                y1, y2 = sort(y1,y2)
                grid[x1+i][y1+i] += 1
                if grid[x1+i][y1+i] == 2: count += 1
        else:
            for i in range(abs(x2-x1)+1):
                if x1 > x2: x1, x2, y1, y2 = x2, x1, y2, y1
                grid[x1+i][y1-i] += 1
                if grid[x1+i][y1-i] == 2: count += 1
print(count)
#5108 is too low
#p2,16910 too low 20347 is too high
for i in range(1,3):
    print(i)