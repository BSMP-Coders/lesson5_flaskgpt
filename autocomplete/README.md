  
# Flask-AzureOpenAI Autocomplete Web App  
   
This project demonstrates how to create an interactive web application using Flask and Azure OpenAI. The application provides autocomplete suggestions based on user input, similar to the example shown in the provided images.  

![Autocomplete Web App Demo](https://github.com/BSMP-Coders/advanced_coding_wiki/blob/main/media/flaskautocomplete.png?raw=true)

## Introduction  
   
This project is a sample lesson on integrating Flask with Azure OpenAI to create an interactive web application. The application features:  
- A live clock display  
- Tabs for different modes (non-functional in this example)  
- An input field for user text  
- Autocomplete suggestions based on user input  
- Response time display  

   
## Running the Application  
   
1. **Start the Flask Application**:  `python -m flask run`
   
2. **Access the Application**: Open your browser and go to `http://127.0.0.1:5000`  
   
## Project Structure  
   
```  
flask-autocomplete/  
│  
├── app.py  
└── templates/  
    └── index.html  
```  
   
- `app.py`: The main Flask application file.  
- `templates/`: Directory containing HTML templates.  
- `index.html`: The main HTML file for the web interface.  
   
## Code Explanation  
   
### Backend (`app.py`)  
   
```python  
from flask import Flask, request, jsonify, render_template  
from openai import AzureOpenAI  
   
app = Flask(__name__)  
   
# Replace with your Azure OpenAI API key and endpoint  
api_key = 'your_api_key'  
endpoint = 'https://your-endpoint.openai.azure.com/'  
   
openai_client = AzureOpenAI(api_key=api_key, azure_endpoint=endpoint, api_version="2024-05-01-preview")  
MODEL_NAME = "gpt-35-turbo"  
   
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
```
### Initial Setup if starring from scratch

   
1. **Clone the Repository**:  git clone
    
1. **Install Dependencies** or run in Codespaces
   
1. **Configure Environment Variables**:  
   - Create a `.env` file and add your Azure OpenAI API key and endpoint:  
     
    ```env  
    AZURE_OPENAI_API_KEY=your_api_key  
    AZURE_OPENAI_ENDPOINT=https://your-endpoint.openai.azure.com/  
    ```  