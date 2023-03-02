def calculadora (numero1,numero2,basicas=False):
    suma = numero1 + numero2
    resta = numero1 - numero2
    multi = numero1 * numero2
    divi = numero1 / numero2

    cadena = ""
    
    if basicas != False:    
    
        cadena += "Suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta: " + str(resta)
        cadena += "\n"
    else:    
        cadena += "Multiplicación: " + str(multi)
        cadena += "\n"
        cadena += "División: " + str(divi)

    return cadena



print(calculadora(56,5,False))