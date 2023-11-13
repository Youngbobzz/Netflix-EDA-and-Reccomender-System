import streamlit as st
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import requests

movies = pd.read_pickle('netflix.pkl')
cosine_sim = pd.read_pickle('cosine_sim.pkl')
movie_list = movies['title'].values 

st.header('Netflix Recommender System')
st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Netflix_2015_logo.svg/1200px-Netflix_2015_logo.svg.png')

colum1, colum2, colum3, colum4, colum5 = st.columns(5)

with colum1:
    st.image('https://resizing.flixster.com/TuSc9h1wQO8ZSuCtmOt-p7_dj2s=/ems.cHJkLWVtcy1hc3NldHMvdHZzZWFzb24vMDYzNWFmNGYtZmVkYS00MDRhLTk2NTctNmExOTc0MGY1ZTVkLmpwZw==')

with colum2:
    st.image('https://m.media-amazon.com/images/M/MV5BZmRjODgyMzEtMzIxYS00OWY2LTk4YjUtMGMzZjMzMTZiN2Q0XkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_.jpg')

with colum3:
    st.image('https://m.media-amazon.com/images/M/MV5BYWE3MDVkN2EtNjQ5MS00ZDQ4LTliNzYtMjc2YWMzMDEwMTA3XkEyXkFqcGdeQXVyMTEzMTI1Mjk3._V1_FMjpg_UX1000_.jpg')

with colum4:
    st.image('https://m.media-amazon.com/images/I/71tsl8uVFeL._AC_UF894,1000_QL80_.jpg')

with colum5:
    st.image('https://m.media-amazon.com/images/M/MV5BZWQyZTkwMTMtYTJiZS00MGNlLThhN2EtYzEzOGQzYjFiZGQxXkEyXkFqcGdeQXVyMTEzMjQ4NzEw._V1_.jpg')



select_value = st.selectbox('Select Movie from dropdown', movie_list)

def recommend(df):
    index=movies[movies['title']==df].index[0]
    distance = sorted(list(enumerate(cosine_sim[index])), reverse=True, key=lambda vector:vector[1])
    recommend_movie=[]
    for i in distance[1:6]:
        movies_id=movies.iloc[i[0]].show_id
        recommend_movie.append(movies.iloc[i[0]].title)
    return recommend_movie


if st.button('Show Recommend'):
    movie_name = recommend(select_value)
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.text(movie_name[0])
    with col2:
        st.text(movie_name[1])
    with col3:
        st.text(movie_name[2])
    with col4:
        st.text(movie_name[3])
    with col5:
        st.text(movie_name[4])