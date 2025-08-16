# movie-recommender
# 🎬 Movie Recommendation Engine

An NLP-powered movie recommender using **TF-IDF** and **cosine similarity**, deployed with FastAPI and Streamlit. Recommends films based on plot/genre similarity.

[![Deployed on Render](https://img.shields.io/badge/Render-Deployed-green)](https://your-render-link-here)  
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-streamlit-link-here)

## 🚀 Features
- **Content-based filtering** (no user data required)
- **FastAPI backend** for recommendations
- **Streamlit UI** for interactive testing
- **Free deployment** on Render

## 🛠️ Tech Stack
| Component       | Technology |
|----------------|------------|
| NLP Model      | TF-IDF + Cosine Similarity |
| Backend        | FastAPI    |
| Frontend       | Streamlit  |
| Deployment     | Render     |
| Dataset        | [TMDB Movies](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) |

## 📦 Installation
```bash
git clone https://github.com/saida25/movie-recommender.git
cd movie-recommender
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate  # Windows
pip install -r requirements.txt