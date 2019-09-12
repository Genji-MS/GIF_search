from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    query = request.args.get('query')
    params = {"tag":query, "key":"IF96GMLBDV8W", "limit":10}
    r = requests.get('https://api.tenor.co/v1/search', params= params)
    return render_template('index.html', params= params, query = query)
    # √: Extract query term from url
    # √: Make 'params' dict with query term and API key
    # √: Make an API call to Tenor using the 'requests' library

    # TODO: Get the first 10 results from the search results

if __name__ == '__main__':
    app.run(debug=True)