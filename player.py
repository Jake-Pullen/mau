import json 
import random


error_chance = 0.3

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

    def check_hand(self):
        return len(self.hand)

class BotPlayer(player):
    def __init__(self, name):
        super().__init__(name)

    def command(self, card):
        rules = json.load(open('rules.json'))
        commands = []
        #chance to return the wrong command
        if random.random() < error_chance:
            commands.append('wrong command')
        #print(f'generating command for {len(self.hand)} cards, {card.suit} and {card.value}')
        for rule in rules:
            if 'suit' in rule and rule['suit'] == card.suit:
                commands.append(rule['command'])
            if 'value' in rule and rule['value'] == card.value:
                commands.append(rule['command'])
            if 'card_count' in rule and rule['card_count'] == len(self.hand):
                commands.append(rule['command'])
        #print(f'Commands: {commands}')
        return ' and '.join(commands) if commands else ''
    
    def play(self, deck):
        for card in self.hand:
            if card.suit == deck.discard_pile[-1].suit or card.value == deck.discard_pile[-1].value:
                player_card = self.hand.pop(self.hand.index(card))
                deck.discard_pile.append(player_card)
                print(f'{self.name} played {player_card}')
                commands = self.command(player_card)
                #if commands is not None:
                    #print(f'{self.name} announced: {commands}')
                return True, commands
        else:
            print(f'{self.name} cannot play')
            return False, None
        

class HumanPlayer(player):
    def __init__(self, name):
        super().__init__(name)

    def play(self, deck):
        print(f'Top Card: {deck.discard_pile[-1]}')
        print(f'Your hand:')
        for i, card in enumerate(self.hand):
            print(f'{i}: {card}')
        card_index = input('Enter the index of the card you want to play(or type N to pass your go): ').lower()
        if card_index == 'n':
            return False, None
        card = self.hand.pop(int(card_index))
        deck.discard_pile.append(card)
        command = input('Enter your command: ').lower()
        return True, command
