import re

class MinVoc:
    def __init__(self) -> None:
        pass

    @staticmethod
    def buscar(texto: str) -> list:
        #patrón de palabras que empiezan por vocal en minúscula
        patron = ""