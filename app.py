import os
import pickle
import streamlit as st
import requests
import pandas as pd  


def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=427447aef4335c2135b9915e4299803f&language=en-US"
    response = requests.get(url)
    data = response.json()
    poster_path = data.get('poster_path')

    
    if poster_path:
        return "https://image.tmdb.org/t/p/w500/" + poster_path
    else:
        return "https://via.placeholder.com/500x750?text=No+Image+Available"


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []

    for i in distances[1:6]:  
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters


base_path = os.path.dirname(os.path.abspath(__file__))
movie_list_path = os.path.join(base_path, 'model', 'movie_list.pkl')
similarity_path = os.path.join(base_path, 'model', 'similarity.pkl')


with open(movie_list_path, 'rb') as f:
    movies = pickle.load(f)
with open(similarity_path, 'rb') as f:
    similarity = pickle.load(f)


st.title("🎬 Movie Recommender System")
st.write("Select a movie to get top 5 recommendations with posters!")

movie_list = movies['title'].values
selected_movie = st.selectbox("Search or select a movie:", movie_list)

if st.button("Show Recommendation"):
    with st.spinner("Fetching recommendations..."):
        recommended_movie_names, recommended_movie_posters = recommend(selected_movie)

        
        cols = st.columns(5)
        for i in range(5):
            with cols[i]:
                st.text(recommended_movie_names[i])
                st.image(recommended_movie_posters[i])
