import streamlit as st
from recommender import recommend_movies

st.title("🎬 Movie Recommender")
title = st.selectbox("Pick a movie", df["title"])
if st.button("Recommend"):
    recommendations = recommend_movies(title)
    st.write(recommendations)