import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors

from fastapi import FastAPI

import uvicorn


data = pd.read_csv("modelo.csv")


#Instanciar el modelo TF-IDF
tfidf = TfidfVectorizer(stop_words='english')

#Crear la matriz TF-IDF
tfidf_matrix = tfidf.fit_transform(data['tags'])

#Crear el modelo Nearest Neighbors
n_neighbors = 5 # Número de vecinos más cercanos a buscar
nn_model = NearestNeighbors(metric='cosine')
nn_model.fit(tfidf_matrix)

def get_recomendacion(title, nn_model, data, top_n=5):
    # Obtener el índice de la película que coincide con el título
    index_id = data[data['title'] == title].index[0]

    # Obtener los índices y las distancias de los vecinos más cercanos a la película en cuestión
    distances, neighbor_indices = nn_model.kneighbors(tfidf_matrix[index_id], n_neighbors=n_neighbors+1)
    neighbor_indices = neighbor_indices.flatten()

    # Devolver los títulos de las películas más similares (hasta top_n)
    top_peliculas = data['title'].iloc[neighbor_indices[1:top_n+1]].tolist()
    return top_peliculas