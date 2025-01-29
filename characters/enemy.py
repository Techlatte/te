

class Enemy:
    def __init__(self, name, description, strength):
        self.name = name
        self.description = description
        self.strength = strength

    def interact(self):
        print(f"The {self.name} growls: '{self.description}'")
