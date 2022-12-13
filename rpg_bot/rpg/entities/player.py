from datetime import datetime

from .entity import Entity
class Player(Entity):
    def __init__(self, id: str, name: str, hp: int, mana: int, attack: int, defence: int, gold: int, level: int, xp: int):
        super().__init__(name, hp, mana, attack, defence, level, xp)
        self.id = id
        self.max_hp = hp
        self._health = hp
        self.gold = gold
        self.items = {}
        self._last_hp_update = datetime.now()

    # Getters and setters
    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_max_hp(self):
        return self.max_hp

    def set_max_hp(self, max_hp):   
        self.max_hp = max_hp

    def get_gold(self):
        return self.gold

    def set_gold(self, gold):
        self.gold = gold

    def get_items(self):
        # if self.items empty return 'no items' string else return items
        if not self.items:
            return 'no items'
        return self.items

    def set_items(self, items):
        self.items = items

    @property
    def health(self):
        now = datetime.now()
        if self._health < self.max_hp:
            time_passed = now - self._last_hp_update
            if time_passed.total_seconds() >= 40:
                hp_change = round((time_passed.total_seconds() - 30) * 0.1)
                if hp_change + self._health > self.max_hp:
                    self._health = self.max_hp
                else:
                    self._health += hp_change
        self._last_hp_update = now
        return self._health

    @health.setter
    def health(self, value):
        self._health = value
        self._last_hp_update = datetime.now()

    # Methods
    def add_xp(self, xp: int):
        self.xp += xp
        if self.xp >= 10:
            self.level += 1
            self.xp = 0
            self.max_hp += 10
            self.attack += 2
            self.health = self.max_hp
            return True
        return False