score_maximal = 0
type_maximal = None
valeur_maximal = None
for type in types_caracteristiques_ordre_aleatoire():  # aléatoire
    for valeur in valeurs_ordre_aleatoire(type):  # aléatoire
        score = score_dichotomie(personnages_restants, type,
                                 valeur)  # calcule le score des meilleur choix en tout moment de la partie
        if score > score_maximal:
            score_maximal = score
            type_maximal = type
            valeur_maximal = valeur
        # print(type_maximal, valeur_maximal)
return type_maximal, valeur_maximal







dict = {}  # commencer avec un dictionnaire vide pour rajouter les personnage que nous voulons

for i, donnees in personnages_restants.items():
    possede_t_il = possede(donnees, type_caracteristique,
                           valeur_caracteristique)  # détermine si le personnage en question à une caracteristique demandé
    concerve = reponse  # voulons nous gardez ou perdre les personnage avec cette caracteristique.

    if possede_t_il and concerve == True:  # a le chapeau et on veut ceux qui ont un chapeaux
        dict[i] = donnees
    elif not possede_t_il and concerve == False:  # n'a pas le chapeau et on veut ceux qui nont pas de chapeau
        dict[i] = dict
    else:  # a un chapeau que on veut pas ou a pas un chapeau quand on veut
        dict = dict
# print(t)
return dict

dictionnaire = {}
for nom, donnees in personnages_restants.items():
    est_ce_possede = possede(donnees, type_caracteristique, valeur_caracteristique)
    veut_concerver = reponse

    if est_ce_possede and veut_concerver == True:
        dictionnaire[nom] = donnees
    elif not est_ce_possede and veut_concerver == False:
        dictionnaire[nom] = donnees
    else:
        dictionnaire = dictionnaire
return dictionnaire