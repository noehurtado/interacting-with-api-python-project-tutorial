import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# load the .env file variables
load_dotenv()

# Getting the id and secret from the .env file 
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')

# Connecting to spotify and getting the top tracks 
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))
artist = 'spotify:artist:6XyY86QOPPrYVGvF9ch6wz'
artist_tracks = sp.artist_top_tracks(artist)

# Creating a dataframe 
tracks = pd.DataFrame(artist_tracks['tracks'])
tracks['duration_sec'] = tracks['duration_ms'] / 1000
tracks = tracks.drop(columns=['album', 'artists', 'available_markets', 'disc_number', 
       'explicit', 'external_ids', 'external_urls', 'href', 'id', 'is_local',
       'is_playable', 'preview_url', 'track_number', 'type', 'uri'])

# Sorting our df by popularity descending and printing the top 3 songs 
tracks = tracks.sort_values('popularity', ascending=False)
print(tracks.head(3))

# Plotting a scatter plot
print('As we can see on the scatter plot, song popularity is not highly correlated to duration, since the most popular song is not the longest, neither the less popular is the shortest.')

plt.figure(figsize=(12,12))
plt.title('"Linking Park" Top 10 Songs Popularity')
plt.xlabel('Duration in seconds')
plt.ylabel('Popularity')
sns.scatterplot(data=tracks, x='duration_sec', y='popularity', hue='name', legend='brief')
plt.legend(loc='lower center')
plt.show()




