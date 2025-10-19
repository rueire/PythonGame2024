import actions
import items_and_locations as loc; 
import inventory as inv

currentRoom = loc.currentRoom
attack_count = 0
is_hurt = False

# Game guidance
def guide():
    print(
          "\n\n-Move by typing order and direction, e.g.: 'go downstairs' or 'go west'"
          "\n-Check your location by typing: 'current location'"
          "\n-Look up inventory or this guide by typing: 'show inventory/guide'"
          "\n -Use items by 'use item', leave them behind in the room by 'drop item'."
          "\n For example: use knife or drop mug\n"
          "\n-Close the game by typing: 'close'. Process is not saved."
          "\n-All commands are two or more words unless stated otherwise."
          "\n for example: 'take water bottle' or 'use paper'"
          "\n\nFind a way out, as well as a way to survive that way out.\n"
          "Watch out for the thief that has made their residence in the east.\n")

# Beginning of the game
def start():
    print(f"The room around you is dark.\n"
          "The only source of light is a weak flame in an crumbling chandelier above you.\n"
          "You have no idea how you ended in here, but somehow this doesn't frighten you.\n"
          "You almost feel like home.\nAlmost.\n")
    print(f"You're at: {currentRoom}")


# Found items description
def items_in_room(item):
        if len(item) == 0:
            return "There is nothing else that catches your attention.\n"
        elif len(item) == 1:
            return f"You see {item} nearby.\n"
        else:
            return f"You see {', '.join(item[:-1])} and {item[-1]} in the room.\n"
    
#====================================================================
#the lair

def enter_lair():
    loc.area[loc.currentRoom]['north'] = 'lair'
    print("\nAs you reach the bottom of the stairs, an iron "
          "frame drops from the ceiling,\n blocking your way back.\n"
          "'Hello there' a neutral voice echoed in the damp room.\n"
          "Dark shade emerged from the corner of the room.\n"
          "'If you wish to continue, GIVE me one of your items.'\n")

def leave_lair():
    #loc.area[loc.currentRoom]['north'] = 'chasm'
    print("\n'Thank you!' the voice sounded again as "
          "figure disappeares into the shadows.\n")
    print("You can leave the lair now.")



def lair():
    global item_lost
    enter_lair()
    while True:
        print("You cannot continue until you GIVE the stranger something.")
        print(f"Your items: {inv.inventory}\n")

        user_input = actions.read_prompt()
        length = len(user_input)

        if length == 1:
            if user_input == 'close':
                print("You can't close game here.")
                continue
            else:
                print("You can't do that here.")
                continue
        if length == 2:
            verb = user_input[0]
            object = user_input[1]

        if verb == 'show' and object == 'guide':
            guide()
        
        if verb == 'current' and object == 'location':
            loc.location()
        
        if verb == 'look' and object == 'around':
            describe_room()

        if verb == 'give' and object in inv.inventory:
            inv.delete_item(object)
            item_lost = True
            leave_lair()
            break

#===============================================================================
# Room description
# Havent found a way to add to locations as desc w/out starting from scratch
def describe_room():
    global attack_count, is_hurt
    items = loc.area[loc.currentRoom]['items']

# Start
    if loc.currentRoom == 'lobby':
        print("\nThere are 4 doors, one on each main compass point: NORTH, WEST, EAST and SOUTH.\n")
        items = loc.area[loc.currentRoom]['items']
        print(items_in_room(items))

