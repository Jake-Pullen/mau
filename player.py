import json 
import random
from deck import deck
#from rules import Rule, RuleEngine


class player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        
    def draw(self, deck):
        self.hand.append(deck.cards.pop())
        return self
    
    def show_hand(self):
        for card in self.hand:
            print(card)
    
    def discard(self):
        return self.hand.pop()
    
    def command(self, card_played):
        rules = json.load(open('rules.json'))
        for rule in rules:
            if ('suit' in rule and rule['suit'] == card_played.suit) or ('value' in rule and rule['value'] == card_played.value):
                # 10% chance to return the wrong command
                if random.random() < 0.1:
                    return 'wrong command'
                else:
                    return rule['command']
        else:
            if random.random() < 0.1:
                return 'wrong command'
            else:
                return None

    
    def play(self, deck):
        for card in self.hand:
            if card.suit == deck.discard_pile[-1].suit or card.value == deck.discard_pile[-1].value:
                player_card = self.hand.pop(self.hand.index(card))
                command = self.command(player_card)
                deck.discard_pile.append(player_card)
                print(f'{self.name} played {player_card}')
                if command != None:
                    print(f'Command is {command}\n')
                return True, command
        else:
            print(f'{self.name} cannot play')
            return False, None
        
    def check_hand(self):
        return len(self.hand)
            