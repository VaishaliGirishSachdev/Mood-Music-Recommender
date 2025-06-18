from nrclex import NRCLex

def detect_mood(text):
    emotion = NRCLex(text)
    raw_emotions = emotion.raw_emotion_scores

    if not raw_emotions:
        return "neutral"

    # Get emotion with highest score
    primary = max(raw_emotions, key=raw_emotions.get)

    # Map complex emotion to general mood
    mapping = {
        "joy": "happy",
        "trust": "happy",
        "positive": "happy",
        "anticipation": "energetic",
        "anger": "angry",
        "fear": "sad",
        "sadness": "sad",
        "disgust": "angry",
        "surprise": "energetic"
    }

    return mapping.get(primary, "neutral")
