from random import randrange


class Player:
    # Constructor
    def __init__(
        self, id: int, xp: int = 0, attack: int = 0, hp: int = 0, level: int = 0
    ):
        self.id = id
        self.xp = xp
        self.attack = attack
        self.max_hp = hp
        self.current_hp = hp
        self.level = level

    # Getters and setters
    def get_id(self):
        return self.id

    def set_id(self, id: int):
        self.id = id

    def get_xp(self):
        return self.xp

    def set_xp(self, xp: int):
        self.xp = xp

    def get_attack(self):
        return self.attack

    def set_attack(self, attack: int):
        self.attack = attack

    def get_max_hp(self):
        return self.max_hp

    def set_max_hp(self, max_hp: int):
        self.max_hp = max_hp

    def get_current_hp(self):
        return self.current_hp

    def set_current_hp(self, current_hp: int):
        self.current_hp = current_hp

    def get_level(self):
        return self.level

    def set_level(self, level: int):
        self.level = level

    # Methods
    def do_attack(self):
        return self.attack + randrange(4)

    def take_damage(self, damage: int):
        self.current_hp -= damage
        return self.is_alive()

    def is_alive(self):
        return self.current_hp > 0
