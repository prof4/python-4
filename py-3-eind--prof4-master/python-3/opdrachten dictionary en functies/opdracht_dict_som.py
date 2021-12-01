dictionary = {10: 20, 2: 10, "som": 10 , "nog_een": 80, "boven_100":102}

def dict_som(dictionary):
    som = dictionary.values()
    eind_som = 0
    for som in  dictionary.values():
        eind_som = eind_som +som
    return eind_som

print(dict_som(dictionary))
