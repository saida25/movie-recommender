import pandas as pd
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

csv_path = os.path.join(os.path.dirname(__file__), "movies.csv")
df = pd.read_csv(csv_path)
df["features"] = df["overview"] + " " + df["genres"].astype(str)

tfidf = TfidfVectorizer(stop_words="english")
df["features"] = df["features"].fillna("")
tfidf_matrix = tfidf.fit_transform(df["features"])
cosine_sim = cosine_similarity(tfidf_matrix)

def recommend_movies(title, n=5):
    idx = df[df["title"] == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    movie_indices = [i[0] for i in sim_scores[1:n+1]]
    return df["title"].iloc[movie_indices]

print(recommend_movies("The Dark Knight"))