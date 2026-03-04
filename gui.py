import tkinter as tk
import shunting_yard
from shunting_yard import tokenize
    
def cliquer():
    depart = champ_nom.get()
    tokens = tokenize(depart)
    etiquette.config(text=str(tokens))
fenetre = tk.Tk()  

etiquette = tk.Label(fenetre, text= "Saisissez une expression mathématique:")
etiquette.pack()

champ_nom = tk.Entry(fenetre)
champ_nom.pack()

depart = []
print(depart)
bouton = tk.Button(fenetre, text= "Enter", command= cliquer)
bouton.pack()
fenetre.title("Shunting-yard")
fenetre.mainloop()