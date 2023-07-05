from fastapi import FastAPI
import pandas as pd

app = FastAPI()

#http://127.0.0.1:8000/

@app.get("/")
def index():
    return "Hola_Mundo"

data=pd.read_csv('datos.csv')

@app.get("/peliculas_idioma/{Idioma}")
def peliculas_idioma(Idioma : str):
    
    movies = []
    for x in (data['original_language']):
        if Idioma == x: movies.insert(0,x)
    num=len(movies)
    return f"{num} de peliculas fueron encontradas en el idioma {Idioma}"

@app.get("/peliculas_duraction/{Pelicula}")
def pelicula_duraction(Pelicula:str):
    info=data.loc[data['title']==Pelicula, ['runtime','release_year']]
    return f"el Titulo: {Pelicula} tiene una duracion de: {int(info['runtime'])} y estrenada en el año: {int(info['release_year'])}"

@app.get("/franquicia/{Franquicia}")
def franquicia(Franquicia:str):
    info=data.loc[data['franquicia']==Franquicia, ['title','revenue','budget','return']]
    return f"La Franquicia {Franquicia} Tiene {info.shape[0]} Peliculas, con ganacias totales: {info['return'].sum()} y ganancias promedio: {(info['return'].sum())/info.shape[0]} "

@app.get("/peliculas_pais/{Pais}")
def peliculas_pais(Pais: str):
    movies = 0
    for x in data['pais_prod']:
        if Pais in x:
            movies +=1
    return f"peliculas en {Pais} encontradas fueron: {movies}"

@app.get("/productora/{Productora}")
def productora(Productora: str):
    df_prod = data[data['company'].apply(lambda x: Productora in x)]
    recaudo=df_prod['revenue'].sum()  
    return f"peliculas realizadas por {Productora} encontradas fueron: {len(df_prod)} y el recaudo total: {recaudo}"

@app.get("/get_director/{Director}")
def get_director(Director: str):
    df_prod = data[data['directors'].apply(lambda x: Director in x)]
    #print(df_prod)
    exito = list[df_prod[['title','release_date','return','budget','revenue']]]
    return exito