
"""
personas = {
    "nombre":"Alejandro",
    "apellidos":"Varrica",
    "email":"varrica@varrica.com"

}

print(personas["apellidos"])
"""
contactos = [
        {
            "nombre":"Alberto",
            "apellido":"Lopez",
            "dirección":"Juncal 1600"
        },
        {
            "nombre":"Damian",
            "apellido": "Gomez",
            "dirección":"Buenos Aires 1000"
        },
        {
            "nombre":"Salvador",
            "apellido":"Varrica",
        },


]

for contacto in contactos:
    print(f"Nombre del contacto: {contacto ['nombre']}")