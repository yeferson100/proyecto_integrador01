from fastapi import FastAPI

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
from modelo import get_recomendacion

app = FastAPI()

#http://127.0.0.1:8000/

@app.get("/")
def index():
    return "Hola_Mundo"

data=pd.read_csv('datos.csv')
data1 = pd.read_csv("modelo.csv")

#Instanciar el modelo TF-IDF
tfidf = TfidfVectorizer(stop_words='english')

#Crear la matriz TF-IDF
tfidf_matrix = tfidf.fit_transform(data1['tags'])
nn_model = NearestNeighbors(metric='cosine')
nn_model.fit(tfidf_matrix)

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
    




    top_peliculas= get_recomendacion(nombre_pelicula, nn_model, data1)
    return top_peliculas

if __name__ == "__main__":
    import uvicorn   # Biblioteca de python que ejecutará y servirá a la aplicación FastAPi
    # Recibe las solictudes HTTP entrantes y enruta a la aplicación FastApi
    uvicorn.run(app, host="0.0.0.0", port=10000)