""" """
""" from perro import Perro

perro1 = Perro("Tango","Beagle")

perro2 = Perro("Apolo", "Lobo")

perro1.caminar(10) """
"""

from persona import Persona

per = Persona(11, "Pedro", "peter@yahoo.com")

print(per.getIdentificacion())

per.setIdentificacion(111)

print(per.getIdentificacion())

per2 = Persona()

print(per.getNombre())

per3 = Persona(nombre= "Rosa",correo= "rosa@gmail.com", identificacion="2323") 

per4 = Persona ("23", "Maria","maria@sena.edu.co")

aprendiz = aprendiz(320, "99", "Maria Pinto", "marco@etc.com")
aprendiz(getIdentificacion())
aprendiz.setIdentificacion("100")
print(aprendiz.getIdentificacion())

aprendiz.setPuntajeIcfes(380)

aprendiz.saludar() """
""" 
from alumno import Alumno
from curso import Curso

unCurso = Curso("Desarrollo web en python")

alumno1 = Alumno("Maria", 18)
alumno2 = Alumno("Pedro", 21)
alumno3 = Alumno("Erick", 25)

unCurso.matricularAlumno(alumno1)
unCurso.matricularAlumno(alumno2)
unCurso.matricularAlumno(alumno3)

print(f"Curso: {unCurso.getNombre()}")
print(f"Relacionde alumnos")
alumnos = unCurso.getAlumnos()
for alumno in alumnos:
    print(alumno.getNombre())
    print(a.getEdad())
 """

from empleado import Empleado
from empresa import Empresa

elSENA = Empresa("SENA")

elSENA.agregarEmpleado("martin","director",20000)
elSENA.agregarEmpleado("Pablo Ortiz", "Instructor",60000)
elSENA.agregarEmpleado("Monika", "tesorero", 300000)

print(f"Lista de Empleado de la empresa {elSENA()}")

for empleado in elSENA.getEmpleados():
    print (empleado)
    
del elSENA

for empleado