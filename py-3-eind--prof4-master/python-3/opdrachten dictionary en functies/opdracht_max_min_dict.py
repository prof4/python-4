dictionary = {1: 10, 2: 20, 3: 30, 4:40, 5:50}

def max_van_dict(dictionary):
    max_uitkomst = max(dictionary.values())
    return "het grootste getal van het dictionary is: " + str(max_uitkomst)
def min_van_dict(dictionary):
    min_uitkomst = min(dictionary.values())
    return "het kleinste getal van het dictionary is: " + str(min_uitkomst)
def max_min_dict(dictionary):
    print(max_van_dict(dictionary))
    print(min_van_dict(dictionary))

max_min_dict(dictionary)
