import matplotlib.pyplot as plt
a,b = open('../input.txt').read().splitlines()
a, b = a.split(','), b.split(',')


def plotline(lst):
    posx = 0
    posy = 0 
    t = 0
    Coordinates = [(posx, posy, t)]
    for el in lst:
        mv = int(el[1:])
        if el[0] == 'R':
            for i in range(mv):
                Coordinates.append((posx + (i+1), posy, t + i + 1))
            posx += mv
        elif el[0] == 'L':
            for i in range(mv):
                Coordinates.append((posx - (i+1), posy, t + i + 1))
            posx -= mv
        elif el[0] == 'U':
            for i in range(mv):
                Coordinates.append((posx, posy + (i+1), t + i + 1))
            posy += mv
        elif el[0] == 'D':
            for i in range(mv):
                Coordinates.append((posx, posy - (i+1), t + i + 1))
            posy -= mv
        t += mv 
    return(Coordinates)

lst_a = plotline(a)
lst_b = plotline(b)

coordinates_a, coordinates_b = [(tup[0],tup[1]) for tup in lst_a], [(tup[0],tup[1]) for tup in lst_b]

inters = list(set(coordinates_a) & set(coordinates_b))

inter_a, inter_b = [], []
for point in inters:
    ia, ib = coordinates_a.index(point), coordinates_b.index(point)
    inter_a.append(lst_a[ia]), inter_b.append(lst_b[ib])

end_lst = [inter_a[i][2] + inter_b[i][2] for i in range(len(inters))]




