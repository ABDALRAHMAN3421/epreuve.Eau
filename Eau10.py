import sys

def premier_index(tableau, element_recherche):   
    for i in range(len(tableau)):               
        if tableau[i] == element_recherche:      
            return i, True                             
    return -1, False                              

def main_logic():
    tableau_input = input("Entrez les éléments séparés par des espaces: ")
    element_recherche = input("Entrez l'élément recherché: ")

    if tableau_input and element_recherche:
        tableau = tableau_input.split()
        index, found = premier_index(tableau, element_recherche)
        if found:
            print("Premier index de l'élément recherché:", index)
        else:
            print("L'élément recherché n'a pas été trouvé.")
    else:
        print("Une erreur s'est produite: les entrées ne doivent pas être vides")

main_logic()
