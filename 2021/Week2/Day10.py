input = open('input.txt', 'r').read().splitlines()
scoreDict = {')':3, ']':57, '}':1197, '>':25137}


def shirk(data):
    for i, b in enumerate(data):
        data[i] = data[i].replace('()', '')
        data[i] = data[i].replace('{}', '')
        data[i] = data[i].replace('[]', '')
        data[i] = data[i].replace('<>', '')
    return(data)

def calculateScore(line):
    score = 0
    otherScoreDict = {'(':1, '[':2, '{':3, '<':4}
    for char in line:
        score *= 5
        score += otherScoreDict[char]
    return(score)

shrunkInput = input.copy()
for i in range(10):
    shirk(shrunkInput)
    print(i)

finalChar = []
toRemove = []
for i, line in enumerate(shrunkInput):
    for char in line:
        if char in '}]>)':
            toRemove.append(i)
            finalChar.append(scoreDict[char])
            break
toRemove.reverse()
for el in toRemove:
    shrunkInput.pop(el)
    
print(sum(finalChar))
print(shrunkInput[0], shrunkInput[0][::-1])

score  = []
for line in shrunkInput:
    score.append(calculateScore(line[::-1]))
    
score.sort()
print(score[int((-1+len(score))/2)])