"""
Created on Tue Nov 17 16:07:14 2020

Easy secret santa pairing
Takes names as command line arguments
Execution: python secretsanta.py name1 name2 ...

@author: Neil
"""

import random
import sys

def secretsanta(names):
    if (len(names) < 2):
        print("Please input 2 or more names!")
        return 0

    keys = [] # store the partner names
    targets = dict(zip(range(len(names)), names))
    for i in range(len(names)):
        tarKeys = list(targets.keys())
        randy = random.choice(tarKeys) # partner index for name i
        # by virtue of randomness, the last person has no partner choices other than themselves :(
        if (len(targets) == 1 and tarKeys[0] == i): 
            return None
        while (randy == i): # can't be your own partner!
            randy = random.choice(tarKeys)
        # if you have a partner, move on!
        keys.append(randy) 
        targets.pop(randy)
    result = dict(zip(keys, names)) # partners together forever
    for i in range(len(result)):
        print(result[i] + " is " + names[i] + "'s secret santa!")
    return 0
        

names = []
[names.append(arg) for arg in sys.argv] # collect names
santas = secretsanta(names)
while(santas is None): # until a pairing is established
    santas = secretsanta(names)