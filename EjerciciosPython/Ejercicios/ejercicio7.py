numero1 = int(input("Ingresa primer número: "))
numero2 = int(input("Ingresa segundo número: "))

if numero1 < numero2:

    for x in range(numero1,(numero2+1)):
        if x%2 == 0:
            print(f"{x} ES PAR")
        else:
            print(f"{x} ES IMPAR")        

else:
    print("El número 1 debe ser mayor al número 2")    