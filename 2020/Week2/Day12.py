import numpy as np
lst = open('input.txt').read().splitlines()
#lst = ['F10', 'N3', 'F7', 'R90', 'F11']

class Ship():

    def __init__(self, sN = 0, sE = 0, wN = 1, wE = 10, ang = 90):
        self.sN = sN
        self.sE = sE
        self.wN = wN
        self.wE = wE

    def move(self, inp):
        if inp[0] == 'N':
            self.wN += int(inp[1:])
        elif inp[0] == 'S':
            self.wN -= int(inp[1:])
        elif inp[0] == 'E':
            self.wE += int(inp[1:])
        elif inp[0] == 'W':
            self.wE -= int(inp[1:])
        #print(self.wN, self.wE)

    def rot(self, inp):
        deg = int(inp[1:])
        if inp[0] == 'L':
            deg = 360 - int(inp[1:])
        x = self.wN
        y = self.wE
        if deg == 90:
            self.wN = -y
            self.wE = x
        elif deg == 180:
            self.wN = -x
            self.wE = -y
        elif deg == 270:
            self.wN = y
            self.wE = -x
        else:
            print(deg)
        #print(self.wN, self.wE)

    def forward(self, inp):
        m = int(inp[1:])
        self.sN += m*self.wN
        self.sE += m*self.wE
    
    def pos(self):
        return(self.sN, self.sE)

def Day12_1st_2nd():
    ship = Ship()
    dlst = 'NESW'
    clst = 'LR'
    for inp in lst:
        if inp[0] in dlst:
            ship.move(inp)
        elif inp[0] in clst:
            ship.rot(inp)
        elif inp[0] == 'F':
            ship.forward(inp)
    N, E = ship.pos()
    return(N, E)

    

N, E = Day12_1st_2nd()
print(abs(N) + abs(E))
        
#6745 is too low
#55652 is too high

    
        
                     
