class EjemploExcepciones:
    # ZeroDivisionError

    def zeroDivisionError(self, *, num: int, den: int):
        if (den == 0):
            raise ZeroDivisionError
        return num // den
    
    # ValueError

    def valueError(self):
        3 * int("f")
        raise ValueError

    # FileNotFoundError

    def fileNotFoundError(self):
        abrir = open("file.txt")
        if abrir != open("file.txt"):
            raise FileNotFoundError
        return "El archivo no se abre"

    # TypeError

    def typeError(self, *, a, b):
        if (b == str):
            raise TypeError
        return a * b
    
    # PermisionError
    
    def permissionError(file):
        try:
            with open("file.txt", "r") as file:
                file.write("Hola")
        except:
            raise PermissionError
        
    # IndexError

    def indexError(self):
        lista = [1, 2, 3, 4, 5]
        x = 0
        while x < len(lista):
            print(lista[x])
            x += 1
        raise IndexError

    # KeyboardInterrupt

    def keyboardInterrupt(n):
        try:
            n = int(input("Input a number: "))
        except:
            raise KeyboardInterrupt

    # UnicodeDecodeError

    def unicodeDecodeError(self):
        try:
            b"\x81".decode("utf-8")
        except UnicodeDecodeError as unicode:
            raise unicode

    # AtributeError

    def atributeError(self):
        mensaje = "hola mundo".error
        if mensaje == AttributeError:
            raise AttributeError

    