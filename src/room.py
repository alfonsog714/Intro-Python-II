# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def __str__(self):
        return f"Room: {self.name}, {self.description}"

    def __repr__(self):
        return f"Room({repr(self.name)}, {repr(self.description)})"


# miniRoom = Room("test", "It's tiny")
# miniRoom.n_to = "foyer"
# print(miniRoom)
# print("")
# print(repr(miniRoom))