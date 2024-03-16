# Main

import time

from modulos.descompresion import descomprimir_archivo, integrar_csv_en_dataframe, integrar_csv_en_diccionario
from modulos.procesamiento import procesamiento
from modulos.filtrado import filtrado
from modulos.analisis_grafico import analisis_grafico


# Rutas de la carpeta que contiene los archivos CSV
ruta_carpeta_data = 'data'
ruta_tmdb_zip = 'TMDB.zip'

# Descomprimiendo archivo
descomprimir_archivo(f'{ruta_carpeta_data}/{ruta_tmdb_zip}')

# Medir el tiempo de procesamiento
inicio_tiempo = time.time()

# Obtener el DataFrame integrado llamando a la función
df = integrar_csv_en_dataframe(ruta_carpeta_data)

# Calcular el tiempo de procesamiento
tiempo_procesamiento = time.time() - inicio_tiempo
print(f'Tiempo de procesamiento: {tiempo_procesamiento:.2f} segundos')

# Medir el tiempo de procesamiento
inicio_tiempo = time.time()

# Obtener el diccionario integrado
diccionario_resultante = integrar_csv_en_diccionario(ruta_carpeta_data)

# Calcular el tiempo de procesamiento
tiempo_procesamiento = time.time() - inicio_tiempo
print(f'Tiempo de procesamiento: {tiempo_procesamiento:.2f} segundos')

# Mostrar las primeras 5 claves y valores del diccionario resultante
print('Primeras 5 claves y valores del diccionario resultante:')
for key, value in list(diccionario_resultante.items())[:5]:
    print(f'Clave: {key}, Valores: {value}')

procesamiento(df)

filtrado(df)

analisis_grafico(df)
