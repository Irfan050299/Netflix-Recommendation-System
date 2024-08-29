import pickle
import re
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve(strict=True).parent


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = cosine_similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]

    recommended_movies = []

    for i in movies_list:
        movie_id = i[0]
        

    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
cosine_similarity = pickle.load(open('cosine_similarity.pkl','rb'))
