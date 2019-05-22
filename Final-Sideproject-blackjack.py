import random as r
import math
import numpy

deck = ["1c", "2c", "3c", "4c", "5c", "6c", "7c", "8c", "9c", "10c", "11c", "12c", "13c", "1d", "2d", "3d", "4d", "5d", "6d", "7d", "8d", "9d", "10d", "11d", "12d", "13d", "1h", "2h", "3h", "4h", "5h", "6h", "7h", "8h", "9h", "10h", "11h", "12h", "13h", "1s", "2s", "3s", "4s", "5s", "6s", "7s", "8s", "9s", "10s", "11s", "12s", "13s"]
numbers = {"1":"ace",
           "2":"two",
           "3":"three",
           "4":"four",
           "5":"five",
           "6":"six",
           "7":"seven",
           "8":"eight",
           "9":"nine",
           "10":"ten",
           "11":"jack",
           "12":"queen",
           "13":"king",
           }
suitd = {"c":"clubs",
        "d":"diamonds",
        "s":"spades",
        "h":"hearts",
        }
acetotal = 0
aiacetotal = 0
c=1
total=0
aitotal=0
aistop = 14
def inputdecksetting():
    deckmode = input("Do you want to play a game of Blackjack? y/n:")
    if deckmode == "y":
        sdmstart()
    
def aicarddrawsdm():
    global c
    global aitotal
    global deck
    global aiacetotal
    global aistop
    if aitotal < 17:
        cnum = r.randint(0,(51-c))
        card = deck[cnum]
        deck.remove(card)
        for x in card:
            if x in "cdsh":
                num = card.replace(x,'')
        aitotal = aitotal + int(num)
        #if num == 1:
        #    aiacetotal = aiacetotal + 1
        for x in card:
            if x in "1234567890":
                suit = card.replace(x,'')
        suit = suit.replace("1",'')
        #print(num + " " + suit + " " + card)
        suit = [suitd.get(n, n) for n in suit]
        suit = "".join(suit)
        num = [numbers.get(num)]
        num = "".join(num)
        print("The AI drew a " + num + " of " + suit + ".")
        print("The AI has a total of " + str(aitotal) + ".")
        c = c+1
    else:
        print("The AI did not draw a new card.")
        print("Their total is still" + aitotal)

def carddrawsdm():
    global c
    global total
    global deck
    cnum = r.randint(0,(51-c))
    card = deck[cnum]
    deck.remove(card)
    for x in card:
        if x in "cdsh":
            num = card.replace(x,'')
    total = total + int(num)
    for x in card:
        if x in "1234567890":
            suit = card.replace(x,'')
    suit = suit.replace("1",'')
    #print(num + " " + suit + " " + card)
    suit = [suitd.get(n, n) for n in suit]
    suit = "".join(suit)
    
    num = [numbers.get(num)]
    num = "".join(num)
    #print(c)
    print("You drew a " + num + " of " + suit + ".")
    c=c+1
    print("Your total is now " + str(total) + ".")
def sdmstart():
    yn = input("Do you want to draw a card? y/n :")
    if yn == "y":
        aicarddrawsdm()
        carddrawsdm()
        if total > 21:
            print("You went over 21. You lose.")
        elif aitotal > 21:
            print("The AI went over 21. You win.")
        elif total == 21 and aitotal == 21:
            print("Double Blackjack! It's a tie!")
        elif total == 21 and aitotal < 21:
            print("Blackjack! You win!")
        elif aitotal == 21 and total < 21:
            print("AI has Blackjack! You lose.")
        else:
            sdmstart()
    elif yn == "n":
        gameover()
def gameover():
    if aitotal < 14:
        aicarddrawsdm()
        gameover()
    elif aitotal > total:
        print("The AI wins.")
    elif aitotal < total and aitotal > 13 :
        print("You win.")
    elif aitotal == total:
        print("You and the AI have tied")
inputdecksetting()








