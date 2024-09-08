# Crear un algoritmo, que permita solicitar mínimo 5 registros de  productos de un mercado, con las siguientes características: nombre, valor, tipo producto y cantidad.​
# Nota: El ejercicio se debe hacer en python, debe tener una función y deben incluir alguno de los elementos (listas, tuplas o diccionarios)

def create_register(): 
    pedido = [] 
    nuevo_registro = True 
    while nuevo_registro:
         
        nombre = input("Nombre del producto: ")
        valor = float(input("Valor del producto: "))
        tipoP = input("Tipo de producto: ")
        cantidad = int(input("Cantidad del producto: "))

        producto = [nombre,valor,tipoP,cantidad]

        pedido.append(producto)

        repeat = input("Quiere añadir un nuevo producto? s/n")
        if repeat != 's':
            nuevo_registro = False

    return pedido

crear = input("crear un pedido?")

if crear == 's':
    mostrar_pedido = create_register()
    for producto in mostrar_pedido:
        
        print(producto[0])
        print(producto[1])
        print(producto[2])
        print(producto[3])
