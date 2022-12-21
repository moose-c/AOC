input = open('../media/input.txt').read()
print(input[0])
score_lst = []
# X - lose, Y - draw, Z - win
# A X, B Z, A Y, 
#lose: 1 3, 2 1, 3 2
#win: 1 2, 2 3, 3 1

# Rock Paper Scissors
for el in input:
    result = el[2]
    opponent = ord(el[0]) + 23 - 87
    if result == 'X':
        score= (opponent-1)
        if score == 0:
            score = 3
    elif result == 'Y':
        score = opponent + 3
    else:
        score = opponent%3 + 1 + 6
    score_lst.append(score)
print(sum(score_lst))
# u 12274
# l 11215