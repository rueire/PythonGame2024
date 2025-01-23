import info

inventory = []

items_dict= {

        'lobby' : {'items':['boots']},

        'gate' : {'items':['']},

        'church' : {'items':['']},

        'inside the church': {'items':['map']},

        'beach' : {'items':['']},

        'boat': {'items':['rope']},

        'grove': {'items':['plantain']},

        'chasm' : {'items':['']},

        'kitchen' : {'items':['water bottle']},

        'bedroom':{'items':['lockpick']},

        'balcony' : {'items':[]},

        'cabin' : {'items':['']},

        'inside the cabin':{'items':['bolt cutters']},

        'forest':{'items': ['']},
    }

def collectibles():
    # exception happens sometimes when
    # surveying area and there is nothing to collect.
    try:
        collectible = items_dict[info.currentroom]['items']
        collectible = collectible[0]
        return collectible
    except:
        pass

#Take item from room
def take_item(item):

    # index and pop do not work when using dict.
    collectible = collectibles()
    try:
        if item in collectible:
            inventory.append(collectible)
            items_dict[info.currentroom]['items'] = []
            print(f"You took {item}")
        else:
            print("You can't take that.")
    # if item is not in dict, exception happens
    except:
        print("That item is not here.")
    

#Delete item completely
def delete_item(item):
    if item in inventory:
        inventory.remove(item)
    print(f"You lost {item}\n")

def use_item(room, item):
    # Use items to proceed
    # update dict in info.py according to player actions
    #can't use plantain if not hurt
    hurt = info.status

    if item in inventory:
        if item == 'bolt cutters' and room == 'gate':
            if info.areas[info.currentroom]['north'] == 'gate':
                print("\nThe chains fall to the ground, withering away like\n"
                  "like the rest of this world.\n")
                info.areas[info.currentroom]['north'] = 'church'
            else:
                print("The gate is open.")

        elif item == 'lockpick' and room == 'church':
            inventory.remove(item)
            print("\nDoor lock was no match for you, it is now open.\n"
                  "Lockpick broke. You can't use it anymore.\n")
            info.areas[info.currentroom]['north'] = 'inside the church'
            info.areas[info.currentroom]['inside'] = 'inside the church'
        elif item == 'plantain':
            if hurt == True:
                print("You are healed. This is good.\n")
                hurt = False
            else:
                print("There's no need to use this.")
        else:
            print("You can't use that item here.\n")
    else:
        print("You do not have that item.\n")
