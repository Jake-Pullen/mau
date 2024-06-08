
from deck import deck
#from card import card
from player import BotPlayer, HumanPlayer
from rules import Rule, RuleEngine

import time 

deck = deck()
deck.shuffle()
#deck.show()
deck.first_card()

player_count = int(input('How many players do you want to play with? '))
players = []
for i in range(player_count):
    player_name = input(f'Enter the name of player {i+1}: ')
    players.append(HumanPlayer(player_name))
    print(f'player {player_name} has been added')

bot_count = int(input('How many bots do you want to play against? '))
bots = []
for i in range(bot_count):
    bots.append(f'bot{i+1}')

players = []
# In your main game loop
players = [HumanPlayer('Jake')]  # Add other players

# Create player objects
for person in bots:
    game_player = BotPlayer(person)
    players.append(game_player)

# Now you can use your player objects
for game_player in players:
    print(f'dealing 3 cards to {game_player.name}')
    game_player.draw(deck)
    game_player.draw(deck)
    game_player.draw(deck)

# In your main game loop
rule_engine = RuleEngine()
# Load rules from JSON file
rule_engine.load_rules_from_json('rules.json')


round_counter = 0
#while True: # main game loop
for i in range(50):
    round_counter += 1
    print(f'round: {round_counter}')
    for game_player in players:
        if isinstance(game_player, HumanPlayer):
            has_played, given_command = game_player.play(deck)
        else:
            has_played, given_command = game_player.play(deck)  # Bot player's turn

        if has_played: # if the player has played a card
            if deck.discard_pile[-2].suit != deck.discard_pile[-1].suit and deck.discard_pile[-2].value != deck.discard_pile[-1].value:
                print(f'player {game_player.name} has played a wrong card')
                game_player.hand.append(deck.discard_pile.pop())
                game_player.draw(deck)
                continue
            command = rule_engine.check_rule(deck.discard_pile[-1], game_player.hand)
            print(f'{game_player.name} announced: {given_command}')
            expected_command = ' and '.join(command)
            print(f'expected command: {expected_command}')
            time.sleep(1)
            given_command_set = set(given_command.split(' and '))
            if given_command_set != command:
                print(f'{game_player.name} made the wrong announcement')
                #need to put the card back in the hand
                game_player.hand.append(deck.discard_pile.pop())
                game_player.draw(deck)
            if given_command_set == command:
                print(f'{game_player.name} announced the correct rule')
            print(f'{game_player.name} has {game_player.check_hand()} cards left\n')
            time.sleep(1)
            if game_player.check_hand() == 0: # if the player has no cards left
                print(f'{game_player.name} has won')
                print(f'rounds played: {round_counter}')
                exit()
        else:
            game_player.draw(deck) # if the player has not played a card, draw a card
            print(f'{game_player.name} drew a card')
            print(f'{game_player.name} has {game_player.check_hand()} cards left\n')
            time.sleep(1)
        if deck.check_empty(): # if the deck is empty
            deck.shuffle()
            deck.first_card()
        #game_player.draw(deck)

    print(f'discard  pile: {deck.discard_pile[-1]}')
    print(f'cards in deck: {len(deck.cards)}\n')

