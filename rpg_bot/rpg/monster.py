from random import randrange


class Mob:
    # Constructor
    def __init__(self, current_hp: int, attack: int, xp: int, level: int):
        self.current_hp = current_hp
        self.attack = attack
        self.xp = xp
        self.level = level

    # Getters and setters
    def get_current_hp(self):
        return self.current_hp

    def set_current_hp(self, current_hp: int):
        self.current_hp = current_hp

    def get_attack(self):
        return self.attack

    def set_attack(self, attack: int):
        self.attack = attack

    def get_xp(self):
        return self.xp

    def set_xp(self, xp: int):
        self.xp = xp

    def get_level(self):
        return self.level

    def set_level(self, level: int):
        self.level = level

    # Methods
    def do_attack(self):
        return self.attack + randrange(2)

    def take_damage(self, damage: int):
        self.current_hp -= damage
        return self.is_alive()

    def is_alive(self):
        return self.current_hp > 0
