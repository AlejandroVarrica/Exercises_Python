"""
contador = 1
muestrame = str(0)
while contador <= 100:
    muestrame = muestrame + " , " + str(contador) 
    contador += 1
print(muestrame)
"""

contador = 1

for contador in range(0,121):
    if contador%2 == 0:
        print(f"{contador} es par")
    else:
        print(f"{contador} en impar")    