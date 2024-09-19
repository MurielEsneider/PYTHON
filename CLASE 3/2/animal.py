class Animal():
    def __init__(self,nombre,peso: str) -> None:
        self.__nombre = nombre
        self.__peso = []
     
    def getNombre()-> str:
        return self.__nombre
    
    def setNombre()-> str:
        return f"el nombre de el animal es: {Animal.getNombre()}"
    
    def getPeso()-> str:
        return self.__peso
    
    def setPeso()-> str:
        return f"el peso de el animal es: {Animal.getPeso()}"
           