

class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.inventory = []

    def fight(self, enemy, weapon):
        print(f"You attack the {enemy.name} with {weapon}.")
        if enemy.strength > 50:
            return False  # The player loses if the enemy is too strong
        return True  # The player wins otherwise

    def add_to_inventory(self, item):
        self.inventory.append(item)
        print(f"You picked up {item.name}.")
