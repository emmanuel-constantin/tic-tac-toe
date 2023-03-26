import random

def ia(board, signe):
    if signe not in ("X", "O"):
        return False

    # recherche une case où l'IA peut gagner, c'est-à-dire une case vide où 
    # elle peut placer son signe et ainsi obtenir une configuration gagnante. 
    # Pour chaque case vide, elle place le signe de l'IA et vérifie s'il y a une victoire. 
    # Si c'est le cas, elle retourne l'indice de cette case. Sinon, elle remet cette case à 
    # zéro et continue à chercher dans les cases vides suivantes
    for i in range(9):
        if board[i] == 0:
            board[i] = 1 if signe == "X" else 2
            if verifier_victoire(board, signe):
                board[i] = 0
                return i
            board[i] = 0

    # Si la première boucle "for" n'a pas renvoyé de coup gagnant pour l'IA, 
    # la deuxième boucle "for" recherche une case où l'adversaire peut gagner
    # Pour chaque case vide, elle place le signe de l'adversaire et vérifie s'il y a une victoire. 
    # Si c'est le cas, elle retourne l'indice de cette case. Sinon, elle remet cette case à zéro 
    # et continue à chercher dans les cases vides suivantes
    adversaire = "O" if signe == "X" else "X"
    for i in range(9):
        if board[i] == 0:
            board[i] = 1 if adversaire == "X" else 2
            if verifier_victoire(board, adversaire):
                board[i] = 0
                return i
            board[i] = 0

    # Si la deuxième boucle "for" n'a pas renvoyé de coup gagnant pour l'adversaire, 
    # la fonction choisit une case vide au hasard et la retourne
    cases_libres = [i for i in range(9) if board[i] == 0]
    if cases_libres:
        return random.choice(cases_libres)

    # Si le plateau est plein, retourner False
    return False
# vérifie si le signe du joueur correspond à une configuration gagnante sur le plateau 
# de jeu en vérifiant chaque condition de victoire possible (3 alignées horizontalement, 
# verticalement ou en diagonale). Si le signe du joueur correspond à l'une des configurations gagnantes, 
# la fonction renvoie "True", sinon elle renvoie "False"
def verifier_victoire(board, signe):
    signe = 1 if signe == "X" else 2
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == signe:
            return True
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == signe:
            return True
    if board[0] == board[4] == board[8] == signe:
        return True
    if board[2] == board[4] == board[6] == signe:
        return True
    return False
