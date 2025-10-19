import items_and_locations as loc; 
import lore

inventory = []
currentRoom = loc.currentRoom

#====================================================================
#Take item from current room
def take_item(item):

    if item not in loc.area[loc.currentRoom]['items']:
        print('that item is not here')

    idx = loc.area[loc.currentRoom]['items'].index(item)
    poppedItem = loc.area[loc.currentRoom]['items'].pop(idx)
    inventory.append(poppedItem)

    message = {
        'map': "The map shows a way out to the south!",
        'boots': "These may offer some protection.",
        'plantain': "This might help if you get hurt.",
        'bolt cutters': "This might be of use.",
        'lockpick': "This might be of use.",
        'rope': "This might be of use.",
        'water bottle': "I might need this later."
    }
    # .get = dictionary method, fetched value of the given key
    # messages.get(key, default(if key doesnt exist))
    desc = message.get(poppedItem, 'that item is not here')
    print(f"{desc} {poppedItem} is now in your inventory.")
    
#====================================================================
#Delete item completely (lair)
def delete_item(item):
    if item in inventory:
        inventory.remove(item)
        print(f"You lost {item}\n")

#====================================================================
#leave item in current room
def leave_item(item):
    if currentRoom == 'lair':
        print("You can't leave items here.")
    else:
        idx = inventory.index(item)
        poppedItem = inventory.pop(idx)
        loc.area[loc.currentRoom]['items'].append(poppedItem)
        print(f"You dropped {poppedItem}")

#====================================================================
def use_item(item):
    if item in inventory:
        if item == 'bolt cutters' and loc.currentRoom == 'gate':
            if loc.area[loc.currentRoom]['north'] == 'gate':
                print("\nThe chains fall to the ground, withering away\n" 
                " like they never existed in the first place")
                # update area
                loc.area[loc.currentRoom]['north'] = 'church'
            else:
                print('The gate is open.')
            
        elif item == 'lockpick' and loc.currentRoom == 'church':
            if loc.area[loc.currentRoom]['north'] == 'church':
                inventory.remove(item)
                print("\nDoor lock was no match for you, it is now open.\n"
                    "Lockpick broke. It has been removed from your inventory.\n")
                # update area
                loc.area[loc.currentRoom]['north'] = 'inside the church'
                loc.area[loc.currentRoom]['inside'] = 'inside the church'

        elif item == 'plantain':
            if lore.is_hurt:
                print("You are now healed.")
                inventory.remove(item)
                lore.is_hurt = False
            else:
                print("There is no need to use this right now")
        
    else:
        print('You do not have this item.')