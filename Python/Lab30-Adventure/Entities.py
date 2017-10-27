'''

These are the different entities of the game. Living entities, players, helpers and types enemies.

'''


class Entity:
    def __init__(self, name, symbol, loc_i, loc_j):
        self.name = name
        self.symbol = symbol
        self.loc_i = loc_i
        self.loc_j = loc_j


class LivingEntity(Entity):
    def __init__(self, name, symbol, loc_i, loc_j, health, attack, defense):
        super().__init__(name, symbol, loc_i, loc_j)
        self.health = health
        self.attack = attack
        self.defense = defense
        self.inventory = []

    def calculate_attack(self):
        attack = self.attack
        for item in self.inventory:
            attack += item.attack
        return attack

    def calculate_defense(self):
        defense = self.defense
        for item in self.inventory:
            defense += item.defense
        return defense


class Corbin(LivingEntity):
    def __init__(self, loc_i, loc_j):
        super().__init__('Corbin', '⨂', loc_i, loc_j, health=10, attack=2, defense=1)


class Mangalore(LivingEntity):
    def __init__(self, loc_i, loc_j):
        super().__init__('Mangalore', 'Ⱏ', loc_i, loc_j, health=5, attack=1, defense=1)

class Leeloo(LivingEntity):
    def __init__(self, loc_i, loc_j):
        super().__init__('Leeloo', '☄', loc_i, loc_j, health=10, attack=10, defense=1)

class Police(LivingEntity):
    def __init__(self, loc_i, loc_j):
        super().__init__('Police', '✪', loc_i, loc_j, health=3)

