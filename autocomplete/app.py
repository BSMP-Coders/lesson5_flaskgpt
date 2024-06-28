from flask import Flask, request, jsonify, render_template  
from openai import AzureOpenAI 
import os

app = Flask(__name__,template_folder='templates2')  # templates2 👈 adv for enchanced UI/UX

# Replace with your Azure OpenAI API key and endpoint  
# Put the keys and variables here (never put your real keys in the code)
AOAI_ENDPOINT = os.environ["AZURE_OPENAI_ENDPOINT"]
AOAI_KEY = os.environ["AZURE_OPENAI_API_KEY"]
MODEL_NAME = "gpt-35-turbo"

#openai_client = AzureOpenAI(endpoint, AzureKeyCredential(api_key))  
openai_client = AzureOpenAI(api_key=AOAI_KEY,azure_endpoint=AOAI_ENDPOINT,api_version="2024-05-01-preview",)
MODEL_NAME= "gpt-35-turbo"

@app.route('/')  
def index():  
    return render_template('index.html')  
  
@app.route('/autocomplete', methods=['POST'])  
def autocomplete():  
    data = request.json  
    prompt = data.get('prompt', '')  
  
    response = openai_client.chat.completions.create(  
        model=MODEL_NAME,  
        messages=[  
            {"role": "system", "content": "You are an autocomplete assistant."},  
            {"role": "user", "content": prompt}  
        ],  
        max_tokens=50,  
        temperature=0.5  
    )  
  
    suggestions = response.choices[0].message.content
    return jsonify({'suggestions': suggestions})  
  
if __name__ == '__main__':  
    app.run(debug=True)  