import json
import requests
import os
import pandas as pd

# Enter Artist to artist and song to song_title
artist = "Nirvana"
song_title = "smells like teen spirit"


# Make a request for itunes with parameters for a more accurate search
def get_album_id(term, media='music', entity='song', limit=10):
    url = "https://itunes.apple.com/search?"
    payload = {'term': term, 'media': media, 'entity': entity, 'limit': limit}
    response = requests.get(url, params=payload)
    # Decode the result
    search_song_results = response.json().get("results", [])
    # Write and return the result of the key call collectionId
    album_id = search_song_results[0]['collectionId']
    return album_id

# Having learned id of the collection, you can find the rest of the songs from the collection
def get_list_songs(id, entity='song', limit=10):
    url = "https://itunes.apple.com/lookup?"
    payload = {'id': id, 'entity': entity, 'limit': limit}
    response = requests.get(url, params=payload)
    data = response.json()
    # Wrote the result of the request to the json file
    with open('data.json', 'w') as f:
        json.dump(data, f)


# To search, you need to combine the variables into one
term = artist + ' ' + song_title
# Call the search function and pass the new variable
album_id = get_album_id(term)
# We pass the resulting id to the collection search function
list_songs = get_list_songs(album_id)

# Reading data from the .json file.
json_data = pd.read_json('data.json')
# Writing data to a .csv file
json_data.to_csv('columns.csv', index=None)
# Delete json file
os.remove("data.json")

print("Done! Check your result in columns.csv ")























