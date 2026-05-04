"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


def pregunta_03():
    """
    ¿Cuál es la cantidad de registros por cada letra de la columna `c1` del
    archivo `tbl0.tsv`?

    Rta/
    c1
    A     8
    B     7
    C     5
    D     6
    E    14
    Name: count, dtype: int64

    """
    import pandas as pd
    
    # Leer el archivo TSV
    df = pd.read_csv('files/input/tbl0.tsv', sep='\t')
    
    # Contar la frecuencia de cada valor en la columna c1
    resultado = df['c1'].value_counts().sort_index()
    
    return resultado
