lst = open('input.txt', 'r').read().splitlines()

def Day3_1st():
    ans = 0
    posx = 0
    for line in lst:
        if line[posx] == "#":
            ans += 1
        posx += 3
        posx %= len(line)
    print(ans)
    return

def Day3_2nd():
    ans1, ans2, ans3, ans4, ans5 = 0, 0, 0, 0, 0 #hoe kan dit compacter?
    posx1, posx2, posx3, posx4, posx5 = 0, 0, 0, 0, 0
    posy = 0
    for line in lst:
        if line[posx1] == "#":
            ans1 += 1
        if line[posx2] == "#":
            ans2 += 1
        if line[posx3] == "#":
            ans3 += 1
        if line[posx4] == "#":
            ans4 += 1
        if posy%2 == 0:
            if line[int(posx5)] == "#":
                ans5 += 1
        posx1 += 1
        posx2 += 3
        posx3 += 5
        posx4 += 7
        posx5 += 1/2
        posx1 %= len(line)
        posx2 %= len(line)
        posx3 %= len(line)
        posx4 %= len(line)
        posx5 %= len(line) # hoe kan dit compacter? (werkt ook uberhaubt niet zo)
        posy += 1
    print(ans1, ans2, ans3, ans4, ans5)
    print(ans1*ans2*ans3*ans4*ans5)
    return
        
