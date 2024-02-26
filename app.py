import streamlit as st
import pickle
import pandas as pd
import requests

st.title('Movie Recommender System')

def fetch_poster(movie_id):
    response=requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=76beb8b96516a73e89371784fbd76aec&language=en-US')
    data=response.json()
    # print(data)
    return 'https://image.tmdb.org/t/p/w500/'+data['poster_path']

def recommend_movies(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    recommend_lst=[]
    recommend_posters_lst=[]
    for i in movies_list:
        id=movies.iloc[i[0]].movie_id
        recommend_lst.append(movies.iloc[i[0]].title)
        recommend_posters_lst.append(fetch_poster(id))
    return recommend_lst,recommend_posters_lst

movies_dict=pickle.load(open('movies.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))
movies=pd.DataFrame(movies_dict)


selected_movie_name = st.selectbox(
    'Search for TOP-5 Movie Recommendations',
    movies['title'].values)

if st.button('Recommend'):
    recommendations,posters=recommend_movies(selected_movie_name)

    c1,c2,c3,c4,c5 = st.columns(5)
    with c1:
        st.text(recommendations[0])
        st.image(posters[0])
    with c2:
        st.text(recommendations[1])
        st.image(posters[1])
    with c3:
        st.text(recommendations[2])
        st.image(posters[2])
    with c4:
        st.text(recommendations[3])
        st.image(posters[3])
    with c5:
        st.text(recommendations[4])
        st.image(posters[4])
    