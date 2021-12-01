array =  ["length", "bit depht", "custom"]

def item_toevoeger(array, wat):
    array.insert(1, wat)
    return array

wat = input("wat moet worden toegevoegd: ")
print(item_toevoeger(array, wat))
