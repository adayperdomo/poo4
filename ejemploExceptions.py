class EjemploExcepciones:
    # ZeroDivisionError

    def zeroDivisionError(self, *, num: int, den: int):
        if (den == 0):
            raise ZeroDivisionError
        return num // den
    
    # ValueError

    def valueError(self, num: int):
        if num < 0:
            raise ValueError
        return num ** 0.5

    # FileNotFoundError

    

    # Type
    
    # PermisionError

    # IndexError

    # KeyboardInterrupt

    # UnicodeDecodeError

    # AtributeError
