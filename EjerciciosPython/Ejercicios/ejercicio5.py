numero1 = int(input("Ingrese primer número: "))
numero2 = int(input("Ingrese segundo número: "))

if numero1 < numero2:

    for contador in range(numero1, (numero2 + 1)):
        print(contador)

else:
    print("El numero 1 debe ser menor al numero 2")
