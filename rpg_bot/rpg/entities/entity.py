# Entity Class
class Entity:
    # Constructor
    def __init__(self, name, health, mana, attack, defence, level, xp):
        self.name = name
        self.health = health
        self.mana = mana
        self.attack = attack
        self.defence = defence
        self.level = level
        self.xp = xp

    # Getters and setters
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_health(self):
        return self.health

    def set_health(self, health):
        self.health = health

    def get_mana(self):
        return self.mana

    def set_mana(self, mana):
        self.mana = mana

    def get_attack(self):
        return self.attack

    def set_attack(self, attack):
        self.attack = attack

    def get_defence(self):
        return self.defence

    def set_defence(self, defence):
        self.defence = defence

    def get_level(self):
        return self.level

    def set_level(self, level):
        self.level = level

    def get_xp(self):
        return self.xp

    def set_xp(self, xp):
        self.xp = xp

    # Methods
    def take_damage(self, damage):
        self.health -= damage
        return self.is_alive()

    def is_alive(self):
        return self.health > 0

    def do_attack(self):
        return self.attack

    def add_xp(self, xp):
        self.xp += xp
