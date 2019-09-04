# Implement a class to hold room information. This should have name and
# description attributes.
# return f'Dept({repr(self.name)}, {repr(self.num)})'

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def __str__(self):
        return f"Room: {self.name}, {self.description}"

    def __repr__(self):
        return f"Room({repr(self.name)}, {repr(self.description)})"


# miniRoom = Room("House", "It's tiny")

# print(miniRoom)
# print("")
# print(repr(miniRoom))