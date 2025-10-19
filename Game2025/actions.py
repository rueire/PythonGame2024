import items_and_locations as loc
import lore
import inventory as inv

item_lost = False


def read_prompt():
    """
    User input is made lowercase and stripped of whitespaces
    Then it is split after first whitespace--> list

    (" ", 1) splits input at first whitespace
    """
    user_input = input('> ').lower().strip()
    return user_input.split(" ", 1)

#===============================================================
def act(action):
    """
    validating user prompt
    """
    # current_room is once step behind from info.currentroom
    currentRoom = loc.currentRoom
    end_game = False
    
    try:
        if len(action) == 1 and action[0] == '' or action[0] == ' ':
            pass
        elif action[0] == 'close' or action[0] == 'exit':
            end_game = True
        elif action[0] == 'enter':
            if currentRoom == 'forest':
                lore.ending()
                end_game = True
            else:
                pass
    except:
            print("Not possible")
            
    return end_game
#==============================================================

def validate(verb, object):
    """
    validating user prompt
    """
    global item_lost
    # check location
    if verb == 'current' and object == 'location':
        loc.location()

    #survey area
    if verb == 'look' and object == 'around':
        lore.describe_room()
    
    # user guidance
    if verb == 'show':
        if object == 'inventory':
            print(inv.inventory)
        elif object == 'guide':
            lore.guide()
    
    # Use item
    if verb == 'use' and object in inv.inventory:
        inv.use_item(object)

    # Drop item
    if verb == 'drop' and object in inv.inventory:
        inv.leave_item(object)

    # Move item to inventory when in correct room
    if verb == 'take':
        if object in loc.area[loc.currentRoom]['items']:
            inv.take_item(object)
        else:
            print("You cannot take such an item.")
    
    if verb == 'go':
        try:
            #Figure out room movement by given direction
            #And inform player where they are right now
            if object in loc.area[loc.currentRoom].keys():
                loc.currentRoom = loc.move_rooms(loc.currentRoom, object)
                print(f"\nYou're at: {loc.currentRoom}")
                
            # When in lair, you lose item (once per game)
            if loc.currentRoom == 'lair' and inv.inventory and item_lost == False:
                lore.lair()

            # Making sure player knows locked areas are actually locked
            if object == 'north' or object == 'inside':
                if loc.currentRoom == 'gate' and loc.area[loc.currentRoom]['north'] == 'gate':
                        print("\nGate is sealed with thick chains.\n"
                          "Maybe you can use something to get rid of them?")
                elif loc.currentRoom == 'church' and loc.area[loc.currentRoom]['north'] == 'church':
                        print("\nThe door to the church is locked.\n"
                              "Makes one wonder what is inside.")
            # You can only leave lair bu going north
                elif object != 'north':
                    if loc.currentRoom == 'lair':
                        print("You can only leave this place by going NORTH.")
        except:
            pass

#================================================================