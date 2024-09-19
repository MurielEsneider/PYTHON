import math

def areaCuadrado(lado: float) -> float:
    return lado * lado

def areaCirculo(radio: float) -> float:
    return math.pi * radio**2

def areaTriangulo(base: float, altura: float) -> float:
    return base * altura / 2

# Cálculos
areaC = areaCuadrado(5.8)
areaCir = areaCirculo(3.8)
areaTri = areaTriangulo(5.8, 8.5)

print(f"El área del cuadrado con lado 5.8 es: {areaC}")
print(f"El área del círculo con radio 3.8 es: {areaCir}")
print(f"El área del triángulo con base 5.8 y altura 8.5 es: {areaTri}")

def operaciones():
    x = 5
    y = 8
    print(f"La suma de {x} y {y} es: {x + y}")

operaciones()
