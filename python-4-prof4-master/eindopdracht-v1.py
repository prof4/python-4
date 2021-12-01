#DATA
import glob, os
from os import system, name
import random
DELETE = 'd'
EXTENSIE = '.wrd'
KIES_LIJST = 'k'
MAX_WOORDLENGTE = 20
NIEUWE_LIJST = 'n'
OPSLAAN = 'w'
OVERHOREN = 'o'
SCHEIDER = '='
SCHERMBREEDTE = 80
SCHERMHOOGTE = 40
STANDAARD_LIJST = 'EN-NED'
STOPPEN = 'q'
TOEVOEGEN = 't'
bestandsnaam = STANDAARD_LIJST+EXTENSIE
woordenlijs = {}
bestand_list = []

#FUNCTIONS
#geeft de gebruiker de mogelijkheid om van woordenlijst te wisselen
def kies_lijst(lijst_naam):
  global STANDAARD_LIJST
  global bestandsnaam
  
  STANDAARD_LIJST = lijst_naam
  bestandsnaam = STANDAARD_LIJST+EXTENSIE
  bestand_list = []
  k_in = True
  while k_in:
    bestandsnaam = STANDAARD_LIJST+EXTENSIE
    leeg_scherm()
    print_header()
    inhval1 = "De huidige lijst is: "+STANDAARD_LIJST+"\n \nDe volgende woordenlijsten staan in de map:\n"
    inhval2 = "\nVoer hieronder de naam van de lijst in die u wilt kiezen\nU mag de extensie .wrd weglaten\nVoer 'q' in om te stoppen"
    print_regel(inhval1)


    os.chdir("./")
    for file in glob.glob("*"+EXTENSIE):
      filepre= file.strip(EXTENSIE)
      bestand_list.append(filepre.lower())
      print_regel(file)
        
    print_regel(inhval2)
    print_footer()
    lijstnam = input("Lijstnaam: ")
    if lijstnam.lower() == STOPPEN.lower():
      k_in = False
      main()
    elif lijstnam.lower() in bestand_list:
      STANDAARD_LIJST = lijstnam.upper()
      print(STANDAARD_LIJST)
    
  
#Maakt het terminalscherm leeg
def leeg_scherm():
  #maakt het schermleeg
  _ = system('cls')
  
#Leest de woordparen in uit het bestand genaamd 'bestandsnaam'.
def lees_woordenlijst(bestandsnaam):
  f = open(bestandsnaam)
  for line in f:
    woord1, woord2 = line.strip('\n').split('=')
    woordenlijs.update({woord1:woord2})
  f.close()
        
'''
Laat een keuzemenu zien

Op zijn minst zijn de volgende keuzes mogelijk:
 - nieuwe woordenlijst maken
 - veranderen van woordenlijst
 - woorden toevoegen aan een woordenlijst
 - woordenlijsten overhoren
 - stoppen met het programma

De gebruiker kan vervolgens steeds nieuwe keuzes blijven maken.
'''
def main():
  leeg_scherm()
  print_menu(STANDAARD_LIJST)
  keuze = input("Uw keuze: ")
  keuze_klein_letter = keuze.lower()
  if keuze_klein_letter == OVERHOREN:
    leeg_scherm()
    overhoren(woordenlijs)
  elif keuze_klein_letter == TOEVOEGEN:
    leeg_scherm()
    voeg_woorden_toe(woordenlijs, STANDAARD_LIJST)
  elif keuze_klein_letter == KIES_LIJST:
    leeg_scherm()
    kies_lijst(STANDAARD_LIJST)
  elif keuze_klein_letter == NIEUWE_LIJST:
    leeg_scherm()
    nieuwe_lijst_naam()
  elif keuze_klein_letter == STOPPEN:
    leeg_scherm()
    print_afscheid()
  else:
    print("ongeldige keuze")
    main()
    
