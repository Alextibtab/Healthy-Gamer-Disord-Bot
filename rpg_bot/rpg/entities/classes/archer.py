from ..player import Player

# Archer class
class Archer(Player):
    # Archer class constructor
    def __init__(
        self,
        name,
        level,
        health,
        mana,
        strength,
        dexterity,
        intelligence,
        luck,
        exp,
        gold,
        inventory,
    ):
        super().__init__(
            name,
            level,
            health,
            mana,
            strength,
            dexterity,
            intelligence,
            luck,
            exp,
            gold,
            inventory,
        )

        self.class_name = "Archer"
        self.class_description = (
            "A ranged class that uses bows and arrows to attack enemies."
        )

    # Archer class attack method
