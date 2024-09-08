for i in range(1, 400):
    pc = int (input(f"paciente {i}: "))
    if pc < 10:
        print("no tiene leucemia")
    elif  11<= pc <= 40:
        print("Bajo nivel de leucemia")
    elif  41<= pc <=69:
        print("Moderado nivel de leucemia")
    elif  70 <= pc <=100:
        print("Grave nivel de leucemia")

