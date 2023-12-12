file = open("input.txt", "r")
lines = file.read().splitlines()


def parseInput(lines):
    parsedInput = []
    for line in lines:
        parsedInput.append(
            [
                [int(number) for number in nbList.split(" ") if number.isdigit()]
                for nbList in line.split(":")[1].split("|")
            ]
        )
    return parsedInput


def part1():
    totalScore = 0
    parsedInput = parseInput(lines)
    for winningNumbers, myNumbers in parsedInput:
        cardScore = 0
        for number in myNumbers:
            if number in winningNumbers:
                cardScore = max(1, cardScore * 2)
        totalScore += cardScore
    print(totalScore)


def part2():
    multiplierArray = [1] * len(lines)
    parsedInput = parseInput(lines)
    for i, [winningNumbers, myNumbers] in enumerate(parsedInput):
        counter = 1
        for number in myNumbers:
            if number in winningNumbers:
                try:
                    multiplierArray[i + counter] += 1 * multiplierArray[i]
                    counter += 1
                except IndexError:
                    pass
    print(sum(multiplierArray))


part2()

# 4931596 too low
