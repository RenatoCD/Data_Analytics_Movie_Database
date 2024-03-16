# Anlásis

import pandas as pd
import matplotlib.pyplot as plt

try:
    from descompresion import integrar_csv_en_dataframe
except ModuleNotFoundError:
    from .descompresion import integrar_csv_en_dataframe


def analisis_grafico(df_final):
    # Convertir las columnas de fechas a tipo datetime
    df_final['first_air_date'] = pd.to_datetime(df_final['first_air_date'])
    df_final['last_air_date'] = pd.to_datetime(df_final['last_air_date'])


    # 4.1
    # Contar el número de series por año de inicio
    conteo_series_por_anio = df_final['first_air_date'].dt.year.value_counts().sort_index()

    # Crear el gráfico de barras
    plt.figure(figsize=(12, 6))
    plt.bar(conteo_series_por_anio.index, conteo_series_por_anio.values, color='skyblue')
    plt.xlabel('Año de inicio')
    plt.ylabel('Número de series')
    plt.title('Número de series por año de inicio')
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Guardar el gráfico como una imagen en la carpeta "img"
    plt.savefig('img/series_por_anio.png')

    # Mostrar el gráfico
    # plt.show() 
    # Desactivé show porque detiene la ejecución del programa. Para demostrar su correcto funcionamiento la 
    # la imagen resultante es guardada en la carpeta img. 


    # 4.2
    # Crear una columna de décadas a partir de la columna 'first_air_date'
    df_final['decade'] = (df_final['first_air_date'].dt.year // 10) * 10

    # Filtrar las series producidas desde 1940
    df_desde_1940 = df_final[df_final['first_air_date'].dt.year >= 1940]

    # Contar el número de series por década y tipo
    conteo_series_por_decada_tipo = df_desde_1940.groupby(['decade', 'type']).size().unstack().fillna(0)

    # Crear el gráfico de líneas
    plt.figure(figsize=(12, 6))
    for tipo in conteo_series_por_decada_tipo.columns:
        plt.plot(conteo_series_por_decada_tipo.index, conteo_series_por_decada_tipo[tipo], label=tipo)

    plt.xlabel('Década')
    plt.ylabel('Número de series')
    plt.title('Número de series por categoría y década desde 1940')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)

    # Guardar el gráfico como una imagen en la carpeta "img"
    plt.savefig('img/tendencia_decada.png')

    # plt.show()
    # 

    # 4.3
    # Eliminar las filas con el campo "genres" vacío
    df_genres = df_final.dropna(subset=['genres'])

    # Dividir los géneros y contar el número de series por género
    conteo_series_por_genero = df_genres['genres'].str.split(', ').explode().value_counts()

    # Calcular el porcentaje respecto al total
    porcentaje_series_por_genero = (conteo_series_por_genero / conteo_series_por_genero.sum()) * 100

    # Filtrar géneros que representan menos del 1% y agruparlos como "Other"
    umbral_porcentaje = 1
    generos_filtrados = porcentaje_series_por_genero[porcentaje_series_por_genero >= umbral_porcentaje]
    generos_filtrados['Other'] = porcentaje_series_por_genero[porcentaje_series_por_genero < umbral_porcentaje].sum()

    # Crear el gráfico circular
    plt.figure(figsize=(10, 10))
    plt.pie(generos_filtrados, labels=generos_filtrados.index, autopct='%1.1f%%', startangle=140)
    plt.title('Porcentaje de series por género')

    # Guardar el gráfico como una imagen en la carpeta "img"
    plt.savefig('img/por_genero.png')
    # plt.show()


if __name__ == '__main__':
    df = integrar_csv_en_dataframe('data')

    analisis_grafico(df)
