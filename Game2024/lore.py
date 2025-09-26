import info
import items
import game

def guide():
    print(
          "\n\n-Move by typing order and direction, e.g.: 'go downstairs' or 'go west'"
          "\n-Command 'go back' doesnt work. Check your location by typing: 'current location'"
          "\n-Look up inventory or this guide by typing: 'show inventory/guide'"
          "\n-Close the game by typing: 'close'. Process is not saved."
          "\n-All commands are two or more words unless stated otherwise."
          "\n for example: 'take water bottle' or 'use paper'"
          "\n\nFind a way out, as well as a way to survive that way out.\n"
          "Watch out for the thief that has made their residence in the east.\n")

def start():
    print(f"The room around you is dark.\n"
          "The only source of light is a weak flame in an crumbling chandelier above you.\n"
          "You have no idea how you ended in here, but somehow this doesn't frighten you.\n"
          "You almost feel like home.\nAlmost.\n")
    print(f"You're at: {info.currentroom}")

def run():
    print("This is here mainly because one-word-commands were a requirement.\n"
          "I mean, there is no reason to run here. It's a peaceful place.\n"
          "Hope it was worth it.\n")

#_______________________________________________________________________________
"""
The whole lair interaction with the thief
"""
def enter_lair():
    info.areas[info.currentroom]['north'] = 'lair'
    print("\nAs you reach the bottom of the stairs, an iron "
          "frame drops from the ceiling,\n blocking your way back.\n"
          "'Hello there' a neutral voice echoed in the damp room.\n"
          "Dark shade emerged from the corner of the room.\n"
          "'If you wish to continue, GIVE me one of your items.'\n")

def leave_lair():
    info.areas[info.currentroom]['north'] = 'chasm'
    print("\n'Thank you!' the voice sounded again as "
          "figure's from disappeared into the shadows.\n")
    print("You can leave the lair now.")

def lair():
    enter_lair()
    while True:
        print("You cannot continue until you give the stranger something.")
        print(f"Your items: {items.inventory}\n")

        user_input = game.read_prompt()
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
            info.location()
        
        if verb == 'look' and object == 'around':
            describe_room()

        if verb == 'give' and object in items.inventory:
            items.delete_item(object)
            info.item_lost = True
            leave_lair()
            break
#________________________________________________________________________________
    
def describe_room():
    attack_count = 0 #see if player gets hurt
    collectible = items.collectibles()

    if info.currentroom == 'lobby':
        print("\nThere are 4 doors, one on each wall around you.\n"
          "You are facing north.")
        if not collectible:
            pass
        elif 'boots' in collectible: 
            print("You see a pair of BOOTS in one corner of the room.")
        else:
            pass
        print("There is nothing else that catches your attention.\n")
# North ===
    elif info.currentroom == 'gate':
        if info.areas[info.currentroom]['north'] == 'church':
            print("There is a gate in front of you. It is open."
                  "\nDry grass insinuates that this is near coast."
              "\nOnly ways are to north towards the church, and to south towards lobby.")
        else:
            print("There is a gate in front of you, "
              "dry grass insinuates that this is near coast.\n"
              "Only ways are to north "
              "and to south towards lobby.\n")
    elif info.currentroom == 'church':
        print("There is an old stone church in front of you to the north.\n"
              "There is dry road to the west, "
              "and way east seems to take you somewhere behind the church.\n")
    elif info.currentroom == 'graveyard':
        print("In front of you is a small sea of graves.\n"
              "Weirdy, none of them have names or dates on them.\n"
              "You cannot continue onwards from here.\n")
    elif info.currentroom == 'beach':
        print("You see a rocky beach. "
              "To the west you see a weird shape along the coastline."
              "\nOtherwise the beach is empty, barren of life.\n")
    elif info.currentroom == 'boat':
        print("You're standing in front of what seems to be a broken boat."
              "\nShame that it is not fixable. It could've been a way out.")
        if not collectible:
            pass
        elif 'rope' in collectible: 
            print("There is some ROPE near the end of the boat.\n")
        else:
            pass
        print("You can only go back towards the beach from here.")
    elif info.currentroom == 'inside the church':
        print("Church is as run down from the inside as it is from the outside.")
        if not collectible:
            pass
        elif 'map' in collectible: 
            print("At the altar you see on old paper.\n"
                  "It looks like a MAP. It shows a way out to the south!\n")
        else:
            pass
        print("There is nothing else here.\n")
