"""
contador = 1

while contador <= 100:
    print(f"Voy por el número {contador}")
    contador += 1
"""

"""
contador = 1
muestrame = str(0)
while contador <= 100:
    muestrame = muestrame + " , " + str(contador) 
    contador += 1
print(muestrame)    
"""

numero_usuario = int(input("¿De que numero quieres la tabla?"))


if numero_usuario < 1:
    numero_usuario = 1
print(f"Tabla del {numero_usuario}") 

contador = 1

while contador <=10:
    print(f"{numero_usuario} x {contador} = {numero_usuario*contador}") 
    contador += 1