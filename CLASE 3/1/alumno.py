class Alumno():
    def __init__(self,nombre: str, edad: int) -> None:
        self.__nombre = nombre
        self.__edad = edad
        
            
    def getNombre(self)-> str:
        return self.__nombre
    
    def getEdad(self)->int:
        return self.__edad
    
    def setNombre (self, nombre)->None:
        self.__nombre = nombre
        
    def setEdad(self,edad)-> None:
        self.__edad = edad
    
    del __str__(self) -> str:
        return self.