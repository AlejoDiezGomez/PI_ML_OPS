# Importamos galerias 
from fastapi import FastAPI
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise        import cosine_similarity
from sklearn.metrics.pairwise        import linear_kernel
from sklearn.feature_extraction.text import TfidfVectorizer
#
app=FastAPI(debug=True)
df = pd.read_csv('DataSet_Final.csv')
@app.get('/')
def message():
    return 'PROYECTO INTEGRADOR ML OPS 01 ALEJO DIEZ GOMEZ (agregar /docs al enlace para acceder a las funciones / add /docs to link to access features)'
# Funcion que obtiene el año de lanzamiento con mas horas jugadas segun el genero / Function that obtains the year of release with the most hours played according to the genre
@app.get('/PlayTimeGenre/')
def PlayTimeGenre(genre: str) -> dict:
    genre = genre.capitalize()
    genre_df = df[df[genre] == 1]
    year_playtime_df = genre_df.groupby('year')['playtime_forever'].sum().reset_index()
    max_playtime_year = year_playtime_df.loc[year_playtime_df['playtime_forever'].idxmax(), 'year']
    return {"Género": genre, "Año de lanzamiento con más horas jugadas para Género :": int(max_playtime_year)}
# Funcion que obtiene el usuria con mas horas jugadas en el genero / Function that the user with the most hours played in the genre obtains
@app.get('/UserForGenre/')
def UserForGenre(genre: str) -> dict:
    genre = genre.capitalize()
    genre_df = df[df[genre] == 1]
    max_playtime_user = genre_df.loc[genre_df['playtime_forever'].idxmax(), 'user_id']
    year_playtime_df = genre_df.groupby('year')['playtime_forever'].sum().reset_index()
    playtime_list = year_playtime_df.to_dict(orient='records')
    result = {
        "Usuario con más horas jugadas para Género " + genre: max_playtime_user,
        "Horas jugadas": playtime_list}
    return result
 
# Funcion que devuelve top 3 juegos recomendados por usuarios segun el año y el sentiment score  / Function that returns top 3 games recommended by users according to the year and the sentiment score

@app.get('/UsersRecommend/')
def UsersRecommend(year: int) -> dict:
    df_filtrado = df[(df['year'] == year) & (df['recommend'] == True) & (df['sentiment_score'] >= 1)]
    if df_filtrado.empty:
        return {"error": 'Valor no encontrado'}
    df_ordenado = df_filtrado.sort_values(by='sentiment_score', ascending=False)
    top_3_reseñas = df_ordenado.head(3)
    resultado = {
        "Puesto 1": top_3_reseñas.iloc[0]['title'],
        "Puesto 2": top_3_reseñas.iloc[1]['title'],
        "Puesto 3": top_3_reseñas.iloc[2]['title']
    }
    return resultado

# Funcion que devuelve top 3 juegos no recomendados por usuarios segun el año y el sentiment score / Funcion que devuelve top 3 juegos no recomendados por usuarios segun el año y el sentiment score

@app.get('/UsersWorstDeveloper/')
def UsersRecommend(year: int) -> dict:
    df_filtrado = df[(df['year'] == year) & (df['recommend'] == False) & (df['sentiment_score'] == 0 )]
    if df_filtrado.empty:
        return {"error": 'Valor no encontrado'}
    df_ordenado = df_filtrado.sort_values(by='sentiment_score', ascending=False)
    top_3_reseñas = df_ordenado.head(3)
    resultado = {
        "Puesto 1": top_3_reseñas.iloc[0]['publisher'],
        "Puesto 2": top_3_reseñas.iloc[1]['publisher'],
        "Puesto 3": top_3_reseñas.iloc[2]['publisher']
    }
    return resultado

# Funcion que devuelve el sentiment score segun el año / Function that returns the sentiment score according to the year

@app.get('/sentiment_analysis/')
def sentiment_analysis(publisher : str) -> dict:
    filtered_df = df[df['publisher'] == publisher]
    sentiment_counts = filtered_df['sentiment_score'].value_counts()
    result = {
        "Positive": int(sentiment_counts.get(2, 0)),
        "Neutral": int(sentiment_counts.get(1, 0)),
        "Negative": int(sentiment_counts.get(0, 0))
    }
    return result

#  Este código prepara una muestra de 4000 filas del DataFrame original, utiliza TF-IDF para convertir las revisiones de juegos en una representación numérica y calcula la similitud coseno entre estas revisiones.
# La matriz resultante (cosine_similarity) contiene las puntuaciones de similitud coseno entre todas las combinaciones posibles de revisiones en la muestra.
muestra = df.head(4000)
tfidf = TfidfVectorizer(stop_words='english')
muestra=muestra.fillna("")
tdfid_matrix = tfidf.fit_transform(muestra['review'])
cosine_similarity = linear_kernel( tdfid_matrix, tdfid_matrix)
@app.get('/recomendacion_id/{id_usuario}')
def recomendacion(id_producto: int):
    if id_producto not in muestra['steam_id'].values:
        return {'mensaje': 'No existe el id del usuario.'}
  
    generos = muestra.columns[2:17] 
