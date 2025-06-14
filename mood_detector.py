# Importing Package
from nrclex import NRCLex

# Function for user's mood detection.
def detect_mood(user_input):
    emotion = NRCLex(user_input) # Object
    emotions = emotion.top_emotions  # list of (emotion, score)

    if emotions:
        return emotions[0][0]
    else:
        return "neutral"
    