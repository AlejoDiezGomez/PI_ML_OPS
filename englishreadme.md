# INDIVIDUAL PROJECT 1 ML OPS
## Introduction:
This project involves creating an API for Steam, building a recommendation model based on Machine Learning. Providing an intuitive interface for the user where they can query data about genres, dates, sentiment scores, etc. In a timely manner.

## Technologies Used:
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
Performed the ETL (extraction, transformation, and loading) process with files obtained from various sources for subsequent analysis and use within the ML model.

### 2. [EDA:](EDA.ipynb)
Conducted Exploratory Data Analysis (EDA) on the DataSet obtained in the ETL with the aim of identifying relationships, insights, trends, and/or patterns that serve the creation and execution of the ML model.

### 3. Machine Learning Model:
This Machine Learning model provides accurate and personalized game recommendations for each user using algorithms and techniques such as cosine similarity and scikit-learn.

#### Item-Item Recommendation System:
- `def game_recommendation(product_id)`: By entering the product id ('id'), we should receive a list of 5 games recommended similar to the input. Example of usage: `70`

#### User-Item Recommendation System:
- `def user_recommendation(user_id)`: By entering the user id ('user_id'), we should receive a list of 5 games recommended for that user. Example of usage: `76561198030567998`

### API Deployment:
We created an API using the FastAPI module in Python, creating 5 functions that can be queried:
- `def PlayTimeGenre(genre: str)`: Should return the year with the most played hours for that genre. Example input: `casual`, `sports`
- `def UserForGenre(genre: str)`: Should return the user with the most accumulated playtime for the given genre and a list of accumulated playtime per year. Example input: `action`, `adventure`
- `def UsersRecommend(year: int)`: Returns the top 3 games MOST recommended by users for the given year. (reviews.recommend = True and positive/neutral comments) Example input: `2012`, `2015`
- `def UsersNotRecommend(year: int)`: Returns the top 3 games LEAST recommended by users for the given year. (reviews.recommend = False and negative comments) Example input: `2009`, `2012`
- `def sentiment_analysis(year: int)`: Based on the release year, returns a list with the number of user review records categorized with sentiment analysis. Example input: `2014`

Then we deployed this API using Render.

## Links:
- [API]()
- [Explanatory Video]()

## Contact:
- [Web Portfolio]()
- [Linkedin]()
- [alejo10gomezz@gmail.com]()
