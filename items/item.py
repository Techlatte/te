
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def get_details(self):
        return f"Item: {self.name}, Description: {self.description}"
