def Getnombre(nombre):
    texto = f"El nombre es: {nombre}"
    return texto


def Getapellido(apellido):
    texto = f"El apellido es: {apellido}"
    return texto


def devuelveTodo(nombre,apellido):
    texto = Getnombre(nombre) + "\n" + Getapellido(apellido)
    return texto


print(devuelveTodo("Alejandro","Varrica"))