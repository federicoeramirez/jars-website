import streamlit as st
import requests
import spotipy

'''
# JARS 1.0
'''

st.markdown('''
Search for your favorite song and get a list of recommended songs!
''')

# 1. Add some controllers in order to ask the user to select the parameters of the recommendation
# - song name
# - amount of recommended songs
song = st.text_input('Insert song and artist names:', placeholder = 'song name + artist name')
amount = st.number_input('Insert amount of songs:', min_value=5, max_value=50, value=20)

url = 'https://jars-latest-3l6llep5va-wl.a.run.app/recommendation'

# 2. Let's build a dictionary containing the parameters for our API..
params = {
    'song': song,
    'amount': amount
}

# 3. Let's call our API using the `requests` package...
if st.button('Get recommendation list'):
    response = requests.get(url, params=params)

    # 4. Let's retrieve the recommendation from the JSON returned by the API...
    response_list = response.json()

    list_of_songs = []

    for i in range(amount-1):
        list_of_songs.append(response_list[0][f'{i}'])


    st.write(list_of_songs)

if st.button('Make playlist'):
    username = None
    client_id = 'b8c39473bf4a4b7ea9deeadad8ecd9ae'
    client_secret = 'c3a78c3d7ba54691b07e9198cfe8783e'

    # With authentication
    sp = spotipy.Spotify(
        auth_manager= spotipy.SpotifyOAuth(
            client_id=client_id,
            client_secret=client_secret,
            #redirect_uri="https://federicoeramirez-jars-website-app-test-branch-x6qu44.streamlit.app/",
            redirect_uri='http://127.0.0.1:9090',
            scope="playlist-modify-private"
            )
        )

    user_id = sp.me()['id']

    response = requests.get(url, params=params)

    # 4. Let's retrieve the recommendation from the JSON returned by the API...
    response_list = response.json()

    list_of_id = []

    for i in range(amount-1):
        list_of_id.append(response_list[1][f'{i}'])

    playlist = sp.user_playlist_create(user_id,
                                    'JARS playlist',
                                    public=False,
                                    collaborative=False,
                                    description='Playlist made with JARS v1.0')

    playlist_id = playlist['id']

    sp.user_playlist_add_tracks(user_id,
                                playlist_id,
                                list_of_id,
                                position=None)

    st.text('Playlist saved!')
