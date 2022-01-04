# CREATING a dictionary
bears_dict = {'Darnell Mooney': 80, 'Khalil Mack': 52, 'Justin Fields': 1, 
'David Montgomery': 32, 'Allen Robinson': 12, 'Andy Dalton': 14, 'Bilal Nichols': 98, 'Roquan Smith': 58,
'Eddie Jackson': 4, 'Jaylon Johnson': 33}

# ACCESSING dictionary values
bears_dict['Justin Fields'] # returns 1
bears_dict.get('Justin Fields')

# ADDING key/value pair to a dictionary
bears_dict['Nick Foles'] = 9

# CHANGING existing dictionary values
bears_dict['Darnell Mooney'] = 11 # changes his value to 11 from 80

# REMOVING dictionary entries
bears_dict.pop('Bilal Nichols')

# CHECKING if something exists in dict
if 'David Montgomery' in bears_dict:
    print('He is in')
else:
    print('He is not in')
