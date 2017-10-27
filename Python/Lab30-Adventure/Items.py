'''

This file covers the different items that you can find during the game. Attacking weapons, defense, and adding health.

'''

from Entities import Entity


class Item(Entity):
    def __init__(self, name, symbol, loc_i, loc_j, attack, defense):
        super().__init__(name, symbol, loc_i, loc_j)
        self.attack = attack
        self.defense = defense


class Sword(Item):
    def __init__(self, loc_i, loc_j, attack_modifier):
        super().__init__('sword', '☨', loc_i, loc_j, attack_modifier, 0)


class Shield(Item):
    def __init__(self, loc_i, loc_j, defense_modifier):
        super().__init__('sword', '☨', loc_i, loc_j, 0, defense_modifier)


class SpecialItem(Entity):
    def __init__(self, name, symbol, loc_i, loc_j, item, key_item):
        super().__init__(name, symbol, loc_i, loc_j)
        self.item = item
        self.key_item = key_item

class Key(SpecialItem):
    def __init__(self, loc_i, loc_j, regular_item):
        super().__init__('Door Key', 'k', loc_i, loc_j, regular_item, 0)

class Multipass(SpecialItem):
    def __init__(self, loc_i, loc_j, rare_item):
        super().__init__('Multipass', 'M', loc_i, loc_j, 0, rare_item)



# I want to have some treasure chests with a random item, some appearing more frequently
# than others.