input = open('input.txt', 'r').read()
lanters = [int(el) for el in input.split(',')]
count = 0

def fishUpdate(fish):
    babys = fish.count(0)
    fish = [el-1 for el in fish]
    for i, cur in enumerate(fish):
        if cur == -1: fish[i] = 6
    for j in range(babys): fish.append(8)
    return(fish)
    


def after150days(cur):
    cur = [cur]
    for i in range(150):
        cur = fishUpdate(cur)
    return cur

add = {}
for i in range(9):
    add[i] = len(after150days(i))

print(add)

for fish in lanters:
    fish = [fish]
    for i in range(106):
        fish = fishUpdate(fish)
    for el in fish:
        count += add[el]
print(count)

#heeeeel lelijk, maar gewoon gelukt!