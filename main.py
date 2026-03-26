import spotipy
import os
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials
import streamlit as st 
import pandas as pd


load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id = client_id,
    client_secret = client_secret
))

playlist_id = "37i9dQZEVXbLRQDuF5jeBp"

results = sp.playlist_tracks(playlist_id)

tracks=[]
for item in results['items']:
    track = item['track']
    tracks.append({
        "track_name": track['name'],
        "artist": track['artists'][0]['name']
        "popularity": track['popularity']
    })


df = pd.DataFrame(tracks)
st.write("Top 50 Tracks in the USA")
st.dataframe(df)

#Create bar chart
st.bar_chart(df.set_index("track_name")["popularity"])
