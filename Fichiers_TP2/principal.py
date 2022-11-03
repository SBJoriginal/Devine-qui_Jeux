from personnages import charger_personnages
from devine_qui import selectionner_caracteristique, mettre_a_jour_hypotheses


def former_question(type_caracteristique, caracteristique):
    """
    Cette fonction permet de passer d'un type et d'une caractéristique à une
    question valide en français.

    Args:
        type_caracteristique (str): Le type de caractéristique sur lequel on questionne
        caracteristique (str): La valeur de la caractéristique dont on demande la présence.

    Returns:
        str: Le type et la caractéristique, sous forme de question en français

    """
    questions = {
        "genre": "Le personnage est-il un(e) {} ? ",
        "accessoires": "Le personnage porte-t-il un/des {} ? ",
        "cheveux": "Le personnage a-t-il les cheveux {} ? ",
        "yeux": "Le personnage a-t-il les yeux {} ? ",
        "nez": "Le personnage a-t-il un {} nez ? ",
        "pilosite": "Le personnage a-t-il une {} ? "
    }
    return questions[type_caracteristique].format(caracteristique)


def poser_question(type_caracteristique, caracteristique):
    """
    Cette fonction permet de poser une question et de gérer sa réponse.
    Elle retourne True pour oui/o (majuscule comme minuscule), et False
    pour non/n. Elle valide l'entrée de l'utilisateur de sorte que si on
    entre autre chose, la question est reposée tant que la réponse n'est
    pas valide.

    Args:
        type_caracteristique (str): Le type de caractéristique sur lequel on questionne
        caracteristique (str): La valeur de la caractéristique dont on demande la présence.

    Returns:
        bool: True si l'utilisateur répond oui/o, False s'il répond non/n.

    """
    question = former_question(type_caracteristique, caracteristique)
    reponse = None
    while reponse is None:
        reponse_str = input(question).lower()
        if reponse_str in ['oui', 'o']:
            reponse = True
        elif reponse_str in ['non', 'n']:
            reponse = False
        else:
            print("Veuillez répondre par oui/o ou non/n")
    return reponse


if __name__ == '__main__':
    # Programme principal. Exécuter ce fichier pour jouer au jeu complet.

    print("Bienvenue au jeu Devine qui!")
    print("Choisissez un des 24 personnages disponibles dans l'énoncé. ")
    print("Je vous poserai des questions qui se répondent par oui (o) ou non (n). ")
    print("Mon but est de déterminer votre personnage avec certitude en posant le moins de questions possibles. ")

    personnages_restants = charger_personnages()
    n_questions = 0
    type_caracteristique = None

    input("\nAppuyez sur une Entrée une fois votre personnage choisi... ")

    # Boucle qui sélectionne une question à poser et met à jour les hypothèses de l'intelligence artificielle.
    while len(personnages_restants) > 1:
        n_questions += 1
        type_caracteristique, caracteristique = selectionner_caracteristique(personnages_restants)
        print("Question # {}".format(n_questions))
        reponse = poser_question(type_caracteristique, caracteristique)
        personnages_restants = mettre_a_jour_hypotheses(personnages_restants, type_caracteristique,
                                                        caracteristique, reponse)

    # Code affichant la solution finale.
    print()
    if len(personnages_restants) == 0:
        print("Tiens donc... aucun personnage ne correspond à cette description :(")
    else:
        print("Je devine que votre est personnage est {} !".format(
            list(personnages_restants.keys())[0]
        ))
        print("Cela m'a pris {} questions. ".format(n_questions))
