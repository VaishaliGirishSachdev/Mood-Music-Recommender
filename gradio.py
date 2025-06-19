# gradio_app.py

import gradio as gr
from mood_detector import detect_mood
from recommendor import get_songs_by_mood

def recommend_songs(user_input):
    if not user_input.strip():
        return "Please enter how you're feeling."

    mood = detect_mood(user_input)
    songs = get_songs_by_mood(mood)

    if songs:
        return f"**Detected Mood:** {mood.capitalize()}\n\n" + "\n".join(f"🎵 {song}" for song in songs)
    else:
        return f"**Detected Mood:** {mood.capitalize()}\n\n😕 Sorry, no songs found for this mood."

demo = gr.Interface(
    fn=recommend_songs,
    inputs=gr.Textbox(lines=2, placeholder="How are you feeling today?"),
    outputs="markdown",
    title="🎧 Mood-Based Music Recommender",
    description="Type your mood or a sentence describing how you're feeling, and get music recommendations based on detected emotion.",
    theme="soft"
)

if __name__ == "__main__":
    demo.launch()
