"""
contador = 0
resultado = 0

for contador in range (0,10+1):
    print("voy por el "+str(contador))

    resultado += contador
print(resultado)    
"""

numero_usario = int(input("¿De que numero quieres ver la tabla? "))

if numero_usario < 1:
    numero_usario = 1
print(f"Tabla de multiplicar {numero_usario}")

for numero_tabla in range(0,10+1):
    print(f"{numero_usario} x {numero_tabla} = {numero_usario*numero_tabla}")
else:
    print("La tabla se ha terminado")
        
    
