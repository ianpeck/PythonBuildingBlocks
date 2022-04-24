my_dict = {'monkey': 1 , 'ape': 2, 'cat' : 3, 'dog' : 4}

def change_dict():
    global my_dict
    list_of_primates = ['ape', 'monkey', 'orang']
    for k in my_dict.keys():
        if k in list_of_primates:
            my_dict[k] += 1
        else:
            my_dict[k] -+ 1
    return my_dict
    
print(my_dict)
# Output: {'monkey': 1, 'ape': 2, 'cat': 3, 'dog': 4}

change_dict()

print(my_dict)
# Output: {'monkey': 2, 'ape': 3, 'cat': 3, 'dog': 4}

