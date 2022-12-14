import random

from .entity import Entity

class Monster(Entity):
    # Constructor
    def __init__(self, name, health, mana, attack, defence, level, xp):
        super().__init__(name, health, mana, attack, defence, level, xp)

# Monster Varieties
class GiantRat(Monster):
    def __init__(self):
        super().__init__('Giant Rat', 10, 0, 2, 2, 1, 10)
class Goblin(Monster):
    def __init__(self):
        super().__init__('Goblin', 20, 0, 5, 2, 1, 0)

class GiantSpider(Monster):
    def __init__(self):
        super().__init__('Giant Spider', 20, 0, 5, 2, 1, 0)

class Orc(Monster):
    def __init__(self):
        super().__init__('Orc', 30, 0, 10, 5, 2, 0)

class Crocodile(Monster):
    def __init__(self):
        super().__init__('Crocodile', 30, 0, 10, 5, 2, 0)

class Wolf(Monster):
    def __init__(self):
        super().__init__('Wolf', 30, 0, 10, 5, 2, 0)

class Troll(Monster):
    def __init__(self):
        super().__init__('Troll', 40, 0, 15, 10, 3, 0)

class Dragon(Monster):
    def __init__(self):
        super().__init__('Dragon', 50, 0, 20, 15, 10, 0)

# Monster Factory
class MonsterFactory:
    def __init__(self):
        self._monster_types = {
            'giant rat': GiantRat,
            'goblin': Goblin,
            'giant spider': GiantSpider,
            'orc': Orc,
            'crocodile': Crocodile,
            'wolf': Wolf,
            'troll': Troll,
            'dragon': Dragon
        }

    def create_monster(self, monster_type):
        monster = self._monster_types.get(monster_type.lower())
        if not monster:
            raise ValueError(monster_type)
        return monster()

    def get_random_monster(self, player_level):
        _, monster_class = random.choice(list(self._monster_types.items()))
        monster = monster_class()
        while monster.level > player_level:
            _, monster_class = random.choice(list(self._monster_types.items()))
            monster = monster_class()
        return monster
