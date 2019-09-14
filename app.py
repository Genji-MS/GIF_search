from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    # √: Extract query term from url and set a default (if first run)
    query = request.args.get('query')
    if query is None:
        query = 'cat'
    # √: Make 'params' dict with query term and API key
    params = {"tag":query, "key":"IF96GMLBDV8W", "limit":10}
    # √: Make an API call to Tenor using the 'requests' library
    # √: Get the first 10 results from the search results 
    r = requests.get('https://api.tenor.co/v1/search', params= params)
    # √: convert the request into .json and filter to just the results
    gif_json = r.json()
    gif_list = gif_json['results']
    if len(gif_list) == 0:
        return render_template('index.html', query = 'Theres nothing found for the search : '+query, gif_list= gif_list)
    # √: pass the resulting list of gifs back to the page
    else:
        search_term = 'Showing GIFs for : '+query
        return render_template('index.html', query = search_term, gif_list= gif_list)

if __name__ == '__main__':
    app.run(debug=True)