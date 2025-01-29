

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def get_details(self):
        print(f"Room: {self.name}")
        print(f"Description: {self.description}")
