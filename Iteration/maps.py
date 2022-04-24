my_list = ['I','really', 'like', 'cats.','cats','are', 'cool']

def change_list(word):
    if 'cat' in word:
        return word.replace('cat', 'ape')
    return word
    
print(" ".join(list(map(change_list,my_list))))