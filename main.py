import tkinter as tk
import tkinter.messagebox as messagebox
import random
import ia

class TicTacToe:
    
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.joueur_actuel = "X"
        self.board = [0] * 9
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.plateau()
    
    def plateau(self):
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.master, text="", font=("Helvetica", 20), width=5, height=2,
                                   command=lambda row=row, col=col: self.jouer_coup(row, col))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button
    
    def jouer_coup(self, row, col):
        index = row * 3 + col   
        # calcule l'indice correspondant dans la liste "board" à partir des coordonnées du bouton. 
        # Comme le plateau de jeu est représenté par une liste à une dimension, l'indice est calculé 
        # en multipliant le numéro de ligne par 3 et en ajoutant le numéro de colonne.
        if self.board[index] == 0:  
        # vérifie si la case correspondante est vide (la valeur de la liste "board" à cet indice 
        # est égale à 0). Si ce n'est pas le cas, la fonction ne fait rien
            self.board[index] = 1 if self.joueur_actuel == "X" else 2 
            # Si la case est vide, la troisième ligne met à jour 
            # la liste "board" avec la valeur correspondante (1 pour "X" et 2 pour "O") en utilisant 
            # une expression ternaire. L'expression ternaire teste si le joueur actuel est "X" ou "O" 
            # et assigne la valeur correspondante
            self.buttons[row][col].config(text=self.joueur_actuel)
            # met à jour le texte du bouton correspondant avec le symbole du joueur actuel (soit "X", soit "O") 
            # en utilisant la méthode "config" du bouton.   
            if self.verifier_victoire():
                self.message_victoire()
                # vérifie s'il y a une victoire en appelant la méthode "verifier_victoire". Si c'est le cas, la 
                # méthode "message_victoire" est appelée pour afficher un message de victoire à l'utilisateur.
            elif self.egalite():
                self.message_egalite()
                # vérifie s'il y a une égalité en appelant la méthode "egalite". Si c'est le cas, la méthode 
                # "message_egalite" est appelée pour afficher un message d'égalité à l'utilisateur.
            else:
                self.jouer_coup_ia()
                # Si aucun joueur n'a gagné et qu'il reste des cases vides, la dernière ligne appelle la méthode 
                # "jouer_coup_ia" pour permettre à l'IA de jouer un coup.

    def jouer_coup_ia(self):
        coup = ia.ia(self.board, "X" if self.joueur_actuel == "O" else "O")
        #  appelle la fonction "ia" du module "ia" pour obtenir le coup que l'IA va jouer. 
        #  L'argument "self.board" est utilisé pour représenter le plateau de jeu actuel, 
        #  et l'argument "X" ou "O" est utilisé pour représenter le symbole de l'IA. Le résultat est stocké dans la variable "coup"
        if coup is not False:
            # vérifie si le coup retourné par l'IA est valide. Si "coup" est "False", cela signifie que l'IA ne peut pas jouer de 
            # coup valide et la fonction ne fait rien
            row, col = coup // 3, coup % 3
            # Si le coup est valide, calcule les coordonnées du bouton correspondant à partir de l'indice "coup" 
            # en utilisant la division entière et le modulo. Les variables "row" et "col" sont assignées à ces coordonnées
            ia_signe = "O" if self.joueur_actuel == "X" else "X"
            # détermine le symbole de l'IA ("X" ou "O") en utilisant une expression ternaire, en fonction du symbole du joueur actuel
            self.board[coup] = 2 if self.joueur_actuel == "X" else 1
            # met à jour la liste "board" avec la valeur correspondante (2 pour "O" et 1 pour "X") en utilisant une autre expression ternaire
            self.changement_joueur()
            # appelle la méthode "changement_joueur" pour passer la main au joueur humain
            self.buttons[row][col].config(text=ia_signe)
            # met à jour le texte du bouton correspondant avec le symbole de l'IA en utilisant la méthode "config" du bouton
            if self.verifier_victoire():
                self.message_victoire()
            elif self.egalite():
                self.message_egalite()
            else:
                self.changement_joueur()

    
    def verifier_victoire(self):
        # cette fonction vérifie s'il y a un gagnant en vérifiant si les cases du plateau correspondent à chaque condition de victoire 
        # possible contiennent le symbole du joueur gagnant, et renvoie "True" s'il y a un gagnant et "False" sinon
        for signe in (1, 2):
            if self.board[0] == self.board[1] == self.board[2] == signe:
                return True
            elif self.board[3] == self.board[4] == self.board[5] == signe:
                return True
            elif self.board[6] == self.board[7] == self.board[8] == signe:
                return True
            elif self.board[0] == self.board[3] == self.board[6] == signe:
                return True
            elif self.board[1] == self.board[4] == self.board[7] == signe:
                return True
            elif self.board[2] == self.board[5] == self.board[8] == signe:
                return True
            elif self.board[0] == self.board[4] == self.board[8] == signe:
                return True
            elif self.board[2] == self.board[4] == self.board[6] == signe:
                return True
        return False
    
    def message_victoire(self):
        messagebox.showinfo("Tic Tac Toe", f"{self.joueur_actuel} gagne !")
        self.reinit_plateau()
    
    def egalite(self):
        return not any(x == 0 for x in self.board)
    
    def message_egalite(self):
        messagebox.showinfo("Tic Tac Toe", "Egalité !")
        self.reinit_plateau()

    def changement_joueur(self):
        self.joueur_actuel = "O" if self.joueur_actuel == "X" else "X"

    def reinit_plateau(self):
        self.joueur_actuel = "X"
        self.board = [0] * 9
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text="")
    
if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()

