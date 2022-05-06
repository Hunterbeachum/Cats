from flask import Flask
from waitress import serve
import random
import requests
import json


app = Flask(__name__)
api_key_cats = '4cd4f08b-4233-47cd-90b1-cffdb5ac5d8a'


# CHANGED THIS
@app.route('/')
def home():
    payload = {}
    r = requests.get('https://api.thecatapi.com/v1/images/search', params=payload)
    print('URL: ', r.url)
    cat_data = json.loads(r.text)
    url = cat_data[0]['url']
    html = f'<a href="/movie"><img src="{url}" alt="A random cat image"></a>'
    return html


@app.route('/movie')
def movie():
    payload = {}
    a_random_int = random.randint(2,1000)
    v = requests.get(f'https://api.themoviedb.org/3/movie/{a_random_int}?api_key=29e35d1a18f27c1185d11c046faff565', params=payload)
    movie_data2 = json.loads(v.text)
    while 'success' in movie_data2:
        a_random_int = random.randint(2,1000)
        v = requests.get(f'https://api.themoviedb.org/3/movie/{a_random_int}?api_key=29e35d1a18f27c1185d11c046faff565')
        movie_data2 = json.loads(v.text)
    movie_title = movie_data2['original_title']
    html = f'Your random movie to watch is {movie_title}'
    return html


if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8080)