# North
    elif loc.currentRoom == 'gate':
        if loc.area[loc.currentRoom]['north'] == 'church':
            print("There is a gate in front of you. It is open."
                  "\nDry grass insinuates that this is near coast."
              "\nOnly ways are to NORTH towards the church, and to SOUTH towards lobby.")
        elif loc.area[loc.currentRoom]['north'] == 'gate':
            print("\nHeavy chains hold the gate, making going forward impossible.\n"
                  "The fence is taller than you and made of material \n"
                  "that makes climbing it impossible.\n"
                  "You need to find some way to go forwards.\n"
                  "\nDry grass insinuates that this is near coast.\n"
                  "Only ways are to NORTH beyond the gate "
                  "and to SOUTH towards lobby.\n") 
        items = loc.area[loc.currentRoom]['items']
        print(items_in_room(items))

    elif loc.currentRoom == 'church':
        print("There is an old stone church in front of you to the NORTH.\n"
              "There is dry road to the WEST, "
              "and way EAST seems to take you somewhere behind the church.\n")
        if loc.area[loc.currentRoom]['north'] != 'inside the church':
            print("\nThe church itself is very old, almost crumbling.\n"
                  "The front door is locked but the lock looks like it's easy to break. \n"
                  "IF you happen to have the right equipment.\n")
            items = loc.area[loc.currentRoom]['items']
            print(items_in_room(items))

    elif loc.currentRoom == 'graveyard':
        print("In front of you is a small sea of graves.\n"
              "Weirdy, none of them have names or dates on them.\n"
              "You cannot continue onwards from here.\n")
        items = loc.area[loc.currentRoom]['items']
        print(items_in_room(items))

    elif loc.currentRoom == 'beach':
        print("You see a rocky beach. "
              "To the WEST you see a weird shape along the coastline, to the EAST the church."
              "\nOtherwise the beach is empty, barren of life.\n")
        items = loc.area[loc.currentRoom]['items']
        print(items_in_room(items))

    elif loc.currentRoom == 'boat':
        print("You're standing in front of what seems to be a broken boat."
              "\nShame that it is not fixable. It could've been a way out.")
        items = loc.area[loc.currentRoom]['items']
        print(items_in_room(items))
        print("Only way to go is back EAST.")

    elif loc.currentRoom == 'inside the church':
        print("Church is as run down from the inside as it is from the outside.")
        items = loc.area[loc.currentRoom]['items']
        print(items_in_room(items))
        print("Only way to go is back OUTSIDE.")

# East
    elif loc.currentRoom == 'chasm':
        print("a round hole opens up in front of you.\n"
              "A waist-length iron fence is the only thing protecting you"
              " from falling to certain death.\n"
              "Chasm has 3 exists.\nTo WEST, towards the lobby.\n"
              "Spiral staircase to the SOUTH,\n and wooden door to NORTHERN kitchen.\n")
        items = loc.area[loc.currentRoom]['items']
        print(items_in_room(items))

    elif loc.currentRoom == 'lair':
        print('This room is cold and damp. Like a dungeon.'
              ' Only way out is to NORTH towards the staircase.\n')
        
    elif loc.currentRoom == 'kitchen':
        print("The kitchen is fairly modern, although walls and floor give more medieval feeling.\n")
        print("In the corner is a spiral staircase upstairs. "
              "You can go to chasm by going SOUTH or check UPSTAIRS.\n")
        items = loc.area[loc.currentRoom]['items']
        print(items_in_room(items))


    elif loc.currentRoom == 'bedroom':
        print("Large double-sized bed is taking up most of the room.\n"
              "Two old looking tables are on either side of the bed and "
              "there is a balcony facing north, a nice breeze comes in from the open doors.\n"
              "You can go DOWNSTAIRS to the kitchen or go OUTSIDE to balcony")
        items = loc.area[loc.currentRoom]['items']
        print(items_in_room(items))

    elif loc.currentRoom == 'balcony':
        print("Breeze feels nice against your face and the view is breathtaking.\n"
              "You see an old church in the distance surrounded by thick forest.\n"
              "There is nothing else of interest.\n"
              "You can only go BACK to bedroom, and from there DOWNSTAIRS to kitchen.")
        items = loc.area[loc.currentRoom]['items']
        print(items_in_room(items))
    
