# Mood-Based Music Recommender

This is a beginner-level AI project that recommends songs based on the user's emotions. It uses basic Python along with a lightweight natural language processing library called NRCLex to detect specific emotions such as joy, sadness, anger, or tiredness from user input. Based on the detected emotion, the program filters and displays a list of songs that match the user's mood.

This project was created to explore how simple AI and DSA (data structures and algorithms) concepts can be combined to build interactive applications.

## Features

- Detects specific human emotions like anger, joy, sadness, tiredness, etc.
- Recommends songs based on the detected emotion using a small dataset stored in CSV format
- Easy to understand and run
- Requires only one lightweight Python package (NRCLex)
- Includes both English and Indian songs

## Project Structure

MoodMusicRecommender/
    data/
        songs_dataset.csv     # Contains songs and associated emotions
mood_detector.py              # Detects emotion from user input
recommender.py                # Recommends songs based on emotion
main.py                       # Main entry point to run the app
requirements.txt              # Python packages required
README.md                     # Project description and guide


## How to Install and Run

1 way:

Try the live demo of my Mood-Based Music Recommender app built with Streamlit:  

Click here to run the app
(https://mood-music-recommender-jvcrurhd4vz5apppprwitanp.streamlit.app/)


2 way:
1. Open the project in VS Code or any code editor.
2. Open the terminal and install the required package using this command:


-->     pip install -r requirements.txt


3. Run the project using:


python main.py


4. Enter a sentence describing your mood 
(for example: "I am very happy, I got promotion. Hurrah!!!").

The application will detect your emotion and suggest songs based on that emotion.

## Example

Input:


I feel lonely and sad today.


Output:


Detected Emotion: Sadness

Recommended Songs:
1. Let Her Go by Passenger
2. Channa Mereya by Arijit Singh
3. Agar Tum Saath Ho by Alka Yagnik
4. Khairiyat by Arijit Singh


## Supported Emotions

This project supports the following emotions, depending on the input:
- Joy
- Sadness
- Anger
- Tired
- Trust
- Fear
- Disgust
- Anticipation
- Surprise

## Data Format

The songs are stored in a CSV file located at `data/songs_dataset.csv`.

Example:


Ilahi,Arijit Singh,joy
Sadda Haq,Mohit Chauhan,anger
Let Her Go,Passenger,sadness


## Requirements

Only one package is required for this project:

nrclex


This is already included in `requirements.txt`.

## About the Project

This project was made to explore how text-based emotion detection can be combined with basic file handling and logic in Python to create a music recommendation system. It is lightweight and clean to run easily on any machine, 
Techniques: file I/O, conditional logic, basic NLP.
