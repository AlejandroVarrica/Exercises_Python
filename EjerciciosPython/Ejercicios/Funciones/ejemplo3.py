
def tabla(numero):
    print(f"Table de multiplicar del número: {numero}")
    for contador in range(11):
        operacion = numero * contador
        print(f"{numero} X {contador} = {operacion}")

    print("\n")


tabla(5)        


for numero_tabla in range(1,11):
    tabla(numero_tabla)