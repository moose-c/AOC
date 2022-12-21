lst = open('input.txt','r').read().split('\n\n')

def Day6_1st():
    res = 0
    for group in lst:
        union = set()
        pers = group.split('\n')
        for p in pers:
            union = union.union(p)
        res += len(union)
    return(res)
        
def Day6_2nd():
    res = 0
    for group in lst:
        intersection = set('abcdefghijklmnopqrstuvwxyz')
        pers = group.split('\n')
        for p in pers:
            intersection = intersection.intersection(p)
        res += len(intersection)
    return(res)
print(Day6_1st())
print(Day6_2nd())
