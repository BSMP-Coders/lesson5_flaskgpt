from flask import Flask, request  # import main Flask class and request object
import random

app = Flask(__name__)  # create the Flask app


@app.route('/status', methods=['GET'])
def a_live():
    return "Alive!"

@app.route('/predict', methods=['GET'])
def predict():
    demo=random.randint(2000, 5000)    
    return str(demo)

