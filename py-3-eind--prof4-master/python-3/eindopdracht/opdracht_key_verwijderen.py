dict_om_te_verwijderen = {"leeftijd" : 23, "eten": "bami", "naam": "Carl macguffin"}

def verwijderen_van_een_key(welke, dict_om_te_verwijderen):
    del dict_om_te_verwijderen[welke]
    print("categorie naam verwijdert")
    print(dict_om_te_verwijderen)

print(dict_om_te_verwijderen)
welke = input("Welk categorie wilt u verwijderen: ")
verwijderen_van_een_key(welke, dict_om_te_verwijderen)
