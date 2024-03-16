## Data Analytics-Movie Database

Realizado por **Renato Díaz**

# Índice

1. [Introducción](#introducción)
2. [Objetivo](#objetivo)
3. [Estructura](#estructura) 
4. [Metodología](#metodología)
5. [Requisitos previos y ejecución](#requisitos-previos-y-ejecución)
6. [Conclusiones](#conclusiones)

## Introducción
   En este proyecto analizamos el contenido de la base de datos The Movie Database (TMDB), que contiene información de más de 159.000 programas de televisión. 

## Objetivo
   - El objetivo es que la compañía de medios de comunicación Open Broadcast Corporation tome decisiones informadas con el propósito de  adquirir licencias de emisión de programas de televisión populares con las que espera aumentar significativamente el número de suscriptores. 



## Estructura
- Parte1: Descompresión y lectura de ficheros.
- Parte2: Procesamiento de datos.
- Parte3: Filtrado de datos.
- Parte4: Análisis gráfico.
- Parte5: Conclusiones.

A cada parte del proyecto le corresponde un fichero:
- A la parte 1 le corresponde el fichero descompresion.py. 
- A la parte 2 le corresponde el fichero procesamiento.py. 
- A la parte 3 le corresponde el fichero filtrado.py. 
- A la parte 4 le corresponde el fichero analisis_grafico.py. 
- A la parte 5 le corresponde el fichero conclusiones.py. Como la este apartado es un breve informe de las conclusiones también lo podemos encontrar en las conclusiones de este README. 


## Metodología
   - El proyecto se desarrolla en un entorno virtual para evitar conflictos con otras versiones de las bibliotecas.
   - Cada parte del proyecto se encuentra en su respectivo módulo .py.
   - El fichero principal es main.py desde el que importamos de los diferentes módulos las funciones utilizadas. 
   - La carpeta data contiene los datasets comprimidos en un archivo .zip y a su vez contendrá los archivos csv que se descomprimen al ejecutar el programa.
   - La carpeta img contendrá las imágenes obtenidas al ejecutar la parte 4 denominada análisis gráfico.

## Requisitos previos y ejecución
- Comenzaremos creando un entorno virtual de trabajo utilizando los siguientes comandos en una terminal:

py -m venv venv | Otras opciones en lugar de py pueden ser python o python3.

- Activamos el entorno con uno de estos tres comandos:

source venv/Scripts/activate
source venv\Scripts\activate
source venv/bin/activate | Linux y Mac

- Por último instalamos las dependencias necesarias para la ejecución del proyecto:

pip install -r requirements.txt.

- Ejecuta todo el proyecto con el siguiente comando dentro de la terminal:
python main.py

- También se pueden ejecutar por separado los archivos planos con los siguientes comandos:
- python descompresion.py
- python procesamiento.py
- python filtrado.py
- python analisis_grafico.py

## Conclusiones
   - Podemos concluir lo siguiente:
* Pandas es más eficiente para integrar los csv de este proyecto.
* CBS Evening News es el programa que ha estado más días en el aire. Siendo su primera emisión el 1941-07-01. 
Le sigue el Concierto anual de la filarmónica de Viena y los Golden Globe Awards.
* Los programas de la categoría Scripted son los que más se han producido desde la década de 1940. Pero entre el 2010
y 2020 se redujeron en 10000. 
* El número de series ha crecido de manera exponencial desde la década de 1940 hasta la década del 2010. 
* Los tres géneros más populares son drama, comedia y documental. 

