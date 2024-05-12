import json 
import random


error_chance = 0.2

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

    def command(self, suit, value, card_count):
        rules = json.load(open('rules.json'))
        commands = []
        #chance to return the wrong command
        if random.random() < error_chance:
            commands.append('wrong command')
        print(f'generating command for {card_count} cards, {suit} and {value}')
        for rule in rules:
            if 'suit' in rule and rule['suit'] == suit:
                commands.append(rule['command'])
            if 'value' in rule and rule['value'] == value:
                commands.append(rule['command'])
            if 'card_count' in rule and rule['card_count'] == len(self.hand):
                commands.append(rule['command'])
        #print(f'Commands: {commands}')
        return ' and '.join(commands) if commands else None

    
    def play(self, deck):
        for card in self.hand:
            if card.suit == deck.discard_pile[-1].suit or card.value == deck.discard_pile[-1].value:
                player_card = self.hand.pop(self.hand.index(card))
                deck.discard_pile.append(player_card)
                print(f'{self.name} played {player_card}')
                commands = self.command(card.suit, card.value, len(self.hand))
                if commands is not None:
                   print(f'{self.name} announced: {commands}')
                return True, commands
        else:
            print(f'{self.name} cannot play')
            return False, None
        
    def check_hand(self):
        return len(self.hand)
