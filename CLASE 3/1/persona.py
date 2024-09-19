class Persona():
    def __init__(self, identificacion: str = "15", nombre: str="Juan", correo: str="juan@gmail.com") -> None:
        """_summary_

        Args:
            identificacion (_type_): _description_
            nombre (_type_): _description_
            correo (_type_): _description_
        """
        self.__indetificacion = identificacion
        self.__nombre = nombre
        self.__correo = correo
    
    def getIdentificacion(self)->str:
        return self.__indetificacion
    
    def getNombre(self)->str:
        return self.__nombre
    
    def getCorreo(self)->str:
        return self.__correo
    
    def setIdentificacion(self, identificacion)->None:
        self.__identificacion = identificacion
        
    def setNombre(self, nombre)->None:
        self.__nombre = nombre
    
    def setCorreo(self,correo)->None:
        self.__correo = correo
        

    def saludar(self):
        print(f"Desde Instructor. Hola soy tipo {type(self).__name__}")
    
    
    
    
