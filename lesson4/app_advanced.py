# python app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"



import random
@app.route('/predict', methods=['GET'])  
def predict():  
    demo = random.randint(2000, 5000)  
    return str(demo)  

from flask import request, jsonify
import requests, json
@app.route('/echo', methods=['GET', 'POST'])  
def echo():  
    if request.method == 'POST':  
        data = request.json  # Get the JSON data sent in the POST request  
        return jsonify(data)  # Return the data as a JSON response  
    else:  
        return "Send a POST request with JSON data to this endpoint." 


## Meme generator
def get_meme():  
    url = "https://meme-api.com/gimme"  
    response = requests.get(url)  
    return response.json()['url']  
  
@app.route('/meme')  
def meme():  
    meme_url = get_meme()  
    return f'<img src="{meme_url}" alt="Meme" style="max-width: 100%; height: auto;">'  


#from demos.meme_app import meme_bp  
# Register the blueprint  
#app.register_blueprint(meme_bp) 



if __name__ == '__main__':
    app.run(debug=True)