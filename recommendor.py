import csv

def get_songs_by_mood(mood):
    songs = []

    with open('data/songs_dataset.csv', mode='r') as file:
        reader = csv.DictReader(file)

        for r in reader:
            if r['mood'].strip().lower() == mood.lower():
                songs.append(f"{r['title']} by {r['artist']}")

    return songs