import csv

def convertir_numero_entero_seguro(value):
    '''
        Funcion para convertir seguro un valor a un numero entero
        value: number
        return Numero entero en caso de error devuelve None
    '''
    try:
        value = int(value)
    except ValueError: 
        value = None
    return value


def cargar_archivo_csv(nombre_archivo):
    '''
        Funcion para leer una ruta que contiene archivo csv.
        nombre_archivo: str con ruta de directorio archivo
        return lista con valores del archivo csv
    '''
    with open(nombre_archivo,'r') as archivo:
        lector = csv.DictReader(archivo)
        return list(lector)
    
def limpiar_datos(data):
    for fila in data:
        fila['edad'] = convertir_numero_entero_seguro(fila['edad'])
        fila['horas_estudio_semanal'] = convertir_numero_entero_seguro(fila['horas_estudio_semanal'])
    return data

def calcular_estadistica(data):
    '''
        Funcion que registra informacion basica sobre los datos
        data: lista de diccionario con datos
        return: diccionario con informacion relevante de los dats
    '''
    edades_validas = [fila['edad'] for fila in data if fila['edad']is not None]
    horas_estudio_validas = [fila['horas_estudio_semanal'] for fila in data if fila['horas_estudio_semanal'] is not None]
    diccionario = {'total_estudiantes': len(data),
                   'edad_promedio': sum(edades_validas)/ len(data),
                   'horas_promedio': sum(edades_validas)/ len(data),
                   'registros_cont_edad_invalida':len(data)- edades_validas.count(None),
                   'registros_cont_horas_invalidas': len(data)-horas_estudio_validas.count(None)}
    return diccionario

def filtrar_lenguaje_programacion(data, lenguaje):
    '''
    Funcion que permite filtrar la data por algun tipo de lenguaje
    data: lista de diccionario con datos,  lenguaje: string
    return lista diccionarios filtrada
    '''
    return [fila for fila in data if fila['lenguaje_favorito']==lenguaje]

def guardar_archivo(estudiantes_filtrados, nombre):
    '''
    Funcion para guardar archiov
    '''
    with open(nombre,'w',newline="") as archivo:
        columnas = ["nombre", "edad", "lenguaje_favorito", "horas_estudio_semanal"]
        escritor = csv.DictWriter(archivo, fieldnames=columnas)
        escritor.writeheader()
        escritor.writerows(estudiantes_filtrados)

def estudiantes_mas_aplicado(data):
    '''
    funcion que devuelve el estudiantes con mayor cantidad de horas de estudio:
    return lista con estudiante con mayor horas estudiadas
    '''
    horas =[fila['horas_estudio_semanal'] for fila in data if fila['horas_estudio_semanal'] is not None]
    mayor_horas = [fila for fila in data if fila['horas_estudio_semanal'] == max(horas)]
    return mayor_horas

estudiantes = cargar_archivo_csv("estudiantes_grande.csv")
estudiantes = limpiar_datos(estudiantes)

stats = calcular_estadistica(estudiantes)
for clave, valor in stats.items():
    print(f"{clave}: {valor}")

estudiantes_python = filtrar_lenguaje_programacion(estudiantes, "Python")
print(f"\nEstudiantes que usan Python: {len(estudiantes_python)}")

estudiante_mad_dedicado = estudiantes_mas_aplicado(estudiantes)
print(f'Estudiante mas dedicado {estudiante_mad_dedicado}')

guardar_archivo(estudiantes_python, "reporte_python.csv")
print("\n✅ Reporte generado: reporte_python.csv")