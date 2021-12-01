array = ['minister', "tien", "twintig", "dertig", 'wachtwoord']


def aangegeven_element_deleten1():
    if welke in array:
        array.remove(welke)
        return array
    else:
        return "het aangegeven element komt niet in het array voor"

print(array)
print()

welke = input("welk element moet worden verijdert")
if welke in array:
    print("het oude array is")

    print(array)
    print()

    print("de aangegeven item in het array is verwijdert via manier 1")
    print("en het nieuwe array is \n")

print(aangegeven_element_deleten1())
