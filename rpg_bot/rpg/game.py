from .entities.player import Player
from .encounter import Encounter, PVP_Encounter, Result


class Game:
    # Constructor
    def __init__(self, db):
        self.players = {}
        self.encounters = {}
        self.db_client = db

    # Getters and setters
    def get_player(self, user):
        id = str(user.id)
        name = user.name
        if id in self.players.keys():
            return self.players.get(id)
        if self.load_player(id):
            return self.players.get(id)
        else:
            self.players[id] = Player(id, name, "Human", 10, 10, 2, 4, 0, 1, 0)
            self.save_player(id)
            return self.players[id]

    # Methods
    def start_encounter(self, user):
        player_id = str(user.id)
        encounter = self.encounters.get(player_id)
        if encounter is None:
            player = self.get_player(user)
            if player.is_alive():
                encounter = Encounter(player)
                self.encounters.update({player_id: encounter})
            else:
                return "You are dead and can't fight!"
        else:
            return f"""Current Status:
            Player HP: {encounter.player.health}
            Mob HP: {encounter.mob.get_health()}
            """

    def encounter_action(self, user):
        player_id = str(user.id)
        encounter = self.encounters.get(player_id)
        if encounter is None:
            new_encounter = self.start_encounter(user)
            encounter = self.encounters.get(player_id)
            if encounter is None:
                return new_encounter

        result = encounter.battle()
        if result.result != Result.CONTINUE:
            self.end_encounter(user)

        self.save_player(player_id)
        return result.message

    def end_encounter(self, user):
        player_id = str(user.id)
        encounter = self.encounters.get(player_id)
        if encounter is not None:
            self.encounters.pop(player_id)
            return "Encounter ended!"
        else:
            return "No encounter in progress!"

    def start_pvp_encounter(self, user, opponent):
        player_id = str(user.id)
        opponent_id = str(opponent.id)
        encounter = self.encounters.get(player_id)
        if encounter is None:
            player = self.get_player(user)
            opponent = self.get_player(opponent)
            if player.is_alive() and opponent.is_alive():
                encounter = PVP_Encounter(player, opponent)
                self.encounters.update({player_id: encounter})
            else:
                return "You or your opponent is dead and can't fight!"
        else:
            return f"""Current Status:
            Player HP: {encounter.player.health}
            Opponent HP: {encounter.opponent.health}
            """

    def create_player(self, user):
        pass

    def reset_player(self, user):
        id = str(user.id)
        name = user.name
        self.players[id] = Player(id, name, 10, 10, 2, 4, 0, 1, 0)
        return "Player reset!"

    def save_player(self, player_id: str):
        player = {
            "player_id": player_id,
            "name": self.players[player_id].get_name(),
            "race": self.players[player_id].get_race(),
            "max_hp": self.players[player_id].get_max_hp(),
            "health": self.players[player_id].health,
            "mana": self.players[player_id].get_mana(),
            "attack": self.players[player_id].get_attack(),
            "defence": self.players[player_id].get_defence(),
            "level": self.players[player_id].get_level(),
            "xp": self.players[player_id].get_xp(),
            "gold": self.players[player_id].get_gold(),
        }
        self.db_client.discord_rpg.players.update_one(
            {"player_id": player_id}, {"$set": player}, upsert=True
        )

    def load_player(self, player_id: str):
        player = self.db_client.discord_rpg.players.find_one({"player_id": player_id})
        if player is not None:
            self.players[player_id] = Player(
                player["player_id"],
                player["name"],
                player["race"],
                player["health"],
                player["mana"],
                player["attack"],
                player["defence"],
                player["gold"],
                player["level"],
                player["xp"],
            )
            self.players[player_id].set_max_hp(player["max_hp"])
            self.players[player_id].set_health(player["health"])
            return True
        else:
            return False
