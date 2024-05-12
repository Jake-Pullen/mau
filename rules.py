import json 

class Rule:
    def __init__(self, suit=None, value=None, command=None):
        self.suit = suit
        self.value = value
        self.command = command
        self.count = 1

class RuleEngine:
    def __init__(self):
        self.rules = []
        self.last_value = None

    def add_rule(self, rule):
        self.rules.append(rule)

    def load_rules_from_json(self, json_file):
        with open(json_file) as f:
            rules_json = json.load(f)
            for rule_json in rules_json:
                self.add_rule(Rule(**rule_json))
                print(f'Added rule: {rule_json}')

    def apply_rules(self, card):
        for rule in self.rules:
            if rule.suit == card.suit or rule.value == card.value:
                if self.last_value == card.value:
                    rule.count += 1
                else:
                    rule.count = 1
                self.last_value = card.value
                return rule.command * rule.count
        self.last_value = card.value
        return None
    
    def check_rule(self, card):
        for rule in self.rules:
            if rule.suit == card.suit or rule.value == card.value:
                return rule.command
        return None
        