numero = int(input("Ingrese número entero para obtener su binario: "))

binario = ""

while True:
    resultado = numero // 2
    residuo = numero % 2
    binario = str(residuo) + binario
    if resultado == 1:
        binario = str(resultado) + binario
        break
    numero = resultado

print("Binario resultante: ")
for i in range(len(binario) - 1, -1, -1):
    print(binario[i], end="")
