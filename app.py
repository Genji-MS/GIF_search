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
    # √: Get the first 10 results from the search results 
    params = {"tag":query, "key":"IF96GMLBDV8W", "limit":10}
    # √: Make an API call to Tenor using the 'requests' library
    #sort the request based on the search_button pressed.
    if request.args.get('search_buttons') == 'trending':
        query = 'Showing trending GIFs'#unique output message
        #We do NOT want the query param, need to remodel this to use the params above
        r = requests.get('https://api.tenor.com/v1/trending?key=IF96GMLBDV8W&limit=10')
    elif request.args.get('search_buttons') == 'random':
        query = 'Showing random GIFs'#unique output message
        #requires a search parameter. Standard search is sorted by TOP. hard to ask the user, so we define this search term ourselves
        r = requests.get('https://api.tenor.com/v1/random?tag=random&key=IF96GMLBDV8W&limit=10')
    else:
        r = requests.get('https://api.tenor.co/v1/search', params= params)
    # √: convert the request into .json and filter to just the results
    gif_json = r.json()
    gif_list = gif_json['results']
    # Set custom page messages based on error, or if user clicked an optional button
    if len(gif_list) == 0:
        search_term = 'Theres nothing found for the search : '+query
    elif query == 'Showing trending GIFs' or query == 'Showing random GIFs':
        search_term = query
    else:
        search_term = 'Showing top GIFs for : '+query
    # √: pass the resulting list of gifs back to the page
    return render_template('index.html', query = search_term, gif_list= gif_list)

if __name__ == '__main__':
    app.run(debug=True)