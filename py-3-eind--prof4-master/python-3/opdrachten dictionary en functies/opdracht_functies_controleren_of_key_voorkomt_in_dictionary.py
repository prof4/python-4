dict_printen = {"naam": "bob",
                "leeftijd": 20,
                "bloedtype": "onbekend",
                "woont in": "maastricht",
                "tijdzone": "Mid European Time(MET)"}

def controle_van_dict(key):
    if key in dict_printen:
        return True
    else:
        return False

key = input("Waar van wilt u controleren of het in een dict is: ")
print(controle_van_dict(key))
