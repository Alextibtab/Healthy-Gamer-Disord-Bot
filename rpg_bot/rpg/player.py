from random import randrange
from datetime import datetime


class Player:
    # Constructor
    def __init__(
        self, id: int, xp: int = 0, attack: int = 0, hp: int = 0, level: int = 0
    ):
        self.id = id
        self.xp = xp
        self.attack = attack
        self.max_hp = hp
        self._current_hp = hp
        self._last_hp_update = datetime.now()
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

    def get_level(self):
        return self.level

    def set_level(self, level: int):
        self.level = level

    # Methods
    @property
    def current_hp(self):
        now = datetime.now()
        if self._current_hp < self.max_hp:
            time_passed = now - self._last_hp_update
            if time_passed.total_seconds() >= 40:
                hp_change = round((time_passed.total_seconds() - 30) * 0.1)
                if hp_change + self._current_hp > self.max_hp:
                    self._current_hp = self.max_hp
                else:
                    self._current_hp += hp_change
        self._last_hp_update = now
        return self._current_hp

    def do_attack(self):
        return self.attack + randrange(4)

    def take_damage(self, damage: int):
        self._current_hp -= damage
        if self.current_hp < 0:
            self._current_hp = 0
        self._last_hp_update = datetime.now()
        return self.is_alive()

    def is_alive(self):
        return self.current_hp > 0
