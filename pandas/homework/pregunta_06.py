"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


def pregunta_06():
    """
    Retorne una lista con los valores unicos de la columna `c4` del archivo
    `tbl1.csv` en mayusculas y ordenados alfabéticamente.

    Rta/
    ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    """
    import pandas as pd
    
    # Leer el archivo TSV (nota: el archivo es tbl1.tsv, no tbl1.csv)
    df = pd.read_csv('files/input/tbl1.tsv', sep='\t')
    
    # Obtener valores únicos de c4, convertir a mayúsculas y ordenar
    valores_unicos = df['c4'].unique()
    valores_mayusculas = [valor.upper() for valor in valores_unicos]
    resultado = sorted(valores_mayusculas)
    
    return resultado