# South 
    elif loc.currentRoom == 'cabin':
        print("Red, old cottage is guarding the way between"
              " SOUTHERN forest and NORTHERN lobby.\n"
              "Maybe you can go INSIDE?\n")
        items = loc.area[loc.currentRoom]['items']
        print(items_in_room(items))
        
    elif loc.currentRoom == 'inside the cabin':
        print("The old cottage seems to be full of stuff.\n"
                  "It's more of an storage than a villa. You can go back OUTSIDE.")
        items = loc.area[loc.currentRoom]['items']
        print(items_in_room(items))

    elif loc.currentRoom == 'forest':
        if 'map' in inv.inventory:
            print("This seems to be the way out of this place,"
                    " at least according to the map you found.\n"
                  "Dark forest seems daunting.\n"
                  "You can leave by going back north or"
                  " you can end game by typing: 'enter'\n")
        elif 'map' not in inv.inventory:
            print("Dark forest in front of you seems daunting.\n"
                  "You could try your luck and just start walking, see what's on the other side"
                  " at your own risk.\n"
                  "You can leave by going back NORTH or"
                  " you can end game by typing: 'ENTER'\n")

# West 
    elif loc.currentRoom == 'swamp':
        print("You're at the end of a swamp.\n"
              "You can continue to WEST, you see a bridge there. It seems to take you to\n"
              "a more lushous area. You can also turn back to EAST, towards the lobby.\n") 
        items = loc.area[loc.currentRoom]['items']
        print(items_in_room(items))
    elif  loc.currentRoom == 'bridge':
        print("WEST towards the grove, or EAST to the swamp.\n"
              "Jumping to the swamp-water is not option.\n")
        items = loc.area[loc.currentRoom]['items']
        print(items_in_room(items))

    elif loc.currentRoom == 'grove':
        print("\nGreen forest surrounds you.")
        items = loc.area[loc.currentRoom]['items']
        print(items_in_room(items))
        # attack counter to make sure you can only get hurt once, 
        # and to see if player gets hurt.
        if attack_count < 1:
            if 'boots' not in inv.inventory:
                print("You feel a stinging pain near you calf.\n"
                      "You looks down to see a small "
                      "spider or two crawling up your legs.\n"
                      "You swat them away but the damage is already done.\n"
                      "Hopefully they weren't poisonous but you're not really hopeful.\n")
                attack_count += 1
                is_hurt = True

            if 'boots' in inv.inventory:
                print("You look down on your legs"
                      " and see bugs crawling up your boots.\n"
                    "If you hadn't picked them up who knows "
                    "what poisonous bug might've "
                    "found their way to bite you.\n")
                attack_count += 2
                is_hurt = False
        print("Only way to go to is EAST towards the bridge\n")

#=====================================================================
def ending():
    counter = 0

    if 'water bottle' in inv.inventory:
        print("\nRoad was long but you had water bottle.\n")
        counter += 1
    elif 'water bottle' not in inv.inventory:
        print("\nRoad was long and you didn't have anything to eat or drink.")
    if 'map' in inv.inventory:
        print("\nYou might have gotten lost if not for the map, what a good find.\n")
        counter += 1
    elif 'map' not in inv.inventory:
        print("\nYou had nothing to guide you through the forest.")

    if counter == 2 and is_hurt:
        print("\nYou had all you needed to make it out of this empty place"
              " but\n unfortunately you suffered an injury earlier.\n"
              "You succumed to your wounds before reaching the other side of the forest.")

    elif counter == 2 and not is_hurt:
        print("\nYou had all you needed to make it out of this empty place"
              " and\n you didn't have single scratch on you. Great!"
              "\nNow you just hope you'll never find yourself here again.")
    elif counter == 1:
        print("\nTry as you might, you didn't have all the necessities\n"
              "and you lost consciousness before reaching the end.\n"
              "At least you know the area now. 1/2 necessary items found. Try again?")
    elif counter == 0:
        print("\nWell that could've gone better.\nYou lose consciousness before reaching halfway point,"
              " if you even made it that far. 0/2 necessary items found.")
        
#=======================================================================