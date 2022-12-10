from enum import Enum

from .monster import Mob
from .player import Player


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
    def __init__(self, player: Player, mob: Mob = Mob(10, 2, 0, 1)):
        self.player = player
        self.mob = mob

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
            return ActionResult(
                Result.WIN,
                f"You killed the mob! You dealt {player_damage} damage to the mob.",
            )
