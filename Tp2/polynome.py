from expression import Expression


class Polynome(Expression):
    def __init__(self, coefficients: list[float]):
        self.coefficients = coefficients

    def evaluer(self, x: int) -> int:
        resultat = 0
        for i, coef in enumerate (self.coefficients):
            resultat += coef * x**i
        return resultat
    
    def deriver(self) -> Expression:
        if len(self.coefficients) <= 1:
            return Polynome([0])
        derivee = []
        for i in range(1, len(self.coefficients)):
            derivee.append(i * self.coefficients[i])
        return Polynome(derivee)

    def __str__(self) -> str:
        termes = []
        for i, coef in enumerate(self.coefficients):
            if coef == 0:
                continue
            if i == 0:
                termes.append(f"{coef}")
            elif i == 1:
                termes.append(f"{coef}x")
            else:
                termes.append(f"{coef}x^ {i}")
        if not termes:
            return("0")
        return " + " .join(termes)