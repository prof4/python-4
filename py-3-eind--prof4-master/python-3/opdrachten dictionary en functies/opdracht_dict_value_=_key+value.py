dictionary = {10: 20, 2: 10, 30: 10 , 20: 80, 3:102}

def dict_som(dictionary):
    som2 = dictionary.values()
    for som1, som2 in  dictionary.items():
        eind_som = som1+som2
        dictionary.update({som1: eind_som})
    return dictionary

print(dict_som(dictionary))
