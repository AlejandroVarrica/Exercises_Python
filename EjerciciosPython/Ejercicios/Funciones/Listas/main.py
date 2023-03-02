#peliculas = ["Batman", "Superman", "Acuaman"]

#cantantes = list(("Ozzy","Mustaine","Plant"))

#print(cantantes)

"""
nueva_pelicula = ""
while nueva_pelicula != "parar":

    nueva_pelicula = input("Ingrese nueva pelicula: ")
    
    if nueva_pelicula != "parar":
        peliculas.append(nueva_pelicula)


for pelicula in peliculas:
    print(f"{peliculas.index(pelicula)} . {pelicula}")
"""


contactos = [

    [
        "Antonio" , 
        "antonio@gmail.com"
    ],
    [
        "Luis", 
        "luis@luis.com"  
    ],
    [
        "Alfredo",
        "alfredo@alfredo.com"
    ]

]

for contacto in contactos:
    for elemento in contacto:
        print(elemento)

#print(contactos[1][1])