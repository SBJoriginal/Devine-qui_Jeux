
# Dictionnaire des caractéristiques possibles dans le jeu.
CARACTERISTIQUES = {
    "genre": ["homme", "femme"],
    "cheveux": ["noirs", "bruns", "blonds", "blancs", "roux"],
    "yeux": ["bruns", "bleus"],
    "nez": ["petit", "gros"],
    "accessoires": ["chapeau", "bijoux", "lunettes"],
    "pilosite": ["barbe", "moustache", "calvitie"]
}


def lire_entree(ligne):
    """
    Cette fonction prend une chaîne de caractère provenant du fichier de personnages, donc
    au format "type_caracteristique:valeur_caracteristique\n", et retourne le tuple
    ("type_caracteristique", "valeur_caracteristique").
    Dans le cas où le type est accessoires ou pilosite, on retourne plutôt
    ("type_caracteristique", ["valeur1", "valeur2", etc.])

    Args:
        ligne (str): La ligne dont on veut extraire le contenu

    Returns:
        tuple: Le type de caractéristique et la valeur (sous forme de chaîne de caractère ou
            de liste de chaînes)

    """
    cle, valeur = ligne.rstrip().split(":")
    if cle in ["accessoires", "pilosite"]:
        if valeur == "":
            return cle, []
        else:
            return cle, valeur.split(",")
    else:
        return cle, valeur


def charger_personnages():
    """
    Cette fonction lit le fichier personnages.txt et le transforme en un dictionnaire
    de personnages utilisables dans le reste du programme.
    Attention! Si vous modifiez le fichier personnages.txt, cette fonction pourrait ne plus
    fonctionner correctement.

    Returns:
        dict: Le dictionnaire de personnages.
    """
    personnages = {}
    nom = None
    with open("personnages.txt", "r") as fichier_personnages:
        for ligne in fichier_personnages:
            if ligne != '\n':
                cle, valeur = lire_entree(ligne)
                if cle == 'nom':
                    nom = valeur
                    personnages[nom] = {}
                else:
                    personnages[nom][cle] = valeur
    return personnages


if __name__ == '__main__':
    # Exécutez ce fichier pour voir à quoi ressemble le dictionnaire de personnages.
    dictionnaire_personnages = charger_personnages()
    print(dictionnaire_personnages)
