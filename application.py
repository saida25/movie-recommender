import streamlit as st
import pandas as pd
import os
csv_path = os.path.join(os.path.dirname(__file__), "movies.csv")
df = pd.read_csv(csv_path)

from ml_recommender import recommend_movies

st.title("🎬 Movie Recommender")
title = st.selectbox("Pick a movie", df["title"])
if st.button("Recommend"):
    recommendations = recommend_movies(title)
    st.write(recommendations)