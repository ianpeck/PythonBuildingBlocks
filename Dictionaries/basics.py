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

# CREATING a dictionary from TWO LISTS
bears_recievers_names = ['Darnell Mooney', 'Allen Robinson', 'Damiere Byrd', 'Marquise Goodwin', 'Dazz Newsome', 'Jakeem Grant']
bears_recievers_numbers = [11,12,10,84,83,17]
bears_recievers_dict = dict(zip(bears_recievers_names,bears_recievers_numbers)) # zip() creates a list of tuples

# CREATING a dictionary from a LIST OF TUPLES
bears_running_backs_list = [('David Montgomery', 32),('Tarik Cohen', 29),('Khalil Herbert', 24),('Damien Williams', 8)]
bears_running_backs_dict = dict(bears_running_backs_list) # very simple, just use dict() on a list of tuples