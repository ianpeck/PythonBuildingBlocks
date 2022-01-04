bears_dict = {'Darnell Mooney': 80, 'Khalil Mack': 52, 'Justin Fields': 1, 
'David Montgomery': 32, 'Allen Robinson': 12, 'Andy Dalton': 14, 'Bilal Nichols': 98, 'Roquan Smith': 58,
'Eddie Jackson': 4, 'Jaylon Johnson': 33}

# Sort by key
print(dict(sorted(bears_dict.items(), key=lambda x:x[0])))

# Sort by value
print(dict(sorted(bears_dict.items(), key=lambda x:x[1])))
