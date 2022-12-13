from .player import Player
from .encounter import Encounter, Result


class Game:
    # Constructor
    def __init__(self, db):
        self.players = {}
        self.encounters = {}
        self.db_client = db

    # Getters and setters
    def get_player(self, id: str):
        if id in self.players.keys():
            return self.players.get(id)
        if self.load_player(id):
            return self.players.get(id)
        else:
            self.players[id] = Player(id, 0, 2, 10, 1)
            self.save_player(id)
            return self.players[id]

    # Methods
    def start_encounter(self, player_id: str):
        encounter = self.encounters.get(player_id)
        if encounter is None:
            player = self.get_player(player_id)
            if player.is_alive():
                encounter = Encounter(player)
                self.encounters.update({player_id: encounter})
            else:
                return "You are dead and can't fight!"
        else:
            return f"""Current Status:
            Player HP: {encounter.player.current_hp}
            Mob HP: {encounter.mob.get_current_hp()}
            """

    def encounter_action(self, player_id: str):
        encounter = self.encounters.get(player_id)
        if encounter is None:
            new_encounter = self.start_encounter(player_id)
            encounter = self.encounters.get(player_id)
            if encounter is None:
                return new_encounter

        result = encounter.battle()
        if result.result != Result.CONTINUE:
            self.end_encounter(player_id)

        self.save_player(player_id)
        return result.message

    def end_encounter(self, player_id: str):
        encounter = self.encounters.get(player_id)
        if encounter is not None:
            self.encounters.pop(player_id)
            return "Encounter ended!"
        else:
            return "No encounter in progress!"

    def reset_player(self, player_id: str):
        self.players[player_id] = Player(player_id, 0, 2, 10, 1)
        return "Player reset!"

    def save_player(self, player_id: str):
        player = {
            "player_id": player_id,
            "xp": self.players[player_id].xp,
            "level": self.players[player_id].level,
            "current_hp": self.players[player_id].current_hp,
            "max_hp": self.players[player_id].max_hp,
            "attack": self.players[player_id].attack,
        }
        self.db_client.discord_rpg.players.update_one(
            {"player_id": player_id}, {"$set": player}, upsert=True
        )

    def load_player(self, player_id: str):
        player = self.db_client.discord_rpg.players.find_one({"player_id": player_id})
        if player is not None:
            self.players[player_id] = Player(
                player["player_id"],
                player["xp"],
                player["attack"],
                player["max_hp"],
                player["level"],
            )
            self.players[player_id]._current_hp = player["current_hp"]
            return True
        else:
            return False
