# en : Real Mah-jong game by Nicolas Siterre
# fr : Vrai jeu de Mah-jong par Nicolas Siterre
# de : Richtigte Mah-jong spiel bei Nicolas Siterre

import time
import math
from tkinter import *
from tkinter import ttk
import algoia as ia
import plaquettes

root = Tk()
root.title("Mah-jong")
mainframe = ttk.Frame(root, padding="100 100")
mainframe.grid(sticky=(N, S, E, W))
root.columnconfigure(10, weight=100)
root.rowconfigure(10, weight=100)

# définitons des pions
def definition_pions () :
    {#1 = bohneurs (dragons).
        #1.1 = dragon vert.
        #1.2 = dragon rouge.
        #1.3 = dragon blanc.
    }
    {#2 = vents. [!honneur!]
        #2.1 = vent du nord.
        #2.2 = vent de l'est.
        #2.3 = vent du sud.
        #2.4 = vent de l'ouest.
    }
    {#3 = cercles.
        #3.1 = 1 de cercle. [!honneur!]
        #3.2-8 = 3-8 de cercles.
        #3.9 = 9 de cercles. [!honneur!]
    }
    {#4 = symboles.
        #4.1 = 1 de symbole. [!honneur!]
        #4.2-8 = 2-8 de symboles.
        #4.9 = 9 de symboles. [!honneur!]
    }
    {#5 = banbous.
        #5.1 = 1 de banbou. [!honneur!]
        #5.2-8 = 2-8 de banbous.
        #5.9 = 9 de banbous. [!honneur!]
    }

# départ
# création des variables qui représentes les murs // 1 = haut & 2 = bas
mur_nord_1 = [3.5,3.1,5.7,4.9,5.2,3.8,4.4,5.9,4.8,5.6,5.1]
mur_nord_2 = [4.1,3.3,2.4,4.7,5.8,4.3,1.2,3.6,3.9,4.2,2.3]
mur_est_1 =  [5.3,2.1,5.8,4.9,3.2,5.7,4.5,3.7,3.3,5.3]
mur_est_2 =  [3.1,3.4,4.6,1.1,5.9,2.2,4.1,5.5,4.8,5.2]
mur_sud_1 =  [4.6,2.4,3.5,5.7,4.4,3.4,4.8,3.6,2.3,5.6,1.3]
mur_sud_2 =  [1.3,5.3,4.1,5.4,4.9,2.2,3.1,5.1,4.3,5.8,5.4]
mur_ouest_1 = [2.1,5.5,3.8,4.2,5.9,3.8,5.8,2.4,5.7,4.4]
mur_ouest_2 = [4.9,3.7,5.3,3.3,1.2,4.3,5.2,4.5,3.2,5.1]
# création des variables qui représentes les plaquettes
plaquettes.modifier.creer.norm()
# création des variables qui représentes les plaquettes des pans et show
plaquettes.modifier.creer.pan()
print("initialisation terminée")

def etape_2(pion, ligne) :
    #identification des pions
    #premier nombre
    pion_test = int(pion)
    if (pion_test == 1) :
        resultat_test = ["dragon"]
    elif (pion_test == 2) :
        resultat_test = ["vent"]
    elif (pion_test == 3) :
        resultat_test = ["cercle"]
    elif (pion_test == 4) :
        resultat_test = ["symbole"]
    elif (pion_test == 5) :
        resultat_test = ["banbou"]
    #deuxième nombre
    pion_test = int(pion*10-pion_test*10)
    if (pion_test == 1) :
        if (resultat_test[0] == "dragon") :
            resultat_test.insert(0,"vert")
        elif (resultat_test[0] == "vent") :
            resultat_test.insert(0,"nord")
        else :
            resultat_test.insert(0,"un")
    elif (pion_test == 2) :
        if (resultat_test[0] == "dragon") :
            resultat_test.insert(0,"rouge")
        elif (resultat_test[0] == "vent") :
            resultat_test.insert(0,"est")
        else :
            resultat_test.insert(0,"deux")
    elif (pion_test == 3) :
        if (resultat_test[0] == "dragon") :
           resultat_test.insert(0,"blanc")
        elif (resultat_test[0] == "vent") :
            resultat_test.insert(0,"sud")
        else :
            resultat_test.insert(0,"trois")
    elif (pion_test == 4) :
        if (resultat_test[0] == "vent") :
            resultat_test.insert(0,"ouest")
        else :
            resultat_test.insert(0,"quatre")
    elif (pion_test == 5) :
        resultat_test.insert(0,"cinq")
    elif (pion_test == 6) :
        resultat_test.insert(0,"six")
    elif (pion_test == 7) :
        resultat_test.insert(0,"sept")
    elif (pion_test == 8) :
        resultat_test.insert(0,"huit")
    elif (pion_test == 9) :
        resultat_test.insert(0,"neuf")

ia.main(1.2, "est")



root.mainloop()
