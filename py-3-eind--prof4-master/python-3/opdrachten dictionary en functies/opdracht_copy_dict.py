
dictionary = {1: 10, 2: 20, 3: 30, 4:40, 5:50}

def copy_van_dict(dictionary):
    copy_dict = dictionary.copy()
    return "het gekopieerde dict is: " + str(copy_dict)
print("Het originele dict is: " + str(dictionary))
print(copy_van_dict(dictionary))
