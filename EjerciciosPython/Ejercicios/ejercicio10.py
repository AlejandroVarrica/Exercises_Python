

contador = 1
aprobados = 0
suspendidos = 0

numero_alumnos = int(input("¿Cuantos alumnos tienen?: "))

while contador <= numero_alumnos:
    nota = int(input(f"¿Que nota tiene el \"alumno {contador}\"?"))

    if nota >= 5:
        aprobados += 1
        
    else:
        suspendidos += 1


    contador += 1                
print(f"Alumnos aprobados: {aprobados}")
print(f"Alumnos suspendidos: {suspendidos}")    