bears_dict = {'Darnell Mooney': 80, 'Khalil Mack': 52, 'Justin Fields': 1, 
'David Montgomery': 32, 'Allen Robinson': 12, 'Andy Dalton': 14, 'Bilal Nichols': 98, 'Roquan Smith': 58,
'Eddie Jackson': 4, 'Jaylon Johnson': 33}

# Iterating through a dictionary's KEYS
for player in bears_dict.keys():
    print(player)
    # dict.keys() returns a list of all the keys in the dictionary

# Iterating through a dictionary's VALUES
for jersey_number in bears_dict.values():
    print(jersey_number)
    # dict.values() returns a list of all the values in the dictionary

# Iterating through a dictionary's ITEMS, or a tuple of Key Value Pairs
bears_dict_low_numbers = {}
    # Add all low numbered players into new dictionary
for player, jersey_number in bears_dict.items():
    if jersey_number < 20:
        bears_dict_low_numbers[player] = jersey_number


# Iterate and REMOVE pairs
for player, jersey_number in list(bears_dict.items()):
    if jersey_number > 50:
        del bears_dict[player]
    # you need to use list() so it doesn't iterate over the dict while you're removing items
    # instead it iterates over a seperate list


