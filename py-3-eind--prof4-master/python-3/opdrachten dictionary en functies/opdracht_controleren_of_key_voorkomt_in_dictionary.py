dict_printen = {"naam": "bob",
                "leeftijd": 20,
                "bloedtype": "onbekend",
                "woont in": "maastricht",
                "tijdzone": "Mid European Time(MET)"}

def controle_van_dict():
    key = input("Waar van wilt u controleren of het in een dict is: ")
    value = dict_printen[key]
    if key in dict_printen:
        print("het opgegeven element komt voor in de dictionary")
        print(key, value)

controle_van_dict()
