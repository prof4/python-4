dictionary = {}

def is_empty(dictionary):
    dictionary_size = len(dictionary)
    if dictionary_size == 0:
        return True
    else:
        return False


print("Het dict is leeg: "+str(is_empty(dictionary)))
