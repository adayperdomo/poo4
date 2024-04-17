class EjemploExcepciones:
    # ZeroDivisionError

    def intDiv(a: int, b: int) -> int:
        try:
            a = 10
            b = 0
            print(a/b)
        except ZeroDivisionError:
            return("Error: Cannot divide by zero")
    
    # ValueError

    

    # FileNotFoundError

    # Type
    
    # PermisionError

    # IndexError

    # KeyboardInterrupt

    # UnicodeDecodeError

    # AtributeError
