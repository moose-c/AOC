input =  open('input.txt').read().split('\n\n')
randomNumbers, cards, cardsOriginal = input[0], input[1:], input[1:]
randomNumbers = randomNumbers.split(',') 
def singleNumberDrawn(nb, card):
    if len(nb) == 2 and nb in card:
        card = card.replace(nb, ' x')
    elif len(nb) == 1 and nb in card:
        card = card.replace(' ' + nb + ' ', ' x ')
        card = card.replace(' ' + nb + '\n', ' x\n')
        try: 
            if int(card[len(card)-2:]) == int(nb): card = card[:len(card)-2] + ' x'
        except: pass
            ## hier zit nog een klein probleem.
    return(card)

def hasBingo(card):
    if ' x  x  x  x  x' in card:
        return(True)
    else:
        ## first row has length 13
        for i in range(14):
            if card[i] == 'x' and card[i+15] == 'x' and card[i+30] == 'x' and card[i+45] == 'x' and card[i+60] == 'x':
                return(True)
    return(False)

def sumUnmarked(card):
    print(card)
    list1 = card.split('\n')
    cardList = []
    for el in list1: cardList += el.split(' ')
    sum = 0
    for el in cardList:
        try: sum += int(el)
        except: pass
    return(sum)

# for nb in randomNumbers:
#     bo = False
#     for card in cards:
#         newCard = singleNumberDrawn(nb, card)
#         cards[cards.index(card)] = newCard
#         if hasBingo(newCard):
#             finalCardChanged = newCard
#             finalCardOriginal = cardsOriginal[cards.index(newCard)]
#             finalEntry = int(nb)
#             bo = True
#             break
#     if bo:
#         break
    


test = ''' 3 17  3  2  5
13 87  x 74  x
 x 21  x 98  x
 x 51  x 84  x
 x 75 16 41  x
 '''

for nb in randomNumbers:
    cardsToRemove = []
    for card in cards:
        newCard = singleNumberDrawn(nb, card)
        if hasBingo(newCard):
            finalCardChanged = newCard
            finalEntry = int(nb)
            cardsToRemove.append(card)
        else:
            cards[cards.index(card)] = newCard
    #cardsToRemove.reverse()
    for card in cardsToRemove: 
        cards.remove(card)
    

print(sumUnmarked(finalCardChanged)*finalEntry)
print(finalEntry)
# 5394 is too low, 16605 is too high
##!! Mistake! Concurrent list operation, removen uit een lijst terwijl je erover itereert -> ellende.