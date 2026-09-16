import csv

def promedio(valor):
    return round(sum(valor)/len(valor),2)

with open("estudiantes.csv", "r") as archivo:
    lector = csv.DictReader(archivo)
    estudiantes = list(lector)   # una sola lectura, guardada en memoria

# Ahora trabajas sobre 'estudiantes', sin volver a tocar el archivo
edades = [int(fila["edad"]) for fila in estudiantes]
promedio_estudiantes = promedio(edades)
    

## Estudiantes de python

with open('estudiantes.csv', 'r') as sheets:
    lector = csv.DictReader(sheets)
    nombre_estudiantes_python = [fila['nombre'] for fila in lector if fila["lenguaje_favorito"]=='Python']

 # promedio estudiantes       
promedio_estudiantes = promedio(edades)


#filtrando estudiantes de python
estudiantes_python = []
with open('estudiantes.csv', 'r') as sheets:   
    lector = csv.DictReader(sheets)
    for fila in lector:
        if fila['lenguaje_favorito'] == 'Python':
            estudiantes_python.append(fila)

print(f'El promedio de edad de todos los estudiantes es de: {promedio_estudiantes}')
# creando archivo nuevo con estudiantes de python.
with open("estudiantes_python.csv", "w", newline="") as archivo:
    columnas = ["nombre", "edad", "lenguaje_favorito"]
    escritor = csv.DictWriter(archivo, fieldnames=columnas)
    escritor.writeheader()
    escritor.writerows(estudiantes_python)