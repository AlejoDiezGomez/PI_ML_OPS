# PROYECTO INDIVIDUAL 1 ML OPS
## Introducción : 
Este proyecto consiste en crear una API para Steam, construyendo un modelo de recomendacion basado en Machine Learning . Otorgando una interfaz intuitiva para el usuario donde podra consultar datos sobre generos , fechas , sentiment score ,etc. De manera puntual.
## Tecnologías utilizadas :
- FastAPI
- Matplotlib
- NLTK
- Numpy
- Pandas
- Python
- Render
- Scikit-Learn
- Seaborn
- Uvicorn
- Wordcloud
## Resolución :
### 1. [ETL :](ETL.ipynb)
Realice el proceso de ETL (extracción, transformación y carga ) con los archivos obtenidos de distintas fuentes para su posterior análisis y utilización dentro del modelo de ML.
### 2. [EDA :](EDA.ipynb)
Realice el proceso EDA  (Exploratory Data Analysis) en el DataSet obtenido en el etl con el objetivo de identificar relaciones , insights , tendencias y/o patrones , tal que , sirvan para la creacion y ejecucion del modelo de ML
### 3. Modelo de Machine Learning :
Este modelo de  Machine Learning entrega recomendaciones de juegos precisas y personalizadas para cada usuario  con la utilizacion de algoritmos y tecnicas como la similitud del coseno y scikit-lear .
#### Sistema de recomendación item-item:
   - def recomendacion_juego( id de producto ): Ingresando el id de producto ('id), deberíamos recibir una lista con 5 juegos recomendados similares al ingresado.
Ejemplo de uso : 70
#### Sistema de recomendacion user-item: 
- def recomendacion_usuario( id de usuario ): Ingresando el id de un usuario ('user_id'), deberíamos recibir una lista con 5 juegos recomendados para dicho usuario. 
Ejemplo de uso: 76561198030567998
### Deployment de la API
Creamos una API utilizando el módulo FastAPI de Python, creando 5 funciones para que puedan ser consultadas:
- def PlayTimeGenre( genero : str ): Debe devolver año con mas horas jugadas para dicho género. Ejemplo de input: casual , sports 
- def UserForGenre( genero : str ): Debe devolver el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año. Ejemplo de input: action , adventure 
- def UsersRecommend( año : int ): Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado. (reviews.recommend = True y comentarios positivos/neutrales) Ejemplo de input: 2012 , 2015 
- def UsersNotRecommend( año : int ): Devuelve el top 3 de juegos MENOS recomendados por usuarios para el año dado. (reviews.recommend = False y comentarios negativos) Ejemplo de input: 2009 , 2012
- def sentiment_analysis( año : int ): Según el año de lanzamiento, se devuelve una lista con la cantidad de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento. Ejemplo de input: 2014

Luego realizamos el deployement de esta API utilizando Render.
## Elaces : 
- [API]()
- [Video explicativo]()
## Contacto : 
- [Portafolio Web]()
- [Linkedin]()
- [alejodiezgomez@gmail.com]()
- [alejo10gomezz@gmail.com]()

