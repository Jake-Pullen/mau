
from deck import deck
#from card import card
from player import player
from rules import Rule, RuleEngine

import time 

d = deck()
d.shuffle()
#d.show()
d.first_card()


people  = ['Jake','bot1','bot2','bot3','bot4','bot5']
players = []

# Create player objects
for person in people:
    game_player = player(person)
    players.append(game_player)

# Now you can use your player objects
for game_player in players:
    print(f'dealing 3 cards to {game_player.name}')
    game_player.draw(d)
    game_player.draw(d)
    game_player.draw(d)

# In your main game loop
rule_engine = RuleEngine()
# Load rules from JSON file
rule_engine.load_rules_from_json('rules.json')


round_counter = 0
#while True: # main game loop
for i in range(50):
    round_counter += 1
    print(f'round: {round_counter}')
    for game_player in players: # loop through each player
        #time.sleep(2)
        has_played,given_command = game_player.play(d) # play a card
        if has_played: # if the player has played a card
            command = rule_engine.check_rule(d.discard_pile[-1], game_player.hand)
            if given_command != command:
                print(f'{game_player.name} made the wrong announcement\n')
                game_player.draw(d)
            if given_command == command:
                print(f'{game_player.name} announced the correct rule\n')
            print(f'Player {game_player.name} has {game_player.check_hand()} cards left\n')
            if game_player.check_hand() == 0: # if the player has no cards left
                print(f'{game_player.name} has won')
                print(f'rounds played: {round_counter}')
                exit()
        else:
            game_player.draw(d) # if the player has not played a card, draw a card
            print(f'{game_player.name} has {game_player.check_hand()} cards left\n')
        if d.check_empty(): # if the deck is empty
            d.shuffle()
            d.first_card()
        #game_player.draw(d)

    print(f'discard  pile: {d.discard_pile[-1]}')
    print(f'cards in deck: {len(d.cards)}\n')

