# Ryan Hubbuck - IT-140 Project 2
# Function to print instructions to play the game
def show_instructions():
    print('-' * 20)
    print('A captain on a deep-space voyage, you awaken in the barracks to a loud explosion.')
    print('With the alarm blaring, the ship A.I. tells you there is an alien in the hanger!')
    print('Collect all 6 items before facing the alien to kill the invader and win the game.')
    print("Move commands: go South, go North, go East, go West")
    print("Add to Inventory: get 'item name'")
    print("Exit the game command: Exit")
    print('You are in the Barracks')
    print('-' * 20)


def main():
    # Set dictionary of rooms
    rooms = {
            'Barracks': {'North': 'Infirmary', 'West': 'Engineering Room', 'South': 'Navigation Room', 'East': 'Armory'},
            'Engineering Room': {'East': 'Barracks'},
            'Navigation Room': {'North': 'Barracks', 'East': 'Security Room'},
            'Security Room': {'West': 'Navigation Room'},
            'Armory': {'West': 'Barracks', 'North': 'Hanger'},
            'Hanger': {'South': 'Armory'},
            'Infirmary': {'South': 'Barracks', 'East': "Captain's Room"},
            "Captain's Room": {'West': 'Infirmary'}
        }

    # Set dictionary of items for each room
    items = {
            'Barracks': 0,
            'Engineering Room': 'Helmet',
            'Navigation Room': 'Data Tablet',
            'Security Room': 'Security Key',
            'Armory': 'Blaster',
            'Hanger': 0,
            'Infirmary': 'Space Suit',
            "Captain's Room": 'Ammo Belt'
    }

    # Declare empty inventory list
    inventory = []

    # Function to print instructions to play the game
    # def show_instructions():
    #     print('-' * 20)
    #     print('A captain on a deep-space voyage, you awaken in the barracks to a loud explosion.')
    #     print('With the alarm blaring, the ship A.I. tells you there is an alien in the hanger!')
    #     print('Collect all 6 items before facing the alien to kill the invader and win the game.')
    #     print("Move commands: go South, go North, go East, go West")
    #     print("Add to Inventory: get 'item name'")
    #     print("Exit the game command: Exit")
    #     print('You are in the Barracks')
    #     print('-' * 20)

    # Function to display current room, current item if there is an item and the item is not
    # in player inventory, and the current inventory
    def show_status():
        print('You are in the {}'.format(current_room))
        if current_item not in inventory and current_item != 0:
            print('You see a {}'.format(current_item))
        print('Inventory: {}'.format(inventory))
        print('-' * 20)

    show_instructions()

    # Set the current room to Barracks to begin the game
    current_room = 'Barracks'

    # Declare current item variable to use in each room
    current_item = ''

    # Get initial user input
    user_int = input('Enter your move:')

    # As long as user does not enter the hanger (where the alien is)
    while current_room != 'Hanger' and current_room != 'Exit':
        # Split user input and get the last word as direction to go
        split_string = user_int.split()
        user_direction = split_string[-1]
        # If user enters "go" as command to move, get the options available to move as value for that room's key
        if split_string[0] == 'go':
            room_options = rooms.get(current_room, 0)
            # Validate to see if the direction entered is an option
            if user_direction not in room_options.keys():
                print('Cannot go that way.')
                show_status()
            # If that direction is an option, set current room to the value for that direction (key)
            # and set current item to the value for the key associated with that room
            elif user_direction in room_options.keys():
                for key, value in room_options.items():
                    if user_direction == key:
                        current_room = value
                        current_item = items.get(current_room, 0)
                        show_status()

            # Get new user input action as long as they are not in the Hanger
            if current_room != 'Hanger':
                user_int = input('Enter your move:')
        # If the user enters "get" as command, the word(s) entered after "get" will be the user input item they
        # are trying to get. Use join() to make the list a string
        elif split_string[0] == 'get':
            user_item_input = split_string[1:]
            user_item_join = ' '.join(user_item_input)
            # If the user entered an item that is in the room, and the item is not in their inventory,
            # add that item to their inventory and get their next move
            if user_item_join == current_item and current_item not in inventory:
                inventory.append(current_item)
                print('You got the {}.'.format(current_item))
                show_status()
                user_int = input('Enter your move:')
            # If they enter the correct item for the room, but they already have it,
            # tell them and get their next move. Do not add to inventory.
            elif user_item_join == current_item and current_item in inventory:
                print('You already have the {}.'.format(current_item))
                show_status()
                user_int = input('Enter your move:')
            # If user enters a word or item that is not in the room, tell them and get next input
            else:
                print('Invalid item.')
                show_status()
                user_int = input('Enter your move:')
        # If the user enters Exit, exit the game
        elif split_string[0] == 'Exit':
            current_room = 'Exit'
        # If user enters any other command besides "go" or "get" tell them it is not valid and get new input
        else:
            print('Invalid input.')
            show_status()
            user_int = input('Enter your move:')
    # If user is in the hanger or exit
    else:
        # If the current room is exit, the game will exit. If not, the current room is hanger and
        # the game will be won or lost depending on having all items
        if current_room == 'Exit':
            print('Thank you for playing -- Hope you had fun!')
        else:
            # If the player has less than all 6 items, they lose the game
            if len(inventory) < 6:
                print('You see the alien!')
                print("You don't have everything you need!")
                print("The alien sees you and fires his beam rifle!")
                print("You have died and the ship is lost :(")
                print('Thank you for playing -- Hope you had fun!')
            # If the player has all 6 items, they win the game
            else:
                print('You see the alien invader!')
                print('While trying to cut through a blast-door, he does not notice you approaching.')
                print('Fully equipped to face the enemy, you take cover and set your sights.')
                print("You fire your blaster and it's a hit!")
                print("The enemy is defeated and you've saved the ship!")
                print('Thank you for playing -- Hope you had fun!')


# Call the main game function
main()
