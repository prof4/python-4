import itertools as it 
dictionary = {1: ['a','b'], 2:['c', 'd']}

def combineren(dictionary):
    allNames = sorted(dictionary)
    combinations = it.product(*(dictionary[Name] for Name in allNames))
    print(list(combinations))

combineren(dictionary)
