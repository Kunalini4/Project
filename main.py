import streamlit as st
from openai import OpenAI

# Set your OpenAI API key here (ensure it's set in Replit secrets)
openai_api_key = st.secrets['OPEN_API_KEY']
client = OpenAI(api_key=openai_api_key)

def get_movie_recommendations(genre, movie_name, movie_length):
    prompt = f"Recommend a {genre} movie similar to {movie_name} that is around {movie_length} minutes long. Provide the movie name, introduction, main actors, duration, and genre."

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
    )

    return             response.choices[0].message.content.strip()

# Streamlit user interface
st.title('Movie Recommendation AI')

# User Inputs
genre = st.selectbox('Select your favorite genre:', ['Action', 'Comedy', 'Drama', 'Sci-Fi', 'Horror'])
movie_name = st.text_input('Enter a favorite movie:')
movie_length = st.slider('Select preferred movie length (in minutes):', 60, 240, 120)

if st.button('Get Recommendations'):
    # Call the function to get movie recommendations
    recommendations = get_movie_recommendations(genre, movie_name, movie_length)
    st.write(recommendations)