#maakt een nieuwe lijst genoemd naar de meegegeven naam
def nieuwe_lijst_naam():
  dg=True
  while dg:
    global STANDAARD_LIJST
    global bestandsnaam
    inhval1 = "Typ de naam van de woordenlijst dat u wilt toevoegen.\n\nU kunt de extensie "+EXTENSIE+" weglaten.\n\nVoer 'q' in om te stoppen"
    print_header()
    print_regel(inhval1)
    print_footer()
    nieuw_lijst = input("Lijstnaam: ")
    if nieuw_lijst.lower() == STOPPEN:
      dg=False
      main()
    else:
      STANDAARD_LIJST = nieuw_lijst.upper()
      f = open(STANDAARD_LIJST+EXTENSIE, "w")
      f.close
      bestandsnaam = STANDAARD_LIJST+EXTENSIE
      inhval2 = "Woordenlijst Succesvol toegevoegd\nDruk Enter om verder te gaan.\nVoer 'q' in om te stoppen."
      print_header()
      print_regel(inhval2)
      print_footer()
      dg_of_nie = input("Keuze: ")
      if dg_of_nie == STOPPEN:
        main()
    
  
#Blijf woorden overhoren totdat de gebruiker aangeeft te willen stoppen.
def overhoren(woordenlijst):
  leeg_scherm()
  MAX_WOORD_LENGTE = 14
  nietgestop = True
  inhval4 = "\nDruk Enter om verder te gaan. \nDruk 'q' om te stoppen en 'd' om het woord te verwijderen"
  while nietgestop:
    leeg_scherm()
    lees_woordenlijst(bestandsnaam)
    print_header()
    
    woord = random.choice(list(woordenlijst.keys()))
    lengte_woord = len(woord)
    afstand =  lengte_woord+8
    inhvalpre1 = "vertaal het woord: {:"+str(afstand)+"s}"
    inhval1 = inhvalpre1.format(woord)    
  
    print_regel(inhval1)
    print_footer()
    vertaling = input("Uw vertaling: ")
    inhval3 = "Helaas, het antwoord was: "+woord+" \nJij had als antwoord: "+vertaling
    goed_vert = woordenlijst.get(woord)
    if vertaling.lower() == goed_vert.lower():
      leeg_scherm()
      print_header()
      print_regel(("Goed zo! {:^" + str(MAX_WOORD_LENGTE) + "} Betekent: {:^" + str(MAX_WOORD_LENGTE) + "}").format(vertaling.lower(), woord.lower()))
      print_regel(inhval4)
      print_footer()
      keuze = input("Uw keuze: ")
      if keuze.lower() == STOPPEN:
        nietgestop = False
        main()
      elif keuze.lower() == DELETE.lower():
        verwijder_woord(woord, woordenlijst)
    else:
      leeg_scherm()
      print_header()
      print_regel(inhval3)
      print_regel(inhval4)
      print_footer()
      keuze = input("Uw keuze: ")
      if keuze.lower() == STOPPEN:
        nietgestop = False
        main()
      elif keuze.lower() == DELETE.lower():
        verwijder_woord(woord, woordenlijst)


        
  
        


#Print een afscheidboodschap nadat het programma is afgesloten
def print_afscheid():
  inhval = "Dankuwel voor het gebruikmaken van onze overhoor programma! Tot Gauw!\n\nAls u zeker weet dat u het programma wilt aflsuiten druk enter, als u het programma niet wilt afsluiten typ dan iets gevolgt door enter."
  print_header()
  print_regel(inhval)
  print_footer()
  bye = input()
  if not bye == "":
    main()
  #stopt het programma helemaal
  quit()
  
'''
Print het volgende over de hele breedte van het scherm:
|             |
===============
Dus een volle regel met '='-tekens en een regel die begint en eindigt met een '|'.
'''
def print_footer():
  print("| "+(SCHERMBREEDTE-4)*" "+" |")
  print(SCHERMBREEDTE*"=")

'''
Print het volgende over de hele breedte van het scherm:
===============
|             |
Dus een volle regel met '='-tekens en een regel die begint en eindigt met een '|'.
'''
def print_header():
  print(SCHERMBREEDTE*"=")
  print("| "+(SCHERMBREEDTE-4)*" "+" |")
        
#Print het (keuze)menu inclusief de geselecteerde lijst
def print_menu(lijst_naam):
  inhval = "Welkom bij het overhoorprogramma! \n \n De woordenlijst die nu geselecteerd is, is: "+lijst_naam+" \n \n Hieronder vind je de keuzes doe je hebt in dit programma: \n \n o - overhoor de geselecteerde woordenlijst \n \n t - voeg woorden toe aan de geselecteerde woordenlijst \n \n k - selecteer een andere woordenlijst \n \n n - maak een nieuwe woordenlijst \n \n q - stop het programma"
  print_header()
  print_regel(inhval)
  print_footer()
  
