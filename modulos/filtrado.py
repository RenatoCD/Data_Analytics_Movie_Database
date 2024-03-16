# Filtrado


# Obtenía continuamente error en la importación, así que lo resolví con un try y un except 
try:
    from descompresion import integrar_csv_en_dataframe
except ModuleNotFoundError:
    from .descompresion import integrar_csv_en_dataframe


def filtrado(df_final):
    #Ejercicio 3.1
    
    # Filtrar el DataFrame para obtener las series en inglés con palabras "mystery" o "crime" en el resumen
    series_interesantes = df_final[(df_final['original_language'] == 'en') & 
                                (df_final['overview'].str.contains('mystery|crime', case=False))]

    # Mostrar los nombres de las series
    nombres_series_interesantes = series_interesantes['name'].tolist()
    print("Nombres de las series en inglés con 'mystery' o 'crime' en el resumen:")
    for nombre in nombres_series_interesantes:
        print(nombre)


    #3.2
    
    # Filtrar el DataFrame para obtener las series que han empezado en 2023 y han sido canceladas
    series_canceladas_2023 = df_final[(df_final['status'] == 'Canceled') & 
                                  (df_final['first_air_date'].dt.year == 2023)]

    # Mostrar los primeros 20 elementos de la lista
    print("Series que han empezado en 2023 y han sido canceladas (primeros 20 elementos):")
    print(series_canceladas_2023['name'].head(20).tolist())



    # Ejercicio 3.3

    # Filtrar el DataFrame para obtener las series en japonés
    series_japonesas = df_final[df_final['languages'].str.contains('ja', case=False, na=False)]

    # Seleccionar las columnas requeridas
    columnas_seleccionadas = ['name', 'original_name', 'networks', 'production_companies', 'languages']
    df_series_japonesas = series_japonesas[columnas_seleccionadas]

    # Mostrar los primeros 20 registros por pantalla
    print("Primeros 20 registros de series en japonés:")
    print(df_series_japonesas.head(20))


if __name__ == '__main__':
    df = integrar_csv_en_dataframe('data')

    filtrado(df)
