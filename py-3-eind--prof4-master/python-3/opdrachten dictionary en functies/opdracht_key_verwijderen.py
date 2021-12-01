dict_om_te_verwijderen = {"leeftijd" : 23, "eten": "bami", "naam": "bob grinn"}

def verwijderen_van_een_key():
    print(dict_om_te_verwijderen)
    welke = input("Welk categorie wilt u verwijderen: ")
    del dict_om_te_verwijderen[welke]
    print("categorie naam verwijdert")
    print(dict_om_te_verwijderen)

verwijderen_van_een_key()
