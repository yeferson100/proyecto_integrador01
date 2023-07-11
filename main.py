from fastapi import FastAPI
import pandas as pd
from modelo import get_recomendacion

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
    return {'Peliculas': num,
            'Idioma': Idioma}

@app.get("/peliculas_duraction/{Pelicula}")
def pelicula_duraction(Pelicula):
    info=data.loc[data['title']==Pelicula, ['runtime','release_year']]
    if not info.empty:
        return {'Titulo':Pelicula,
            'Duracion':int(info['runtime']),
            'Estreno': int(info['release_year'])}
    else:
        return {'Titulo':Pelicula,
            'Duracion':0,
            'Estreno': None}

@app.get("/franquicia/{Franquicia}")
def franquicia(Franquicia):
    info=data.loc[data['franquicia']==Franquicia, ['title','return']]
    return {'Franquicia':Franquicia,
            'NumeroPeliculas:':info.shape[0],
            'GananciasTotales':info['return'].sum(),
            'GananciasPromedio':(info['return'].sum())/info.shape[0]}

@app.get("/peliculas_pais/{Pais}")
def peliculas_pais(Pais: str):
    movies = 0
    for x in data['pais_prod']:
        if Pais in x:
            movies +=1
    
    return {'Peliculas':movies,
            'Pais':Pais}

@app.get("/productora/{Productora}")
def productora(Productora: str):
    
    info = data[data['company'].str.contains(Productora, na=False, case=False)]
    recaudo = int(info['revenue'].sum())

    return {'Productora':Productora,
            'Peliculas':len(info),
            'RecaudoTotal':recaudo}

@app.get("/get_director/{Director}")
def get_director(Director: str):
    df_prod = data[data['directors'].apply(lambda x: Director in x)]

    return {'Director':Director,
            'Cantidad Peliculas':len(df_prod),
            'Retorno Total':df_prod['return'].sum(),
            'Peliculas':[{
                'Titulos': df_prod['title'].tolist(),
                'Estreno': df_prod['release_year'].tolist(),
                'Retorno': df_prod['return'].tolist(),
                'Ganancias': df_prod['revenue'].tolist()
            }]}

@app.get('/recomendacion/{nombre_pelicula}')
def recomendacion(nombre_pelicula: str):

    top_peliculas= get_recomendacion(nombre_pelicula)
    return top_peliculas