'''
print_regel() print de inhoud links uitgelijnd uit.
Voor de inhoud wordt '| ' gezet en rechts uitgelijnd ' |'.
'''

def print_regel(inhoud):
  def inhoudt():
    prival = list(inhoud.split('\n'))
    for lin in prival:
      print_regel(str(lin))
  def print_regel(regel):
    print(("| {:" + str(SCHERMBREEDTE - 4)+ "} |").format(regel))

  inhoudt()

'''
Schrijft de woordparen weg naar het bestand genaamd 'bestandsnaam'.
De oude inhoud van het bestand wordt overschreven!
'''
def schrijf_woordenlijst(bestandsnaam, woordenlijst):
  f = open(bestandsnaam)
  for line in f:
    woord1, woord2 = line.strip('\n').split('=')
    woordenlijst.update({woord1:woord2})
  f.close()
  f = open(bestandsnaam, 'w')
  for woord1, woord2 in woordenlijs.items():
    f.write(woord1+"="+ woord2+"\n")
  f.close()

#Vraagt of gebruiker zeker weet of er verwijderd moet worden.
#verwijdert het woord en de vertaling uit de lijst als dit zo is.
def verwijder_woord(woord, woordenlijst):
  leeg_scherm()
  print_header()
  inhval = "Weet u zeker dat u het woord: " + woord + " wilt verwijderen?\n \nType enter om het woord te verwijderen en iets anders gevolg door enter om \nhet woord niet te verwijderen."
  print_regel(inhval)
  print_footer()
  zofnie = input()
  if not zofnie == "":
    overhoren(woordenlijst)
  
  f = open(bestandsnaam)
  for line in f:
    woord1, woord2 = line.strip('\n').split('=')
    woordenlijst.update({woord1:woord2})
  f.close()
  del woordenlijst[woord]
  f= open(bestandsnaam, 'w')
  for woord1, woord2 in woordenlijst.items():
    f.write(woord1+"="+ woord2+"\n")
  f.close()
  overhoren(woordenlijst)
        
##Vraag de gebruiker steeds om woordenparen en voeg ze toe aan de lijst.
##Stop als de gebruiker aangeeft te willen stoppen.
def voeg_woorden_toe(woordenlijst, lijst_naam):
  nieuw_woord_j_n = 0
  print_header()
  inhval1 = "Je Voegt woorden toe in de lijst: "+lijst_naam+"\nVoer de twee woorden in met een '='-teken ertussen \nVoorbeeld:\nCar=Auto \n \nDenk erom: geen spaties! \n \nVoer 'q' om  te stoppen"
  print_regel(inhval1)
  doorofnie = True
  nieuw_woord_j_n = 1
  print_footer()
  while doorofnie:
      countofis = 0
      invoer_toevoeg = input("Woorden: ")
      for i in invoer_toevoeg:
        if i == "=":
              countofis += 1

      if invoer_toevoeg == "q":
          doorofnie= False
          main()
      elif not countofis == 1:
        print("ERROR >>> te veel of te weinig '='-sen")
            
      else:
        leeg_scherm()
        prival = list(invoer_toevoeg.split('='))
        woord1 = prival[0]
        woord2 = prival[1]
        nieuw_woord_j_n = 1
        print_header()
        inhval2 = "Je hebt ingevoerd: \n" + "'"+woord1+" en "+woord2+"'\nDruk Enter om toe te voegen en iets anders gevolg door enter om het niet toe\nte voegen"
        print_regel(inhval2)
        print_footer()
        vofnie = input()
        if vofnie == "":
          leeg_scherm()
          nieuw_woord_j_n = 1
          woordenlijs.update({woord1: woord2})
          print_header()
          print_regel(inhval1)
          print_footer()
          schrijf_woordenlijst(lijst_naam+EXTENSIE, woordenlijst)

        else:
          leeg_scherm()
          if nieuw_woord_j_n == 1:
            schrijf_woordenlijst(lijst_naam+EXTENSIE, woordenlijst)
          print_header()
          print_regel(inhval1)
          print_footer()              
            
            
#roept het programma aan
main()
  
        

