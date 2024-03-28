import pickle
import streamlit as st
import pandas as pd
from PIL import Image

# Load data
movies_dict = pickle.load(open("model\\movies.pkl", 'rb'))
similarity_tfidf = pickle.load(open("model\\similarity_bert.pkl", 'rb'))

# Function to recommend movies
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity_tfidf[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    for i in movies_list:
        movie_id = i[0]
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

movies = pd.DataFrame(movies_dict)

# Streamlit UI
st.set_page_config(page_title="Movie Recommender", page_icon=":movie_camera:", layout="wide")

# Title and description
col1, col2 = st.columns([1, 3])
with col1:
    image = Image.open("data\\movie_icon.jpg")
    st.image(image, use_column_width=True)

with col2:
    st.title("Movie Recommender System")
    st.write("Get personalized movie recommendations based on your preferences.")

# Movie selection
selected_movie_name = st.selectbox("Select a Movie", movies['title'].values)

if st.button("Recommend"):
    recommendations = recommend(selected_movie_name)
    st.subheader(f"Here are some recommendations based on '{selected_movie_name}':")
    for i, movie in enumerate(recommendations, start=1):
        st.success(f"{i}. {movie}")

# Footer
st.markdown("""
<style>
footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #f8f9fa;
    color: #6c757d;
    text-align: center;
    padding: 10px;
}
</style>
<footer>
    <p>&copy; 2024 Movie Recommender System</p>
</footer>
""", unsafe_allow_html=True)