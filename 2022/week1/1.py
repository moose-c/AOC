text = open('../media/input.txt').read()
split_lst = [[int(nb) for nb in el.split()] for el in text.split('\n\n')]
result = [sum(el) for el in split_lst]
nb = 0
for i in range(3):
    nb += max(result)
    result.remove(max(result))
    
print(nb)
# sum_lst = []
# for el in split_lst:
#     result = sum(el.split('\n'))
#     sum_lst.append(result)
    
# sum_lst[0:5]