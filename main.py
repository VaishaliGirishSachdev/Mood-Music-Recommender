from mood_detector import detect_mood
from recommendor import get_songs_by_mood

print("Mood-Based Music Recommender")
print("Tell me how you're feeling:")

user_input = input("> ")

emotion = detect_mood(user_input)
print(f"\nDtected Emotion: {emotion.capitalize()}")

songs = get_songs_by_mood(emotion)

if songs:
    print("\n Recommended Songs: ")
    for idx, song in enumerate(songs, 1):
        print(f"{idx}.{songs}")

else:
    print("Sorry, no songs for your emotion")

    