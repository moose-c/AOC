lst = open('input.txt', 'r').read().splitlines()
llst = []
for line in lst:
    a,b = line.split(' contain ')
    l = [a, b]
    llst.append(l)

#shiny gold bag vinden

def Day7_1st(st = 'shiny gold', llst = llst):
    el = []
    #print(st)
    for bag in llst:
        #print(st)
        if st in bag[1]:
            el.append(bag[0])
            recbag = bag[0]
            if recbag[-1] == 's':
                recbag = recbag[:-1]
            #print(recbag)
            el += Day7_1st(recbag, llst)
    return(el)            

def find(st = 'shiny gold', lst = llst):
    for bag in lst:
        if st in bag[0]:
            return(bag)
        
def Day7_2nd(st = 'shiny gold', lst = llst):
    som = 1
    bag = find(st, lst)
    print(bag)
    lst = bag[1].split(', ')
    for el in lst:
        el = el.split(' ')
        if el[0] != 'no':
 #           som += int(el[0])
            som += int(el[0])*Day7_2nd(el[1] + ' ' + el[2])
            print(som)
        else:
            som = 1
    return(som)
        
print(Day7_2nd())

vb = [['goud geel', '4 rood geel, 3 blauw donker'], ['blauw donker', '3 wit wit, 2 groen geel'], ['wit wit', 'no'], ['rood geel', 'no'], ['groen geel', 'no']]
print(Day7_2nd('goud geel', vb))




#, ['indigo', 'vla'], 'rood','goud'], ['blauw', 'goud'], ['groen', 'blauw'], ['wit', 'blauw']]

