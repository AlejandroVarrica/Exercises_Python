#Funciones predefinidas

nombre = "Alejandro Varrica"

print(type(nombre))


comprobar = isinstance(nombre, str)
if comprobar:
    print("Esa variable es un string")
else:
    print("No es un string") 

if not isinstance(nombre, float):
    print("No es un numero decimal")
            