naam_leeftijd = {}
def key_toevoegen():
    key = input("Wat is uw naam: ")
    waarde = input("Wat is uw leeftijd: ")
    naam_leeftijd.update({key:waarde})
    print(naam_leeftijd)

key_toevoegen()
