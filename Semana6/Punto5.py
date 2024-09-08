for i in range(1, 407):
    pc = int (input(f"Cabina {i}: "))
    if pc <= 2:
        print("Defectuoso")
    elif  pc == 3:
        print("Aceptable")
    elif  pc == 4:
        print("Optimo")
