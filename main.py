from flask import Flask
from waitress import serve
import requests
import json



app = Flask(__name__)
api_key = '4cd4f08b-4233-47cd-90b1-cffdb5ac5d8a'


@app.route('/')
def hello():
    payload = {}
    r = requests.get('https://api.thecatapi.com/v1/images/search', params=payload)
    print('URL: ', r.url)
    cat_data = json.loads(r.text)
    url = cat_data[0]['url']
    html = f'<img src="{url}" alt="A random cat image">'
    return html

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8080)
