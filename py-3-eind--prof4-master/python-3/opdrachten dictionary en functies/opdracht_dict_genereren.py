dictionary = {}

def dict_opvullen():
    for key in range(10):
        value = key*key
        dictionary.update({key: value})
    print(dictionary)

dict_opvullen()
