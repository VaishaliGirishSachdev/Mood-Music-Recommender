import streamlit as st
from mood_detector import detect_mood
from recommendor import get_songs_by_mood

# Set page settings
st.set_page_config(page_title="Mood Music Recommender", layout="centered")

# Page title
st.title("🎵 Mood-Based Music Recommender")

# Ask user for input
user_input = st.text_input("Tell me how you're feeling:")

# When input is entered
if user_input:
    # Detect mood
    emotion = detect_mood(user_input)
    st.success(f"Detected Emotion: **{emotion.capitalize()}**")

    # Recommend songs
    songs = get_songs_by_mood(emotion)

    if songs:
        st.subheader("🎧 Recommended Songs:")
        for idx, song in enumerate(songs, 1):
            st.markdown(f"{idx}. {song}")
    else:
        st.warning("😔 Sorry, no songs found for your emotion.")
