import json 

class Rule:
    def __init__(self, suit=None, value=None, command=None, card_count=99):
        self.suit = suit
        self.value = value
        self.command = command
        self.card_count = card_count
        self.count = 1

class RuleEngine:
    def __init__(self):
        self.rules = []
        self.last_value = None
        self.card_count = 99

    def add_rule(self, rule):
        self.rules.append(rule)

    def load_rules_from_json(self, json_file):
        with open(json_file) as f:
            rules_json = json.load(f)
            for rule_json in rules_json:
                self.add_rule(Rule(**rule_json))
                print(f'Added rule: {rule_json}')
    
    def check_rule(self, card, hand):
        commands = []
        for game_rule in self.rules:
            if (game_rule.suit is not None and game_rule.suit == card.suit) or \
               (game_rule.value is not None and game_rule.value == card.value) or \
               (game_rule.card_count != 99 and game_rule.card_count == len(hand)):
                commands.append(game_rule.command)
        return ' and '.join(commands) if commands else None
        