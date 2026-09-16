import csv

def convertir_edad_segura(value):
    '''
    Funcion para convertir valor a numero entero
    value: number value
    return: valor si numero es valido, en otro caso None
    '''
    try:
        value = int(value)
    except ValueError:
        value = None
    return value

with open('estudiantes.csv','r') as archivo:
    lector = csv.DictReader(archivo)
    estudiantes = list(lector)
edades =[convertir_edad_segura(fila['edad']) for fila in estudiantes ]
print(f'La cantidad de numeros mal ingresados es de: {edades.count(None)}')