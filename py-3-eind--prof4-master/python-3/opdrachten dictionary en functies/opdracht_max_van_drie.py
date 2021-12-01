def max_een(een):
    return een
def max_twee(twee):
    return twee
def max_drie(drie):
    return drie

def max_van_3(een, twee, drie):
    if een > twee and een > drie:
        print(max_een(een))
    elif twee > een and twee > drie:
        print(max_een(twee))
    elif drie > een and drie> twee:
        print(max_een(drie))


een = int(input("wat is het eerste getal: "))
twee = int(input("wat is het tweede getal: "))
drie = int(input("wat is het derde getal: "))

max_van_3(een, twee, drie)