# West ===
    elif info.currentroom == 'swamp':
        print("You're at the end of a swamp.\n"
              "You can continue to west, you see a bridge there. It seems to take you to\n"
              "a more lushous area. You can also turn back to east, towards the lobby.\n")
    elif info.currentroom == 'bridge':
        print("West towards the grove, or east to the swamp.\n"
              "Jumping to the swamp-water is not option.\n")
        
    elif info.currentroom == 'grove':
        print("\nGreen forest surrounds you.")
        # attack counter to make sure you can only get hurt once, 
        # and to see if player gets hurt.
        if attack_count < 1:
            if not items.inventory:
                print("You feel a stinging pain near you calf.\n"
                      "You looks down to see a small "
                      "spider or two crawling up your legs.\n"
                      "You swat them away but the damage is already done.\n"
                      "Hopefully they weren't poisonous but you're not really hopeful.\n")
                attack_count += 1
                info.status = info.heal(attack_count)

            if 'boots' in items.inventory:
                print("You look down on your legs"
                      " and see bugs crawling up your boots.\n"
                    "If you hadn't picked them up who knows "
                    "what poisonous bug might've "
                    "found their way to bite you.\n")
                attack_count += 2
                info.status = info.heal(attack_count)

            elif 'boots' not in items.inventory:
                    print("You feel a stinging pain near you calf.\n"
                          "You looks down to see a small "
                          "spider or two crawling up your legs.\n"
                          "You swat them away but the damage is already done.\n"
                          "Hopefully they weren't poisonous but you're not really hopeful.\n")
                    attack_count += 1
                    info.status = info.heal(attack_count)
        if not collectible:
            pass
        elif 'plantain' in collectible: 
            print("You see a small area of PLANTAINs near you.\n"
                  "They might be able to be used as a band-aid.\n")
        else:
            pass
        print("Only way to go to is east towards the bridge\n")
# South ===
    elif info.currentroom == 'cabin':
        print("Red, old cottage is guarding the way between"
              " southern forest and northern lobby.\n"
              "Maybe you can go inside?\n")
        
    elif info.currentroom == 'inside the cabin':
        print("The old cottage seems to be full of stuff.\n"
                  "It's more of an storage than a villa")
        if not collectible:
            pass
        elif 'bolt cutters' in collectible: 
            print("You see many tools but BOLT CUTTERS catch your attention.")
        else:
            pass
        print("There is nothing worthwhile here.\n")

    elif info.currentroom == 'forest':
        if 'map' in items.inventory:
            print("This seems to be the way out of this place,"
                    " at least according to the map you found.\n"
                  "Dark forest seems daunting.\n"
                  "You can leave by going back north or"
                  " you can end game by typing: 'enter'\n")
        elif 'map' not in items.inventory:
            print("Dark forest in front of you seems daunting.\n"
                  "You could try your luck and just start walking, see what's on the other side.\n"
                  "At your own risk.\n"
                  "You can leave by going back north or"
                  " you can end game by typing: 'enter'\n")
                
# East ===
    elif info.currentroom == 'chasm':
        print("a round hole opens up in front of you.\n"
              "A waist-length iron fence is the only thing protecting you"
              " from falling to certain death.\n"
              "Chasm has 3 exists.\nTo west, towards the lobby.\n"
              "Spiral staircase to the south.\nAnd wooden door to northern kitchen.\n")
    elif info.currentroom == 'lair':
        print('This room is cold and damp. Like a dungeon.'
              ' Only way out is to north towards the staircase.\n')
    elif info.currentroom == 'kitchen':
        print("The kitchen is fairly modern, although walls and floor give more medieval feeling.\n")
        if not collectible:
            pass
        elif 'water bottle' in collectible: 
            print("You open the fridge. It has barely any food but it has a WATER BOTTLE or two.\n"
                  "Taking one wouldn't break your back.\n")
        else:
            pass
        print("In the corner is a spiral staircase upstairs. "
              "You can go to chasm by going south or check upstairs.\n")
    elif info.currentroom == 'bedroom':
        print("Large double bed is taking up most of the room.\n")
        if not collectible:
            pass
        elif 'lockpick' in collectible:
            print("Two old looking tables are on either side of the bed.\n"
                  "On the table nearest to you lays a couple of small metal rods"
                    " that you soon realize is a LOCKPICK.")
        else:
            pass
        print("There is a balcony facing north, a nice breeze comes in from the open doors.\n"
              "You can go downstairs to the kitchen or go outside to balcony.\n")
    elif info.currentroom == 'balcony':
        print("Breeze feels nice against your face and the view is breathtaking.\n"
              "You see an old church in the distance surrounded by thick forest.\n"
              "There is nothing else of interest.\n"
              "You can only go back to bedroom, and from there downstairs to kitchen.")
        
def extras():
    if info.currentroom == 'gate':
        if info.areas[info.currentroom]['north'] == 'gate':
            print("Heavy chains hold the gate, making going forward impossible.\n"
                  "The fence is taller than you and made of material \n"
                  "that makes climbing it impossible.\n"
                  "You need to find some way to go forwards.")
    if info.currentroom == 'church':
        if info.areas[info.currentroom]['north'] == 'church':
            print("The church itself is very old, almost crumbling.\n"
                  "The front door is locked but the lock looks like it's easy to break. \n"
                  "If you happen to have the right equipment.\n")
