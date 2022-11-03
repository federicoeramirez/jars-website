import streamlit as st
import requests

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
amount = st.number_input('Insert amount of songs:', min_value=1, max_value=50, value=15)
#playlist = st.checkbox('Create new playlist:', value=False)

url = 'https://jars-test-3l6llep5va-wl.a.run.app/recommendation'

# 2. Let's build a dictionary containing the parameters for our API...

params = {
    'song': song,
    'amount': amount
    #'playlist': pickup_lat
}

# 3. Let's call our API using the `requests` package...

response = requests.get(url, params=params)

# 4. Let's retrieve the prediction from the **JSON** returned by the API...

prediction = response.json()

## Finally, we can display the prediction to the user

st.write(prediction)
