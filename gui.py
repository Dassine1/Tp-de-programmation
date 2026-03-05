import tkinter as tk
from shunting_yard import tokenize
from shunting_yard import infix_to_postfix
from shunting_yard import evaluate_postfix    
def cliquer():
    try:
        depart = champ_nom.get()
        tokens = tokenize(depart)
        postfix = infix_to_postfix(tokens)
        resultat = evaluate_postfix(postfix)
        etiquette.config(text=f"Résultat: {resultat}")

    except Exception as e:
        etiquette.config(text=f"Erreur : {e}")
fenetre = tk.Tk()  

etiquette = tk.Label(fenetre, text= "Saisissez une expression mathématique:")
etiquette.pack()

champ_nom = tk.Entry(fenetre)
champ_nom.pack()

bouton = tk.Button(fenetre, text= "Enter", command= cliquer)
bouton.pack()
fenetre.title("Shunting-yard")
fenetre.mainloop()