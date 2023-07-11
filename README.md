<h1 align='center' style="font-weight:light; text-align:justify; margin-left: 80px; margin-right: 100px;">
  Desarrollo e Implementacion de un Sistema de Recomendacion de Peliculas
</h1>


<h2 align='center'>
  Proyecto Individual MLoPs
</h2>



## Introducción:

Este proyecto permite realizar consultas por medio de una FastAPI, la cual nos permite realizar consultas sobre un amplio número de películas, las cuales están almacenadas en un dataset de más de 45 mil datos. También se presenta la fase de análisis y pre-procesamiento de datos mediante un análisis estadístico y un EDA que nos permiten conocer de antemano el contenido de la información suministrada. posterior a esto se desarrolla un sistema de recomendación de películas por medio de un Modelo de Aprendizaje (ML).

## Objetivos del proyecto:
---
1. **Implementar un API que permita acceder a la información suministrada por medio de consultas**

2. **Implementar un sistema de recomendación de películas por medio de un Modelo de aprendizaje**

---
## Resumen de los procesos:
---
#### 1.Extracción, Transformación y Carga [ ETL ]

 **ETL.py**. Se entrega la información en dos dataset (**movies.csv** y **credits.csv**), se procede a unir en uno y posteriormente se eliminan datos irrelevantes para el proyecto. datos nulos y se crean nuevas variables de información necesarias para nuestras consultas. dando como resultado un nuevo dataset **datos.csv**

### 2. Implementación de una FastAPI  [main.py ]

Mediante el archivo **main.py**, se implementa una API por medio de las librerías **FastAPI y Uvicorn**. Por medio de esta API se podrá consumir tanto nuestras consultas como nuestro sistema de recomendación.

### 3. Análisis Exploratorio de Datos [ EDA ]

**EDA.ipynb** .En esta parte se lleva a cabo un análisis estadístico del dataset, esto con el fin de tener un conocimiento más afondo de los diferentes datos, sus relaciones entre sí. por medio de estadística descriptiva, diagramas de barras, histogramas, outliers, correlaciones para así determinar qué información es la más adecuada para llevar a cabo nuestro sistema de recomendación. tambien hace parte de este el pre-procesamiento de datos. por el cual solo se toma el 'overview','comapñia productora' y 'directores' como informacion relevante para entrenar el modelo.


### 4. Desarrollo del Modelo de Machine Learning [modelo.py ]

**model.py** .En este archivo se encuentra la implementacion de un modelo de Nearest Neighbors para la clasificacion y una matriz TF-IDF para determinar la similitud entre datos por medio de la similitud de coseno.

## Aspectos a Tener en cuenta en la FastAPI

- para la Funciones  que requieren titulo de la pelicula ingresar la primera letra de cada palabra en mayusculas. ej:'Toy Story'
- 
- En la función 'peliculas_idioma', ingresar las abreviaturas del idioma. ej: "inglés" --> "en", "italiano" --> "it".

## Links

- [FastAPI para el consumo de la informacion](https://movies-recomendation-system-bgw9.onrender.com/docs#/)
- [Videotutorial del trabajo realizado en YouTube](#)



## Desarrollado por

Yeferson Narvaez

- yef.narvaez@gmail.com
