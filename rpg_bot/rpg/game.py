from .player import Player
from .encounter import Encounter, Result


class Game:
    # Constructor
    def __init__(self):
        self.players = {}
        self.encounters = {}

    # Getters and setters
    def get_player(self, id: int):
        player = self.players.get(id)
        if player is not None:
            return player
        else:
            self.players[id] = Player(id, 0, 2, 10, 1)
            return self.players[id]

    # Methods
    def start_encounter(self, player_id: int):
        encounter = self.encounters.get(player_id)
        if encounter is None:
            player = self.get_player(player_id)
            encounter = Encounter(player)
            self.encounters.update({player_id: encounter})
            print(f"Encounter started! ID: {player_id}")

    def encounter_action(self, player_id: int):
        encounter = self.encounters.get(player_id)
        if encounter is None:
            self.start_encounter(player_id)
            encounter = self.encounters.get(player_id)

        result = encounter.battle()
        if result.result != Result.CONTINUE:
            self.end_encounter(player_id)

        return result.message

    def end_encounter(self, player_id: int):
        encounter = self.encounters.get(player_id)
        if encounter is not None:
            self.encounters.pop(player_id)
            print(f"Encounter ended! ID: {player_id}")
            return "Encounter ended!"
        else:
            return "No encounter in progress!"
