import random

def intDiv(a: int, b: int) -> int:
    try:
        return a // b
    except:
        print("Realizamos tareas de control de cierre")


#Si es el flujo principal
if __name__ == "__main__":
    """
    for i in range(10):
        a = random.randint(0, 9)
        b = random.randint(0, 9)
        print("a:", a, "b:", b, "a // b:", intDiv (a, b))
    """
    intDiv(2, "3")