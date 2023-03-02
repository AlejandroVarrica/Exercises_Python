"""
def muestra_nombre():
    print("Alejandro")
    print("Leandro")
    print("Pedro")
    print("Julia")
    print("Luis")

muestra_nombre()
"""    





def mostrartunombre(nombre, edad):
    print(f"Tu nombre es: {nombre}")

    if edad >= 18:
       print("Eres mayor de edad.")
           
nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))
mostrartunombre(nombre, edad)