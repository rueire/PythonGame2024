"""
Locations, items and movement

"""
currentRoom = 'lobby'

# Movement
def move_rooms(room, direction):
    try:
        room = area[room]
        newroom = room[direction]
        return newroom
    
    except:
        print("You can't go there.")

# Inform player of current location
def location():
        print(f"\nYou're in: {currentRoom}")
        print("You can move to:")
        for i in area[currentRoom].keys():
                print(i)
        print('')

# Areas/ Rooms
area = {
    
#Startin point
        'lobby' : {'north': 'gate',
                       'south':'cabin', 
                       'east':'chasm', 
                       'west': 'swamp',
                       'items' : ['boots']
                       },

# North areas
        'gate' : {'north': 'gate',
                    'south':'lobby',
                    'items': [],
                    },
    
        'church': {'east':'graveyard',
                    'south':'gate',
                    'west': 'beach',
                    'inside': 'church',
                    'north': 'church',
                    'items':[],
                    },
        'inside the church': {
                              'outside':'church',
                              'south':'church',
                              'items':['map'],
                              },


        'graveyard': {'west':'church','items':[]},

        'beach': {'east':'church',
                    'west': 'boat',
                    'items':[]},

        'boat': {'east':'beach','items':['rope']},

# West areas
        'swamp' : {'west':'bridge',
                'east':'lobby',
                'items':[]},

        'bridge' : {
                'west':'grove',
                'east':'swamp',
                'items':[]},

        'grove': {'east':'bridge', 'items':['plantain']},

# East areas

        'chasm' : {
                'south':'lair',
                'north':'kitchen',
                'west':'lobby',
                'items':[]
                },
        
        'lair' : {'north': 'chasm', 'items':[]},

        'kitchen':{'upstairs':'bedroom',
                'south':'chasm', 
                'items':['water bottle']
                },

        'bedroom':{'downstairs':'kitchen',
                   'outside': 'balcony',
                   'north':'balcony',
                   'items':['lockpick']
                   },

        'balcony' : {'inside':'bedroom','items':[]},

# South areas

        'cabin':{'south':'forest',
                'north':'lobby',
                'inside':'inside the cabin',
                'items':[]
                },

        'inside the cabin':{'outside':'cabin', 'items':['bolt cutters']},

        'forest':{'north': 'cabin', 'items':[]},
}