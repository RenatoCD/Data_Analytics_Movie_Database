# Descompresion

import os
import zipfile
import tarfile
import pandas as pd
import csv


#Ejercicio 1. 1
def descomprimir_archivo(ruta_archivo):
    """
    Descomprime un archivo zip o tar.gz.

    Parameters:
    - ruta_archivo (str): Ruta del archivo que se desea descomprimir.

    Returns:
    - None
    """
    # Obtener la extensión del archivo
    _, extension = os.path.splitext(ruta_archivo)

    if extension == ".zip":
        with zipfile.ZipFile(ruta_archivo, 'r') as zip_ref:
            zip_ref.extractall(os.path.dirname(ruta_archivo))
        print(f'Archivo {ruta_archivo} descomprimido exitosamente.')

    elif extension == ".tar.gz":
        with tarfile.open(ruta_archivo, 'r:gz') as tar_ref:
            tar_ref.extractall(os.path.dirname(ruta_archivo))
        print(f'Archivo {ruta_archivo} descomprimido exitosamente.')

    else:
        print(f'Error: El archivo {ruta_archivo} no está en formato zip o tar.gz.')


#Ejercicio 1.2 
def integrar_csv_en_dataframe(ruta_carpeta):

    archivos_csv = ["TMDB_distribution.csv", "TMDB_info.csv", "TMDB_overview.csv"]
    df_integrado = None  # Inicializar a None

    for archivo in archivos_csv:
        ruta_archivo = os.path.join(ruta_carpeta, archivo)
        df_temporal = pd.read_csv(ruta_archivo)
        
        # En la primera iteración, asignar df_temporal a df_integrado
        if df_integrado is None:
            df_integrado = df_temporal
        else:
            # En las siguientes iteraciones, realizar el merge
            df_integrado = pd.merge(df_integrado, df_temporal, on='id', how='outer')

    return df_integrado


#1.3
def integrar_csv_en_diccionario(ruta_carpeta_data):

    diccionario_integrado = {}
    archivos_csv = ["TMDB_distribution.csv", "TMDB_info.csv", "TMDB_overview.csv"]

    for archivo in archivos_csv:
        ruta_archivo = os.path.join(ruta_carpeta_data, archivo)

        with open(ruta_archivo, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                id_valor = row['id']
                diccionario_interno = {k: v for k, v in row.items() if k != 'id'}
                diccionario_integrado.setdefault(id_valor, {}).update(diccionario_interno)

    return diccionario_integrado


#Ejercicio 1.4
""" 
La diferencia fundamental es que con Pandas es más rápida la ejecución de la función. 
Esto es debido a que Pandas está optimizado para operaciones con datos tubulares. 
Mientras que la lectura de archivos CSV con csv.DictReader y la iteración sobre las filas es más lenta. 
En la función con Pandas, Pandas opera directamente sobre la estructura tabular mientras que en la otra función 
debemos construir y actualizar diccionarios. 
Además, sabemos que Pandas tiene mecanismos internos para administar con eficiencia la memoria. 
Para un mejor rendimiento de conjuntos de datos grandes como ficheros de 10 GB utilizar Pandas es más eficiente 
porque está optimizado para este volumen de datos en forma tabular. """


if __name__ == '__main__':
    # Rutas de la carpeta que contiene los archivos CSV
    ruta_carpeta_data = 'data'
    ruta_tmdb_zip = 'TMDB.zip'

    descomprimir_archivo(f'{ruta_carpeta_data}/{ruta_tmdb_zip}')
    print(integrar_csv_en_dataframe(f'{ruta_carpeta_data}'))
    print(integrar_csv_en_diccionario(f'{ruta_carpeta_data}'))
