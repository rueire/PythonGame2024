
# player's current room
currentroom = 'lobby'
# Used in game, lore, items
# hurt/not hurt
status = False
# Used in game, makes sure you can't be robbed 
# more than once at a time
item_lost = False

def heal(num):
    # 1= you get hurt; 2= you're not hurt
    # needed to specify ending
    if num <= 1:
        is_hurt = True
    elif num == 2:
        is_hurt = False
    return is_hurt

def destination():
    # for 'run' command
    directions = [*areas[currentroom].keys()]
    first_room = directions[0]
    return first_room

def move_rooms(room, direction):
    # movement script
    try:
        room = areas[room]
        newroom = room[direction]
        return newroom
    
    except:
        print("You can't go there.")


def location():
        print(f"\nYou're in: {currentroom}")
        print("You can move to:")
        for i in areas[currentroom].keys():
                print(i)
        print('')

# dict map of the game area
areas = {

#Startin point
        'lobby' : {'north': 'gate',
                       'south':'cabin', 
                       'east':'chasm', 
                       'west': 'swamp',},

# north areas
        'gate' : {'north': 'gate',  #update values in-game
                    'south':'lobby'},
    
        'church': {'east':'graveyard',
                    'south':'gate',
                    'west': 'beach',
                    'inside': 'church',
                    'north': 'church'}, #update values in-game
        'inside the church': {
                              'outside':'church',
                              'south':'church'},


        'graveyard': {'west':'church',},

        'beach': {'east':'church',
                    'west': 'boat'},

        'boat': {'east':'beach'},

# West areas
        'swamp' : {'west':'bridge',
                'east':'lobby'},

        'bridge' : {
                'west':'grove',
                'east':'swamp'},

        'grove': {'east':'bridge'},

# East areas

        'chasm' : {
                'south':'lair',
                'north':'kitchen',
                'west':'lobby',},
        
        'lair' : {'north': 'chasm'},  #update values in-game

        'kitchen':{'upstairs':'bedroom',
                'south':'chasm'},

        'bedroom':{'downstairs':'kitchen',
                   'outside': 'balcony',
                   'north':'balcony'},

        'balcony' : {'inside':'bedroom'},

# South areas

        'cabin':{'south':'forest',
                'north':'lobby',
                'inside':'inside the cabin'},

        'inside the cabin':{'outside':'cabin'},

        'forest':{'north': 'cabin'},
    }