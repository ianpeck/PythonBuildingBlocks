from dataclasses import dataclass, field
import random

def pick_random_item():
    item_list = ['Moonlight Greatsword', 'Rivers of Blood', 'Iron Sword', 
    'Iron Shield', 'Spiked Shield', 'Finger Shield', 'Death Poker','Scorpion Stinger','Steel Greatsword']
    return random.choice(item_list)

@dataclass
class Tarnished:
    name: str
    #init=False means you can not initlialize your own item, it must be chosen from the random list
    left_hand: str = field(init=False,default_factory=pick_random_item)
    right_hand: str =field(init=False,default_factory=pick_random_item)

you = Tarnished(name='ian')

print(you.left_hand)