# Procesamiento

import pandas as pd

try:
    from descompresion import integrar_csv_en_dataframe
except ModuleNotFoundError:
    from .descompresion import integrar_csv_en_dataframe


def procesamiento(df_final):
    # 2.1 
    # Convertir las columnas de fechas a tipo datetime
    df_final['first_air_date'] = pd.to_datetime(df_final['first_air_date'])
    df_final['last_air_date'] = pd.to_datetime(df_final['last_air_date'])

    # Calcular la variable air_days
    df_final['air_days'] = (df_final['last_air_date'] - df_final['first_air_date']).dt.days

    # Mostrar los 10 registros del dataset que más días han estado en emisión
    top_10_air_days = df_final.nlargest(10, 'air_days')
    print(top_10_air_days[['name', 'first_air_date', 'last_air_date', 'air_days']])


    # 2.2
    # Crea un diccionario
    diccionario_posters = {}

    # Iterar sobre las filas del DataFrame df_final
    for _, row in df_final.iterrows():
        nombre_serie = row['name']
        homepage = row['homepage']
        poster_path = row['poster_path']

        # Comprobar si homepage o poster_path son NaN o ""
        if pd.isna(homepage) or homepage == "":
            homepage = "NOT AVAILABLE"
        if pd.isna(poster_path) or poster_path == "":
            poster_path = "NOT AVAILABLE"

        # Construir la dirección web completa del poster
        direccion_web_poster = f"{homepage}/{poster_path}"

        # Añadir al diccionario
        diccionario_posters[nombre_serie] = {"homepage": homepage, "poster_path": direccion_web_poster}

    # Mostrar los primeros 5 registros del diccionario
    for key, value in list(diccionario_posters.items())[:5]:
        print(f'Clave: {key}, Valores: {value}')

if __name__ == '__main__':
    df = integrar_csv_en_dataframe('data')

    procesamiento(df)
