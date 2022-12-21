a, b = open('../input.txt').read().split('-')
a, b = int(a), int(b)

answers = []
for i in range(a,b):
    s = str(i)
    bo = True
    for j in range(len(s)-1):
        if int(s[j]) > int(s[j+1]):
            bo = False
            break
    if bo:
        bo = False
        for j in range(len(s)-1):
            if int(s[j]) == int(s[j+1]):
                bo = True
    if bo:
        answers.append(i)

newanswers = []
for nb in answers:
    bo = False
    s = str(nb)
    for el in set(s):
        n = s.count(el)
        if n == 2:
            newanswers.append(nb)
            break


