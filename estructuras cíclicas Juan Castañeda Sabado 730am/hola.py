    # _______________________________________________ EJERCICIO 1
# num1 = int (input("ingrese el numero del que quiere ver la tabla de multiplicar"))

# for i  in range (0,11):
#     resultado = i*num1
#     print(num1,"X",i, "=", resultado)

    # _______________________________________________ EJERCICIO 2


# num2 = int (input("ingrese el numero del que quiere ver la tabla de potencia"))
# print("la tabla de potencia del numero ",num2," es:")
# for i  in range (1,10+1):
#     resultado = num2**i
#     print(resultado)

 # _______________________________________________  EJERCICIO 3


# num3 = int (input("ingrese un numero que quiera como limite de impresion ascendente"))
# for i in range (0,num3,+1):
#     print(i)

#___________________________________________________EJERCICIO 4
# num4 = int (input("ingrese un numero que quiera como limite de impresiones descendente "))
# num5 = int (input("ingrese el numero que quiera para iniciar la cuenta "))
# for i in range (num5,num5-num4,-1):
#     print(i)
#___________________________________________________EJERCICIO 5

# num6 = int (input("ingrese el numero par que quiere alcanzar "))
# for i in range (0,num6 + 1,2):
#     print(i)

#___________________________________________________EJERCICIO 6
# num6 = int (input("ingrese el numero de numeros primos que quiere ver"))
# for nprimo in range (0,num6 + 1):
#     primo = True
#     for i in range (2, int(nprimo**0.5)+1):
#         if nprimo % i == 0:
#             primo = False
#         break
#     if primo:
#         print(nprimo)
#__________________________________________________EJERCICIO 7

# word1 = input("Escriba una palabra")

# for i in range(0,11,+1):
#     print(word1)

#__________________________________________________EJERCICIO 8



# edad = int (input("Escriba su edad"))

# for i in range(1,edad+1,+1):
#     print(i)

#__________________________________________________EJERCICIO 9

# num8 = int (input("Escriba un numero"))

# for i in range(1,num8+1,+2):
#     print(i)
#__________________________________________________EJERCICIO 10

# num8 = int (input("Escriba un numero"))
# print("cuenta regresivas: ", end="")

# for i in range(num8,0,-1):
#     if  i == num8 or i == num8 -1:
#         print(i)
#     else:
#         print(i,end=", ")


 # _________________________________________________ EJERCICIO 11

# inversion = int(input("cuanto dinero se quiere invertir?"))
# intereses = float(input("de cuanto sera el interes?")) 
# años = int(input("durante cuantos años?"))
# interes = inversion*intereses/100
# resultado = inversion + interes * años
# print(resultado)

# def registro():
#     productos = []



#     for i in range(0,8):
#         nRegistro = i+1

 
def create_register(): 
    pedido = [] 
    nuevo_registro = True 
    while nuevo_registro:
         
        nombre = input("Nombre del producto: ")
        valor = float(input("Valor del producto: "))
        tipoP = input("Tipo de producto: ")
        cantidad = int(input("Cantidad del producto: "))

        producto = [nombre,valor,tipoP,cantidad]

        # producto = {"product": {"name": nombre, "value": valor, "typeP": tipoP, "quantity": cantidad}}
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

        








    #     producto.append(productos)
    #     print("Numero de registro " + i)

    #     newRegistro = input("Desea Registrar algo mas?: S/N" )

    #     if newRegistro == 'N':
    #         break

    #     return productos
    
    # prodRegistrado = registro()
    # print("/prodRegistrado")
    # for producto in prodRegistrado:
    #     print(producto)
