import re

class RexExample:
    def __init__(self) -> None:
        pass

    @staticmethod
    def buscar(texto: str) -> list:
        #patrón de palabras que empiezan por vocal en minúscula
        patron = "\\b[aeiou][^\\s.,]*"
        result = re.findall(patron, texto)
        return result
    
    @staticmethod
    def validURL(url:str) -> bool:
        pass
    
if __name__=="__main__":
    text = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi suscipit auctor orci, sed sagittis augue. Mauris egestas feugiat urna, et malesuada ex. Donec vel tellus pulvinar augue ultrices ullamcorper. Integer ligula tortor, laoreet nec purus pulvinar, pharetra pellentesque diam. Nulla turpis felis, ultricies ac diam sit amet, porttitor tempor orci. Nam ac consectetur neque. Pellentesque facilisis suscipit odio et gravida. Suspendisse vel quam condimentum, facilisis mi vel, sagittis turpis. Donec accumsan ex risus, in sodales tortor porttitor ut. Praesent sit amet venenatis enim, et gravida est. Sed ultrices erat ex, vel rutrum enim aliquet sed. Cras vel dapibus diam. Curabitur nisi velit, eleifend a quam at, volutpat tempus dui.

Etiam eget arcu dui. Morbi hendrerit mi non velit volutpat condimentum. Nullam sit amet mattis mi. Donec efficitur eleifend mattis. Donec at finibus magna. Donec tincidunt imperdiet lorem eget egestas. Nullam volutpat iaculis libero, et mollis ipsum rutrum a. Nullam ultrices tellus quis auctor vestibulum. Duis velit libero, euismod quis fermentum ut, dignissim id nulla. Pellentesque placerat ullamcorper lectus scelerisque mattis. Sed tempus lectus sem, vitae consequat nisi malesuada non. Pellentesque tincidunt, est eu imperdiet laoreet, massa dui viverra tortor, ac tincidunt nulla erat quis nisi. Integer accumsan turpis vitae eros blandit blandit.

Quisque ligula nisi, viverra in nisi eget, posuere lobortis ligula. Donec viverra odio egestas lacus volutpat dictum. Sed blandit est nec commodo gravida. Integer ut mi aliquam, mollis velit ac, auctor dui. Sed a dapibus dui, quis egestas justo. Phasellus volutpat pellentesque eros. Fusce at convallis leo. Quisque posuere ornare nibh, sed elementum ligula ornare quis. Morbi erat quam, pulvinar id metus et, aliquam condimentum neque. Sed consectetur tristique feugiat. Proin at ultricies ipsum.

Curabitur at finibus augue. In euismod vel sapien et faucibus. Praesent mollis, nunc sit amet mollis faucibus, justo augue laoreet orci, non bibendum nulla dolor id augue. Quisque in vestibulum massa, vel pharetra enim. Pellentesque ac pharetra nisl. Nunc congue et metus sit amet blandit. Maecenas elit tortor, scelerisque id viverra eu, condimentum vitae massa. Etiam varius turpis sit amet diam pharetra tristique. Vivamus vel ante nec turpis rutrum posuere vel eget nibh. Nullam luctus quam at lectus tincidunt auctor. Etiam nec nisi ac lorem suscipit hendrerit. Etiam eleifend dui eu luctus aliquet. Donec eu porttitor ligula, ut pretium dui.

Phasellus malesuada in metus nec tristique. Praesent eget mauris nibh. Phasellus fermentum, erat sit amet fringilla vehicula, mauris dolor venenatis erat, euismod tempor diam ante eu dui. Quisque ultricies blandit turpis, at placerat ante suscipit ac. Phasellus nisl mi, viverra sed convallis ac, pharetra et dolor. Proin condimentum nec tortor quis lacinia. Ut et aliquet ligula, a porta metus. Curabitur sed mi et ligula posuere gravida. Maecenas congue fermentum viverra.
"""
    print(RexExample.buscar(text))