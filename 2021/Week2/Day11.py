import numpy as np
from numpy.core.numeric import count_nonzero
input = open('input.txt', 'r').read().splitlines()
input = np.array([[int(i) for i in line] for line in input])
hor = np.array([[-10000 for i in range(len(input))]])
ver = np.array([-10000 for i in range(len(input)+2)])
ver = np.transpose([ver])
input = np.concatenate((hor, input, hor))
input = np.concatenate((ver, input, ver), 1)
count = 0

def neighborhood(row, col):
    return [(row-1, col), (row+1, col), (row, col-1), (row, col+1), (row-1, col-1), (row-1, col+1), (row+1, col-1), (row+1, col+1)]



def singleStep(data):
    count0 = 0
    data += 1
    while(9 < max(np.nditer(data))):
        for index, value in np.ndenumerate(data):
                if value > 9:
                    global count
                    count += 1
                    data[index] = -20000
                    for pos in neighborhood(index[0], index[1]):
                        data[pos] += 1
                    count0 += 1

    for index, value in np.ndenumerate(data):
        if value < -10000:
            data[index] = 0
    return(count0)


print(input)
steps = 0
while(True):
    count0 = singleStep(input)
    steps += 1
    if count0 == 100:
        break

print(steps)