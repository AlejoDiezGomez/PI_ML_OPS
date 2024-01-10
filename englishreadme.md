# INDIVIDUAL PROJECT 1 ML OPS
### [English Readme](englishreadme.md)
## Introduction:
This project involves creating an API for Steam, building a recommendation model based on Machine Learning. Providing an intuitive interface for the user to query data about genres, dates, sentiment scores, etc. Specifically.

## Technologies used:
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

## Resolution:
### 1. [ETL:](ETL.ipynb)
I performed the ETL (extraction, transformation, and loading) process with files obtained from various sources for subsequent analysis and utilization within the ML model.

### 2. [EDA:](EDA.ipynb)
I carried out the Exploratory Data Analysis (EDA) process on the dataset obtained in the ETL to identify relationships, insights, trends, and/or patterns that serve for the creation and execution of the ML model.

### 3. Machine Learning Model:
This Machine Learning model provides accurate and personalized game recommendations for each user using algorithms and techniques such as cosine similarity and scikit-learn.

#### User-item recommendation system:
- def user_recommendation(user_id): By entering a user's ID ('user_id'), we should receive a list of 5 recommended games for that user.
Example of use: 76561198030567998, 76561198066011588

#### Item-item recommendation system:
- def game_recommendation(product_id): By entering a product ID ('id'), we should receive a list of 5 games recommended similar to the one entered.
Example of use: 70, 1520

### 4. API Deployment:
We created an API using the FastAPI module in Python, creating 5 functions that can be queried:

- def PlayTimeGenre(genre: str): It should return the year with the most played hours for the given genre. Example input: casual, sports

- def UserForGenre(genre: str): It should return the user with the most accumulated hours played for the given genre and a list of the accumulation of hours played per year. Example input: action, adventure

- def UsersRecommend(year: int): It returns the top 3 games MOST recommended by users for the given year. (reviews.recommend = True and positive/neutral comments) Example input: 2012, 2015

- def UsersWorstDeveloper(year: int): It returns the top 3 developers with the LEAST recommended games by users for the given year: 2009, 2012

- def sentiment_analysis(developer_company: str): According to the developer company, it returns a dictionary with the name of the developer as the key and a list with the total quantity of user review records categorized with sentiment analysis as the value. Example input: valve

Then we deployed this API using Render.

## Links:
- [API](https://alejo-diez-gomez-pi-ml-ops.onrender.com/)
- [Explainer Video]()

## Contact:
- [Web Portfolio](https://alejodiezgomez.github.io/)
- [Linkedin](https://www.linkedin.com/in/alejo-gabriel-diez-gomez-402b93254/)
- [alejo10gomezz@gmail.com]()
