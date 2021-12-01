dictionary = {}
def to_dict(string):
    keer = len(string)
    for key in string:
        value = string.count(key)
        dictionary.update({key: value})
    return dictionary

string = list(input("wat is uw string"))
print(to_dict(string))

