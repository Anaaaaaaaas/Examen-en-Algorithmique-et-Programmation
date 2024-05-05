import turtle
from cercle import Cercle
from carre import Carre

turtle.hideturtle() # Cache la tortue graphique pour un dessin plus propre

def main():
    forme = input("Veuillez saisir la forme (cercle ou carré) : ").lower()
    couleur = input("Veuillez saisir la couleur (nom en anglais) : ")

    if forme == "cercle":
        rayon = float(input("Veuillez saisir le rayon du cercle : "))
        cercle = Cercle(rayon, couleur)
        cercle.dessiner()
    elif forme == "carré" or forme == "carre" :
        cote = float(input("Veuillez saisir la taille du côté du carré : "))
        carre = Carre(cote, couleur)
        carre.dessiner()
    else:
        print("Veuillez saisir 'cercle' ou 'carré'.")
        main()

    turtle.done()

if __name__ == "__main__":
    main() # Exécute la fonction principale si le fichier est exécuté directement