import re

class AnaPython:
    @staticmethod
    def countDef(codigo: str) -> int:
        patron = "def.+:"
        result = re.findall(patron, codigo)
        return len(result)
    
if __name__=="__main__":
    codigo = """
def main():
pass

def main()
pass

error()
pass
"""
    print(AnaPython.countDef(codigo))