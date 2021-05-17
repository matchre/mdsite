def tableau_markdown(liste: list) -> str:
    lignes = []
    ajout = lignes.append

    # ligne 1
    q = len(liste)
    ligne_1 = ['|n|'] # le début de la ligne 1
    for i in range(q):
        ligne_1.append(f'{i}|') # chaque morceau
    ajout("".join(ligne_1))

    # ligne 2
    ligne_2 = '|-'*(q+1) + '|'
    ajout(ligne_2)

    # ligne 3
    ligne_3 = ['|u_n|'] # le début de la ligne 3
    for i in range(q):
        ligne_3.append(f'{liste[i]}|') # chaque morceau
    ajout("".join(ligne_3))

    # ligne 4 vide !
    ajout('')

    return "\n".join(lignes)

tableau_markdown([0,1,2,4,5,6])