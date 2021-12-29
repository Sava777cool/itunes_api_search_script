It's script for api request to itunes.
Script make request format artist+song title and receive response json data.

Task: upon request, artist + song title, find out a list of all songs in the album and save the list to a csv file. Also find the lyrics with chords and write to the .txt file

1. For quick start see SETUP.md
2. To form a request at the beginning of the search_script.py file in the artist variables - enter the artist, in the song_title - enter the name of the song.
3. After this, in the terminal you need to run the script with the command: python search_script.py
4. If the search was successful, you will see the message: "Done! Check your result in columns.csv"
5. If message "Not found", something wrong. Maybe you make mistake when entered artist or song_title.

Files columns.csv and text_song.txt file will be automatically created in the root directory of the project.
