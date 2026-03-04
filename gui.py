import tkinter as tk

priorite = {
            "()":1,
            "*":2,
            "/":2,
            "//":2,
            "%":2,
            "+":3,
            "-":3
}

def tokenize(expression:str)-> list[str]:
    return None

def infix_to_postfix(tokens: list[str])-> list[str]:
    return None

def evaluate_postfix(tokens:list[str])-> float:
    return None

def cliquer():
    etiquette.config(text=champ_nom.get() )
    
fenetre = tk.Tk()  

etiquette = tk.Label(fenetre, text= "Saisissez une expression mathématique:")
etiquette.pack()

champ_nom = tk.Entry(fenetre)
champ_nom.pack()
depart = [champ_nom]
print(depart)
bouton = tk.Button(fenetre, text= "Enter", command= cliquer)
bouton.pack()
fenetre.title("Shunting-yard")
fenetre.mainloop()


operateurs  = []
liste_finale = []
