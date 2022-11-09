import streamlit as st
import requests
import spotipy

'''
# JARS test
'''

st.markdown('''
Search for your favorite song and get a list of recommended songs!
''')

# 1. Add some controllers in order to ask the user to select the parameters of the recommendation
# - song name
# - amount of recommended songs

song = st.text_input('Insert song and artist names:', placeholder = 'song name + artist name')
amount = st.number_input('Insert amount of songs:', min_value=5, max_value=50, value=20)
#playlist = st.checkbox('Create new playlist:', value=False)

url = 'https://jars-test-3l6llep5va-wl.a.run.app/recommendation'
#url = 'https://127.0.0.1:8000/recommendation'
# 2. Let's build a dictionary containing the parameters for our API...

params = {
    'song': song,
    'amount': amount
    #'playlist': pickup_lat
}

# 3. Let's call our API using the `requests` package...
if st.button('Get Recommendation'):
    response = requests.get(url, params=params)

    # 4. Let's retrieve the prediction from the **JSON** returned by the API...

    prediction = response.json()

    ## Finally, we can display the prediction to the user

    st.write(prediction)

if st.button('Make Playlist'):

    username = None
    client_id = 'b8c39473bf4a4b7ea9deeadad8ecd9ae'
    client_secret = 'c3a78c3d7ba54691b07e9198cfe8783e'

    # With authentication
    sp = spotipy.Spotify(
        auth_manager= spotipy.SpotifyOAuth(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri="https://federicoeramirez-jars-website-app-test-branch-x6qu44.streamlit.app/",
            scope="playlist-modify-private",
            #scope="user-library-read"
            )
        )

    user_id = sp.me()['id']

    playlist = sp.user_playlist_create(user_id,
                                       'test',
                                       public=False,
                                       collaborative=False,
                                       description='Testing')

    playlist_id = playlist['id']

    top_tracks_list = ['3Bdqlr7jQLNhITAgcBGQBG',
                       '7sLpSWxQazJzDVG6YGzlVs']

    sp.user_playlist_add_tracks(user_id,
                            playlist_id,
                            top_tracks_list,
                            position=None)
