import json
import requests
import os
import pandas as pd
from bs4 import BeautifulSoup
import urllib
import urllib.request


# Enter Artist to artist and song to song_title
artist = "bing-crosby"
song_title = "white hristmas"


# Get the id of the album for further search of the list of songs
def get_album_id(term, media='music', entity='song', limit=10):

    url = "https://itunes.apple.com/search?"
    payload = {'term': term, 'media': media, 'entity': entity, 'limit': limit}
    response = requests.get(url, params=payload)
    status = response.status_code
    # Check the status, if everything is correct, we process the response
    if status == 200:
        # Decode the result
        search_song_results = response.json().get("results", [])
        # Write and return the result of the key call collectionId
        album_id = search_song_results[0]['collectionId']
        return album_id
    else:
        print('Not Found.')


# Having learned id of the collection, you can find the rest of the songs from the collection
def get_list_songs(id, entity='song', limit=10):

    url = "https://itunes.apple.com/lookup?"
    payload = {'id': id, 'entity': entity, 'limit': limit}

    # Make a request with parameters
    response = requests.get(url, params=payload)

    # Receive the answer in json format
    data = response.json()
    data = data['results']

    # Wrote the result of the request to the json file
    with open('data.json', 'w') as f:
        json.dump(data, f)


def generate_csv():
    # Reading data from the .json file.
    json_data = pd.read_json('data.json')

    # Column order
    columns = [
        'artistId', 'collectionId',
        'trackId', 'artistName',
        'collectionName', 'trackName',
        'collectionCensoredName',
        'trackCensoredName', 'artistViewUrl',
        'collectionViewUrl', 'trackViewUrl',
        'previewUrl', 'collectionPrice',
        'trackPrice', 'releaseDate',
        'discCount', 'discNumber',
        'trackCount', 'trackNumber',
        'trackTimeMillis', 'country',
        'currency', 'primaryGenreName'
    ]

    # Organize the data
    json_data = pd.DataFrame(json_data)
    # Delete the first line
    json_data = json_data.iloc[1:]

    # Change the order of columns according to the listing in the list of 'columns'
    json_data = json_data[columns]
    # Writing data to a .csv file
    json_data.to_csv('columns.csv', index=None)
    # Delete json file
    os.remove('data.json')

    print("Done! Check your result in columns.csv")


def generate_text_file(url_ending):

    # Query with arguments to search
    url = 'https://www.e-chords.com/chords/' + url_ending

    # Adding headers to gain access
    url = urllib.request.Request(url, headers={'User-Agent': "Magic Browser"})

    # Reading the page received as a result of the request
    html_page = urllib.request.urlopen(url).read()

    # Parsing pages using a beautiful soup
    soup = BeautifulSoup(html_page, features="html.parser")

    # Search for the 'pre' tag
    html_page = soup.find('pre')

    # Checking the condition if html_page is not none, get the text and write it to the file
    if html_page is not None:
        html_page = html_page.get_text()
        text_file = open("text_song.txt", "w", encoding="utf-8")
        text_file.write(html_page)
        text_file.close()
    # If html_page is none create empty file
    else:
        open('text_song.txt', 'w').close()


# To search, you need to combine the variables into one
term = artist + ' ' + song_title
url_ending = artist.replace(' ', '-') + '/' + song_title.replace(' ', '-')

# Call the search function and pass the new variable
album_id = get_album_id(term)

# We pass the resulting id to the collection search function
list_songs = get_list_songs(album_id)

# Call function of creating a csv file
generate_csv()
# Call function search and create a file with text and chords
generate_text_file(url_ending)



























