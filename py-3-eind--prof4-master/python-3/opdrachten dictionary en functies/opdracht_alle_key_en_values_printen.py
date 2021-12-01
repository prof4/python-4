dict_printen = {"naam:": "bob",
                "leeftijd:": 20,
                "bloedtype:": "onbekend",
                "woont in:": "maastricht"}

def printen_van_dict():
    print(str(dict_printen) + "\n")
    print("\n")
    for key, value in dict_printen.items():
        print(key, value)
    print("\n")

printen_van_dict()
