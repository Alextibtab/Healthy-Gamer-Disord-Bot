from random import randrange
from enum import Enum

from .entities.monster import Monster
from .entities.player import Player


class Result(Enum):
    CONTINUE = 0
    WIN = 1
    LOSE = 2


class ActionResult:
    def __init__(self, result: Result, message: str):
        self.result = result
        self.message = message


class Encounter:
    # Constructor
    def __init__(self, player: Player):
        self.player = player
        self.mob = Monster('Giant Rat', 10, 10, 2, 2, 1, 10)

    # Methods
    def do_player_attack(self):
        damage = self.player.do_attack()
        return self.mob.take_damage(damage), damage

    def do_mob_attack(self):
        damage = self.mob.do_attack()
        return self.player.take_damage(damage), damage

    def battle(self):
        mob_alive, player_damage = self.do_player_attack()
        if mob_alive:
            player_alive, mob_damage = self.do_mob_attack()
            if not player_alive:
                return ActionResult(
                    Result.LOSE,
                    f"You died! You dealt {player_damage} damage to the mob, but the mob dealt {mob_damage} damage to you.",
                )
            else:
                return ActionResult(
                    Result.CONTINUE,
                    f"You dealt {player_damage} damage to the mob, but the mob dealt {mob_damage} damage to you.",
                )
        else:
            self.player.add_xp(self.mob.get_xp())
            return ActionResult(
                Result.WIN,
                f"You killed the mob! You dealt {player_damage} damage to the mob.",
            )
