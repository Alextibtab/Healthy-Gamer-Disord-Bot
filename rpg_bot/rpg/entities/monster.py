from .entity import Entity

class Monster(Entity):
    # Constructor
    def __init__(self, name, health, mana, attack, defence, level, xp):
        super().__init__(name, health, mana, attack, defence, level, xp)