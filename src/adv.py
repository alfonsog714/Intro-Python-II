from room import Room
from player import Player
from item import Item

# Functions

def whereAmI(player):
    print(f"You are at the {player.current_room.name}.\n")
    print(f"{player.current_room.description} \n")

def badPath(player):
    print(f"You're not able to move in that direction from the {player.current_room.name}.\n")

def checkIfItems(room, player):
    if len(room.items) > 0:
        print("The room has the following items:\n")
        for item in room.items:
            print(f"A {item.capitalize()}\n")

    else: 
        print("There's nothing of interest in here...\n")
        
    #     command = input("[Take 'item_name]   [Drop 'item_name']   [Leave]\n").lower()
    #     commands = command.split(" ")

    #     if len(commands) == 1 and commands[0] == "leave":
    #         print("\nYou decided to leave the items alone.\n")
        
    #     elif len(commands) == 2:
    #         if commands[0] == "take":
    #             taken_item = room.items.pop(str(commands[1]))
    #             player.items.update({str(commands[1]) : taken_item})

    #         if commands[0] == "drop":
    #             dropped_item = player.items.pop(str(commands[1]))
    #             room.items.update({str(commands[1]) : dropped_item})
                
    
    # else:
    #     print('No items')


def manipulateItems(room, player):
    command = input("[Take 'item_name]   [Drop 'item_name']   [Leave]\n").lower()
    commands = command.split(" ")
    if commands[0] == "take":
        taken_item = room.items.pop(str(commands[1]))
        player.items.update({str(commands[1]) : taken_item})
    
    elif commands[0] == "drop":
        dropped_item = player.items.pop(str(commands[1]))
        room.items.update({str(commands[1]) : dropped_item})

    else:
        print('No items.\n')
# Items

# sword = Item('Sword', 'A sword with a dull blade, looks like it could barely cut skin.')
# rock = Item("Rock", "A simple rock that's the size of the palm of your hand.")

itemList = {
    'sword': Item('Sword', 'A sword with a dull blade, looks like it could barely cut skin.'),

    'rock': Item("Rock", "A simple rock that's the size of the palm of your hand."),

    'lantern': Item('Lantern', "A lantern that's not lit.")
}

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# assign items via arrays and spread itemList into them
room["outside"].items = dict(itemList)
room['foyer'].items = {}
room['foyer'].items = {}
room['foyer'].items = {}
room['overlook'].items = {}
room['narrow'].items = {}
room['narrow'].items = {}
room['treasure'].items = {}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

player_name = ""
set_name = False

while not set_name:
    player_name = input('Please enter a name for your character:\n')

    if len(player_name) > 10:
        print("Sorry, that name is too long! 10 characters is the limit.")

    else:
        player = Player(str(player_name), room['outside'], {})
        print("Welcome to the Adventure Game!")
        print(f"Your name is {player.name}.\n")
        whereAmI(player)
        checkIfItems(player.current_room, player)
        set_name = True



# Make a new player object that is currently in the 'outside' room.
user = input("[n] Move north  [e] Move east  [s] Move south  [w] Move west   [c] Check Items \n  [q] Quit\n ").lower()



while not user == "q":
    
    if user == "n":
        print("")
        print("")
        print("You move towards the north.\n")

        if player.current_room == room["outside"]:
            player.current_room = room["outside"].n_to
            
        
        elif player.current_room == room["foyer"]:
            player.current_room = room["foyer"].n_to
        
        elif player.current_room == room["overlook"]:
            badPath(player)

        elif player.current_room == room["narrow"]:
            player.current_room = room["narrow"].n_to

        elif player.current_room == room["treasure"]:
            badPath(player)
       
    elif user == "e":
        print("")
        print("")
        print("You move towards the east. \n")

        if player.current_room == room["outside"]:
            badPath(player)
            
        
        elif player.current_room == room["foyer"]:
            player.current_room = room["foyer"].e_to
        
        elif player.current_room == room["overlook"]:
            badPath(player)

        elif player.current_room == room["narrow"]:
            badPath(player)

        elif player.current_room == room["treasure"]:
            badPath(player)

    elif user == "w":
        print("")
        print("")
        print("You move towards the west. \n")

        if player.current_room == room["outside"]:
            badPath(player)
            
        elif player.current_room == room["foyer"]:
            badPath(player)
        
        elif player.current_room == room["overlook"]:
            badPath(player)

        elif player.current_room == room["narrow"]:
            player.current_room = room["narrow"].w_to

        elif player.current_room == room["treasure"]:
            badPath(player)
        
    elif user == "s":
        print("")
        print("")
        print("You move towards the south. \n")

        if player.current_room == room["outside"]:
            badPath(player)
            
        elif player.current_room == room["foyer"]:
            player.current_room = room["foyer"].s_to
        
        elif player.current_room == room["overlook"]:
            player.current_room = room["overlook"].s_to

        elif player.current_room == room["narrow"]:
            badPath(player)

        elif player.current_room == room["treasure"]:
            player.current_room = room["treasure"].s_to

    elif user == "c":
        print("")
        print("")
        print("You look through your backpack. \n")
        if len(player.items) > 0:
            print("You see the following items: \n")
            for item in player.items:
                print(f"A {player.items[item].name} -- {player.items[item].description} \n")
        
        else:
            print('You have no items! \n')
        
        manipulateItems(player.current_room, player)
        
    else:
        print("")
        print("")
        print("Invalid input.")

    whereAmI(player)
    checkIfItems(player.current_room, player)
    print("\nPlease choose to continue...\n")
    user = input("[n] Move north  [e] Move east  [s] Move south  [w] Move west   [c] Check Items \n  [q] Quit\n ").lower()
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
