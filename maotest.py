#mao.py - mao online testing script
#
#
#James McPeak
#jmcpeak@gmx.com
#OCT 25, 2020
#
#

import random

deck = ['2S', '7C', 'KH', 'AC', '4C', 'Jo', '6C', '0C', '0H', 'AD', '9H', 'JC', 'AH', '0H', '6H', '6S', '8H', 'Jo', '8H', 'AD', '4C', '9C', '9D', '9C', 'JS', 'QH', '4D', '3H', 'QH', '6D', '0D', '2D', '9S', '4H', '9S', '5H', '6S', '6H', '3H', 'JS', '9H', 'QS', 'AH', 'QD', 'AS', '3S', '3C', 'QD', 'JD', '0C', '5S', 'KC', '0C', '0S', '9S', 'QD', 'Jo', 'QS', '4S', 'Jo', '0C', 'AC', '4C', '2S', '2D', '3C', '2C', '6D', '8D', '5D', 'KS', '9C', '9D', '8C', '0S', '8S', '8S', '7C', '7D', '7S', '7H', '7D', 'Jo', '0S', '5D', '6C', 'KC', '5C', 'JC', '5C', 'CWAS', 'AC', '4H', 'Jo', 'KD', '8D', 'QC', 'QC', '6C', '8C', '2C', '2C', '2H', '9D', '7S', '7H', '7H', '4S', '5S', '3D', '4D', 'JH', '2D', 'JD', 'KD', '4D', '3D', '5C', 'CWAS', '3S']
#cards are K Q J 0 9 8 7 6 5 4 3 2 A
#suits are S H D C
#suitless cards are Jo (joker), CWAS (card without a suit).
#thus a 10 of spades is 0S, a king of diamonds is KD, a 9 fo spades is 9S, etc.

current_deck = deck

player_id = 0

gameOpen = False
gameStarted = False

class Game:
    def __init__(self, cards):
        global deck
        global player_id
        player_id = 0
        self.gamedeck = deck
        self.players = []
        self.discard_pile = []
        self.draw_pile = deck
        self.cards = cards
        self.isStarted = False

    def addPlayer(self, playername):
        self.players.append(Player(playername))

    def getPlayers(self):
        for p in self.players:
            print(p.name + ", " + p.id)
        return

    def start(self):
        self.deal(self.cards)
        self.isStarted = True
        return

    def playerToDrawPile(self, pid, card):
        draw_pile.append(card)
        self.players[pid].deck.remove(card)
        self.printGame()
        return

    def playerToDiscardPile(self, pid, card):
        discard_pile.append(card)
        self.players[pid].deck.remove(card)
        self.printGame()
        return

    def drawPileToPlayer(self, pid):
        self.players[pid].deck.append(self.draw_pile[0])
        self.draw_pile.pop(0)
        self.printGame()
        return

    def discardPileToPlayer(self, pid):
        self.players[pid].deck.append(self.discard_pile[0])
        self.discard_pile.pop(0)
        self.printGame()
        return

    def deal(self, cards):
        for x in range(0,cards):
            for n in self.players:
                n.deck.append(self.draw_pile[0])
                self.draw_pile.pop(0)
        self.printGame()
        return

    def printGame(self):
        message = """"""
        message += "Top card of draw pile:"
        message += " "
        message += self.draw_pile[0]
        if not len(self.discard_pile) == 0:
            message += "\nTop card of discard pile:"
            message += self.discard_pile[0]
        for n in self.players:
            message += "\n"
            message += n.name
            message += " "
            message += str(n.deck)
            message += " "
            message += str(n.id)
            message += " "
        message += "\n"
        return message
        

class Player:
    def __init__(self, name):
        global player_id
        self.name = name
        self.id = player_id
        player_id += 1
        self.deck = []

random.shuffle(current_deck)

mao = Game(5)
mao.addPlayer("james")
mao.addPlayer("sam")
mao.addPlayer("stein")
mao.start()
print(mao.printGame())
