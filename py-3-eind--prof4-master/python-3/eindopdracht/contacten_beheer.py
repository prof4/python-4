contacten = {}
for line in open("contact.txt", "r"):
    (key, val) = line.split(": ")
    contacten[key] = val

def print_menu():
    global keuze
    print("Kies 0. lees het bestand in.")
    print("Kies 1. Bekijk jouw contacten.")
    print("Kies 2. Voeg een contact toe.")
    print("Kies 3. Pas een contact aan.")
    print("Kies 4. Verwijder een contact.")
    print("Kies 5. Sla mijn contacten op.")
    print("Kies 6. Verlaat het menu.\n")
    keuze = input("Wat is uw keuze: ")
    print()

def bestand_lezen():
    f = open("contact.txt", "r")
    contents = f.read()
    print()
    print(contents)

def dictionary_lezen():
    for key, value in contacten.items():
        print(key + ": " + value)
    print()

    
def contact_toevoegen():
    wie = input("Wie wilt u toevoegen: ")
    nummer = input("Wat is het nummer: ")
    contacten.update({wie: nummer})
    print("Contact "+wie + " toegevoegd. \n")

def contact_aanpassen():
    welk = input("Wat wilt u veranderen de naam of het telefoonnummer: ")

    #kijken of telefoon nummer moet worden verandert of niet zo ja dan:
    #   telefoonnummer(value) veranderen
    if "telefoonnummer" in welk:
        wie = input("Wie's telefoon nummer wilt u veranderen: ")
        if wie in contacten:
            nieuw_nummer = input("Wat is het nieuwe telefoonnummer: ")
            contacten[wie] = str(nieuw_nummer)
            print("Telefoonnummer van het contact" + wie + " is gewijzigd \n")
        else:
            print("telefoonnummer " + welk +" komt niet voor in de database.")
        
    #kijken of naam moet worden verandert of niet zo ja dan:
    #   contact verwijderen en opnieuw aanmaken onder andere naam
    if "naam" in welk:
        wie_old = input("Welk naam wilt u veranderen: ")
        if wie_old in contacten:
            nummer = contacten[wie_old]
            del contacten[wie_old]
            wie_new = input("Wat is de nieuwe naam van het contact: ")
            contacten.update({wie_new: nummer})
            print("Naam contact " + wie_old + " is gewijzigd naar " + wie_new + "\n")
        else:
            print("Contact " + welk + " komt niet voor in de database.")

def contact_verwijderen():
    welk = input("Welk contact wilt u verwijderen: ")
    if welk in contacten:
        del contacten[welk]
        print("Contact " + welk + " is verwijderd \n")
    else:
        print("Aangeven contact " +welk + " komt niet voor in de database. \n")

def contact_wijzigingen_opslaan():
    f = open("contact.txt", "r+")
    for key, value in contacten.items():
        f.write(key + ": " + value + "\n")
    f.close()
    print("Uw contacten zijn opgeslagen/gewijzigd  \n")

def keuze_verwerken(keuze):
    if keuze == "0":
        bestand_lezen()

    if keuze == "1":
        dictionary_lezen()

    elif keuze == "2":
        contact_toevoegen()
    
    elif keuze == "3":
        contact_aanpassen()     
        
    elif keuze == "4":
        contact_verwijderen()
        
        
    elif keuze == "5":
        contact_wijzigingen_opslaan()

        

def main():
    doorgaan = True
    while doorgaan:
        print_menu()
        keuze_verwerken(keuze)
        if keuze == "6":
            doorgaan = False 

main()
