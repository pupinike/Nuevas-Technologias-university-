pares = 0
impares = 0
listado = []

for i in range(400):
    numero = i
    
    if numero % 2 == 0:
        resultado = "par"
        pares += 1
    else:
        resultado = "impar"
        impares += 1

    listado.append(f"Número {numero}: {resultado}")

for linea in listado:
    print()

print(f"Total de números pares: {pares}")
print(f"Total de números impares: {impares}")