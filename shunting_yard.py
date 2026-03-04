operateurs  = []
liste_finale = []

priorite = {
            "()":1,
            "*":2,
            "/":2,
            "//":2,
            "%":2,
            "+":3,
            "-":3
}
def tokenize(depart:str)-> list[str]:
    tokens = []
    nombre = ""
    
    for caractere in depart:
        if caractere.isdigit():
            nombre+= caractere
        else:
            if nombre:
                tokens.append(nombre)
                nombre = ""
            tokens.append(caractere)

    if nombre:
        tokens.append(nombre)
    return tokens
    

def infix_to_postfix(tokens: list[str])-> list[str]:
    return None

def evaluate_postfix(tokens:list[str])-> float:
    return None

