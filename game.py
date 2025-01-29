
from characters.player import Player
from characters.enemy import Enemy
from rooms.room import Room
from items.item import Item


def main():
    # Create rooms
    kitchen = Room("Kitchen", "A dimly lit kitchen with a rusty sink.")
    living_room = Room("Living Room", "A cozy room with a fireplace.")
    kitchen.connect_rooms("south", living_room)
    living_room.connect_rooms("north", kitchen)

    # Create player
    player = Player("Hero", 100)

    # Create enemy
    goblin = Enemy("Goblin", "A small, sneaky creature.", 50)
    kitchen.add_inhabitant(goblin)

    # Game loop
    current_room = kitchen
    while True:
        print("\n")
        current_room.get_details()

        command = input("> ").lower()
        if command in ["north", "south", "east", "west"]:
            next_room = current_room.move(command)
            if next_room:
                current_room = next_room
            else:
                print("You can't go that way!")
        elif command == "talk":
            if current_room.inhabitant:
                current_room.inhabitant.interact()
            else:
                print("There's no one here to talk to.")
        elif command == "fight":
            if current_room.inhabitant:
                weapon = input("What will you fight with? > ")
                if player.fight(current_room.inhabitant, weapon):
                    print(f"You defeated the {current_room.inhabitant.name}!")
                    current_room.inhabitant = None
                else:
                    print("You lost the fight. Game Over!")
                    break
            else:
                print("There's no one here to fight.")
        elif command == "exit":
            print("Goodbye!")
            break
        else:
            print("Invalid command. Try 'north', 'south', 'talk', 'fight', or 'exit'.")


if __name__ == "__main__":
    main()
