edades = []

for i in range(5):
    edad = int(input("Ingrese edad de la persona: "))
    edades.append(edad)

menor = min(edades)
mayor = max(edades)

print(f"La mayor edad es {mayor}")
print(f"La menor edad es {menor}")

