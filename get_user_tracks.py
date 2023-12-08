import spotipy
from spotipy.oauth2 import SpotifyOAuth
import csv
import pandas as pd

CLIENT_ID = "f536719718b146a28cbdc122c5992e92"
CLIENT_SECRET = "e3dee5d378cb4ff8bdc68f9b93e0cc17"
REDIRECT_URI = "http://localhost/"

TOP_TRACKS_ENDPOINT = "https://api.spotify.com/v1/me/top/tracks"
AUDIO_FEATURES_ENDPOINT = "https://api.spotify.com/v1/audio-features/{track_id}"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, scope="user-top-read"))

def get_top_tracks():
    return sp.current_user_top_tracks(limit=100, time_range='medium_term')  # You can adjust the time_range as needed

def get_audio_features(track_id):
    return sp.audio_features([track_id])[0]

def write_to_csv(tracks, filename="top_tracks.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["name", "artist", "album", "popularity", "duration_ms", "danceability", "energy", "key", "loudness", "mode", "speechiness", "acousticness", "instrumentalness", "liveness", "valence", "tempo"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for track in tracks["items"]:
            audio_features = get_audio_features(track["id"])
            track_info = {
                "name": track["name"],
                "artist": track["artists"][0]["name"],
                "album": track["album"]["name"],
                "popularity": track["popularity"],
                "duration_ms": track["duration_ms"],
                "danceability": audio_features["danceability"],
                "energy": audio_features["energy"],
                "key": audio_features["key"],
                "loudness": audio_features["loudness"],
                "mode": audio_features["mode"],
                "speechiness": audio_features["speechiness"],
                "acousticness": audio_features["acousticness"],
                "instrumentalness": audio_features["instrumentalness"],
                "liveness": audio_features["liveness"],
                "valence": audio_features["valence"],
                "tempo": audio_features["tempo"],
            }
            writer.writerow(track_info)

if __name__ == "__main__":
    top_tracks = get_top_tracks()
    write_to_csv(top_tracks)
    print("CSV file created successfully.")


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, scope="user-library-read"))

def get_audio_features(track_id):
    return sp.audio_features([track_id])[0]

def write_to_csv(tracks, filename="user_library_tracks.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["name", "artist", "album", "popularity", "duration_ms", "danceability", "energy", "key", "loudness", "mode", "speechiness", "acousticness", "instrumentalness", "liveness", "valence", "tempo"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for track in tracks:
            audio_features = get_audio_features(track["track"]["id"])
            track_info = {
                "name": track["track"]["name"],
                "artist": track["track"]["artists"][0]["name"],
                "album": track["track"]["album"]["name"],
                "popularity": track["track"]["popularity"],
                "duration_ms": track["track"]["duration_ms"],
                "danceability": audio_features["danceability"],
                "energy": audio_features["energy"],
                "key": audio_features["key"],
                "loudness": audio_features["loudness"],
                "mode": audio_features["mode"],
                "speechiness": audio_features["speechiness"],
                "acousticness": audio_features["acousticness"],
                "instrumentalness": audio_features["instrumentalness"],
                "liveness": audio_features["liveness"],
                "valence": audio_features["valence"],
                "tempo": audio_features["tempo"],
            }
            writer.writerow(track_info)

if __name__ == "__main__":
    user_tracks = sp.current_user_saved_tracks(limit=50)
    tracks = user_tracks["items"]


    while user_tracks["next"]:
        user_tracks = sp.next(user_tracks)
        tracks.extend(user_tracks["items"])


    tracks = tracks[:1000]

    # Write the selected tracks to a CSV file
    write_to_csv(tracks)
    print("CSV file created successfully.")

df1 = pd.read_csv("user_library_tracks.csv")
df2 = pd.read_csv("top_tracks.csv")



merged_df = pd.concat([df1, df2], ignore_index=True)
merged_df.to_csv("merged_file.csv", index=False)

print("CSV files merged successfully.")