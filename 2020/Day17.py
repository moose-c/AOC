import numpy as np
import copy
raw_input = open('input.txt').read().splitlines()
initialstate = [[char for char in line] for line in raw_input]
dimension_dictionary = {0:initialstate}

#data processing is getest en klaar.
def surround_w_dots(data):
    for i, col in enumerate(data):
        data[i] = ['.'] + col + ['.']
    data = [['.']*len(data[0])] + data + [['.']*len(data[0])]
    return(data)
def ready_for_next_iteration(data):
    new_data = copy.deepcopy(data)
    for dimension in data.keys():
        new_data[dimension] = surround_w_dots(data[dimension])
    empty_array = [['.' for i in range(len(new_data[0][0]))] for j in range(len(new_data[0]))]
    new_data[min(data.keys())-1] = empty_array
    new_data[max(data.keys())+1] = empty_array
    return(new_data)


def count_surrounding(x,y,z, data):
    count = -1
    for zi in range(3):
        zi -= 1
        for xi in range(3):
            xi -= 1
            for yi in range(3):
                yi -= 1
                row = x + xi
                col = y + yi
                if row < len(data[z+zi]):
                    if col < len(data[z+zi][row]):
                        if data[z+zi][row][col] == '#':
                            count += 1
    return(count)

def Day17_1st(original_data):
    data = ready_for_next_iteration(original_data)
    new_data = copy.deepcopy(data)
    for z in original_data.keys():
        print(z)
        for x in range(len(data[z])-2):
            x += 1
            for y in range(len(data[z][x])-2):
                y += 1
                if new_data[z][x][y] == '#':
                    if count_surrounding(x,y,z, data) == 2 or count_surrounding(x,y,z, data) == 3: pass
                    else: new_data[z][x][y] = '.'
                elif new_data[z][x][y] == '.':
                    if count_surrounding(x,y,z, data) == 3: new_data[z][x][y] = '#'
    return(new_data)                        

def count_cubes(data):
    count = 0
    for dim in data.keys():
        for x in range(len(data[dim])):
            for y in data[dim][x]:
                if y == '#':
                    count += 1
    return(count)




for d in dimension_dictionary.values():
    print(np.array(d))
#dimension_dictionary = ready_for_next_iteration(dimension_dictionary)

data = dimension_dictionary
for i in range(5):
    new_dim = Day17_1st(data)
    print(np.array(new_dim[0]))
    data = new_dim
print(count_cubes(data))
#print(np.array(surround_w_dots(initialstate)))
