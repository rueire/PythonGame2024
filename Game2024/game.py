import info
import items
import lore

#====================================================================================

def act(action):
    """
    validating user prompt
    """
    # current_room is once step behind from info.currentroom
    current_room = info.currentroom
    end_game = False
    try:
        if len(action) == 1 and action[0] == 'run':
            lore.run()
            info.currentroom = info.move_rooms(current_room, info.destination())
            print(f"You're at: {info.currentroom}")
        elif action[0] == '' or action[0] == ' ':
            pass
        elif action[0] == 'close':
            end_game = True
        elif action[0] == 'enter':
            if info.currentroom == 'forest':
                ending()
                end_game = True
            else:
                pass
    except:
            print("Not possible")
            
    return end_game


def validate(verb, object):
    """
    validating user prompt
    """
    # current_room is once step behind from info.currentroom
    current_room = info.currentroom

    if verb == 'current' and object == 'location':
        info.location()

    #survey area
    if verb == 'look' and object == 'around':
        lore.describe_room()
        lore.extras()
    
    # user guidance
    if verb == 'show':
        if object == 'inventory':
            print(items.inventory)
        elif object == 'guide':
            lore.guide()

    # Move item to inventory when in correct room
    if verb == 'take':
        items.take_item(object)

    if verb == 'go':
        try:
            #Figure out room movement by given direction
            #And inform player where they are right now
            if object in info.areas[current_room]:
                info.currentroom = info.move_rooms(current_room, object)
                print(f"\nYou're at: {info.currentroom}")

            # Making sure player knows locked areas are actually locked
            if object == 'north' or object == 'inside':
                if current_room == 'gate' and info.areas[info.currentroom]['north'] == 'gate':
                        print("\nGate is sealed with thick chains.\n"
                          "Maybe you can use something to get rid of them?")
                elif current_room == 'church' and info.areas[info.currentroom]['north'] == 'church':
                        print("\nThe door to the church is locked.\n"
                              "Makes one wonder what is inside.")
            # You can only leave lair bu going north
                elif object != 'north':
                    if current_room == 'lair':
                        print("You can only leave this place by going north.")
            # after you leave the lair and enter chasm
            # You can lose items again in lair
            if info.currentroom == 'chasm':
                info.item_lost = False

            # When in lair, you lose item
            if info.currentroom == 'lair' and items.inventory:
                if not info.item_lost:
                    lore.lair()
        # confirmed to happen when going inside the church
        except:
            pass


    if verb == 'use':
        items.use_item(current_room, object)

#================================================================

def ending():

    counter = 0
    hurt = info.status

    if 'water bottle' in items.inventory:
        print("\nRoad was long but you had water bottle.\n")
        counter += 1
    elif 'water bottle' not in items.inventory:
        print("\nRoad was long and you didn't have anything to eat or drink.")
    if 'map' in items.inventory:
        print("\nYou might have gotten lost if not for the map, what a good find.\n")
        counter += 1
    elif 'map' not in items.inventory:
        print("\nYou had nothing to guide you through the forest.")

    if counter == 2 and hurt:
        print("\nYou had all you needed to make it out of this empty place"
              " but\n unfortunately you suffered an injury earlier.\n"
              "You succumed to your wounds before reaching the other side of the forest.")

    elif counter == 2 and not hurt:
        print("\nYou had all you needed to make it out of this empty place"
              " and\n you didn't have single scratch on you. Great!"
              "\nNow you just hope you'll never find yourself here again.")
    elif counter == 1:
        print("\nTry as you might, you didn't have all the necessities\n"
              "and you lost consciousness before reaching the end.\n"
              "At least you know the area now. Try again?")
    elif counter == 0:
        print("\nWell that could've gone better.\nYou lose consciousness before reaching halfway point,"
              " if you even made it that far.")
        
#=============================================================================

def read_prompt():
    """
    User input is made lowercase and stripped of whitespaces
    Then it is split after first whitespace--> list

    (" ", 1) splits input at first whitespace
    """
    user_input = input('> ').lower().strip()
    return user_input.split(" ", 1)