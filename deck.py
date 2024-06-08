from card import card

import random 

class deck:
    def __init__(self):
        self.cards = []
        self.build()
        self.discard_pile = []
        
    def build(self):
        for suit in ["Spades", "Hearts", "Diamonds", "Clubs"]:
            for value in range(1, 14):
                self.cards.append( card(suit=suit, value=value) )

    def show(self):
        for card in self.cards:
            print(card)

    def shuffle(self):
        if len(self.cards) > 0:
            print('grabbing the remaining cards from the deck')
            self.discard_pile.extend(self.cards)    
        print('shuffling the deck')
        self.cards = self.discard_pile
        random.shuffle(self.cards)
        self.discard_pile = []
        return self.cards
    
    def check_empty(self):
        if len(self.cards) == 0:
            return True
        else:
            return False
        
    def first_card(self):
        # adds the top deck card to the top of the discard pile
        self.discard_pile.append(self.cards.pop())
        return self
    