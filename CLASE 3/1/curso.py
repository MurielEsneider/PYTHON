from alumno import Alumno

class Curso():
    
    def __init__(self, nombre: str)->None:
        self.__nombre = nombre
        self.__alumnos: []
    
    def matricularAlumno(self, alumno)->None:
        self.__alumnos.append(alumno)
        
    def anularMatricula(self,alumno)->None:
        self.__alumnos.remove(alumno)
        
    def getNombre(self)->str:
        return self.__nombre
    
    def getAlumnos(self)->List:
        return self.__alumnos

