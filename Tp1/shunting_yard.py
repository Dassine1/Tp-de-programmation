priorite = {

            "*":2,
            "/":2,
            "+":3,
             "-":3,
}


def tokenize(depart:str)-> list[str]:
    tokens = []
    nombre = ""
    
    for caractere in depart:
        if caractere.isdigit():
            nombre+= caractere

        elif caractere in "+-*/()":
            if nombre:
                tokens.append(nombre)
                nombre = ""
            tokens.append(caractere)
    
        elif caractere == " ":
            continue

        else:
            raise ValueError(f"Opérteur inconnu {caractere}")
    if nombre:
        tokens.append(nombre)
        
    return tokens
    

def infix_to_postfix(tokens: list[str])-> list[str]:
    operateurs  = []
    liste_finale = []
    for token in tokens:
        if token.isdigit():
            liste_finale.append(token)
        elif token == "(":
            operateurs.append(token)
        elif token == ")":
            while (operateurs and operateurs[-1] != "("):
                liste_finale.append(operateurs.pop())
            operateurs.pop()
        else:
            while(operateurs and operateurs[-1] != "(" and priorite[token] >= priorite[operateurs[-1]]):
                liste_finale.append(operateurs.pop())
            operateurs.append(token)
    while operateurs:
        liste_finale.append(operateurs.pop())
    return liste_finale

def evaluate_postfix(tokens:list[str])-> float:
    pile = []
    for token in tokens:
        if token.isdigit():
            pile.append(float(token))
        else:
            if len(pile)<2:
                raise ValueError("Expression invalide.")
            b = pile.pop()
            a = pile.pop()
            if token == "+":
                pile.append(a + b)
            elif token == "-":
                pile.append(a - b)
            elif token == "*":
                pile.append(a * b)
            else:
                token == "/"
                if b == 0:
                    raise ZeroDivisionError("Il est impossible de diviser par zéro.")
                pile.append(a / b)
    return pile[0]

