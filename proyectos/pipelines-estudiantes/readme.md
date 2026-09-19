# Pipeline de Análisis de Estudiantes

Script en Python puro (sin librerías externas) que procesa un dataset de estudiantes con datos "sucios" (valores faltantes o inválidos), calcula estadísticas y exporta un reporte filtrado.

## Qué hace

1. Carga datos desde un archivo CSV
2. Limpia valores inválidos o faltantes sin detener la ejecución (manejo de errores con `try/except`)
3. Calcula estadísticas generales (promedios, conteo de errores)
4. Filtra estudiantes según un criterio (lenguaje de programación favorito)
5. Exporta un reporte limpio a un nuevo CSV

## Cómo ejecutarlo

```bash
python main.py
```

## Tecnologías

- Python 3
- Módulo `csv` de la librería estándar

## Aprendizajes aplicados

Este proyecto fue construido como cierre de la Semana 2 de mi programa de estudio en Data Science, aplicando: listas, diccionarios, comprensión de listas, manejo de archivos y manejo de excepciones.