import re

file = open('Input.txt', 'r')
lines = file.readlines()

def parse_input(lines):
    parsed_input = []
    for i, line in enumerate(lines):
        # make a dictionary for every line
        line_dict = {'game': i+1, 'red':0, 'green': 0, 'blue': 0}
        altered_line = re.sub(r'[;,\n]', ' ', line)
        split_line = altered_line.split(' ')
        for j, line_element in enumerate(split_line):
            if line_element in line_dict.keys():
                line_dict[line_element] = max(line_dict[line_element], int(split_line[j-1]))
        parsed_input.append(line_dict)
    return parsed_input

games = parse_input(lines)
# only 12 red cubes, 13 green cubes, and 14 blue cubes

def part1(games):
    score = 0
    for game in games:
        if game['red'] <= 12 and game['green'] <= 13 and game['blue'] <= 14:
            score += game['game']
    print(score)

def part2(games):
    score = 0 
    for game in games:
        score+=game['red']*game['green']*game['blue']
    print(score)

part2(games)