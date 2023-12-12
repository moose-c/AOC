file = open("input.txt")
seeds, *information = file.read().split("\n\n")

infDict = {
    "".join(el[0] for el in info.split("-")): info.split("\n")[1:]
    for info in information
}


def performRule(rule, pairs):
    dest, start, offset = [int(split) for split in rule.split(" ")]
    newPairs = pairs[:]
    for pair in pairs:
        if pair[2]:
            somethingHappened = False
            if pair[0] < start:
                if pair[1] >= start:
                    somethingHappened = True
                    newPairs.append([pair[0], start - 1, False])
                    if pair[1] < start + offset:
                        newPairs.append([dest, pair[1] - start + dest, False])
                    else:
                        newPairs.append([dest, dest + offset - 1, False])
                        newPairs.append([start + offset, pair[1], False])
            elif pair[0] < start + offset:
                somethingHappened = True
                if pair[1] < start + offset:
                    newPairs.append(
                        [pair[0] - start + dest, pair[1] - start + dest, False]
                    )
                else:
                    newPairs.append([pair[0] - start + dest, dest + offset - 1, False])
                    newPairs.append([start + offset, pair[1], False])
            if somethingHappened:
                newPairs.remove(pair)
    return newPairs


def part1(seeds):
    seeds = [int(el) for el in seeds.split(" ") if el.isdigit()]

    lowestLoc = 10000000000000000
    for seed in seeds:
        nb = seed
        for key in infDict.keys():
            for rule in infDict[key]:
                dest, start, offset = [int(split) for split in rule.split(" ")]
                if start <= nb < start + offset:
                    nb += dest - start
                    break

        lowestLoc = min(nb, lowestLoc)

    print(lowestLoc)
    # correct: 403695602


def part2(seeds):
    seeds = [int(el) for el in seeds.split(" ") if el.isdigit()]
    seedPairs = [
        [seeds[2 * i], seeds[2 * i] + seeds[2 * i + 1] - 1]
        for i in range(int(len(seeds) / 2))
    ]
    print(seedPairs)
    for key in infDict.keys():
        seedPairs = [[pair[0], pair[1], True] for pair in seedPairs]
        for rule in infDict[key]:
            seedPairs = performRule(rule, seedPairs)

    minArray = [pair[0] for pair in seedPairs]
    print(min(minArray))


part2(seeds)

# 96143715 too low
