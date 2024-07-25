# meme_app.py  
from flask import Blueprint  
import requests  
  
meme_bp = Blueprint('meme_bp', __name__)  
  
def get_meme():  
    url = "https://meme-api.com/gimme"  
    response = requests.get(url)  
    return response.json()['url']  
  
@meme_bp.route('/meme2')  
def meme():  
    print("running meme generator from demos/meme_app.py")
    meme_url = get_meme()  
    return f'<img src="{meme_url}" alt="Meme" style="max-width: 100%; height: auto;">'  
