# Lesson 5 - Flask + Azure Open AI

## Goals 🎯
- Understand basic Python and Flask concepts.
- Learn how to create web applications using Flask.
- Explore how to integrate Azure OpenAI into your applications.
- Practice running and testing Flask apps in separate terminals.

## Lesson Overview 📖
We'll start with creating a simple Flask app with multiple routes, then build an interactive app that echoes messages. Finally, we'll integrate Azure OpenAI to add advanced features like chat and autocomplete.

# Lesson Instructions for coders

## Lesson quick start

all of the lesson code today is in basics folder. so in the termanal to start the frist app do the following

```sh
cd basics
python app1.py
```

### Part 1: Basic Flask App with Multiple Routes

**Objective:** Introduce basic Flask routes and a simple HTML template with buttons, images, and a video.

**app1.py:**
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, this is a basic Flask app!"

@app.route('/page1')
def page1():
    message = "Hello, this is a basic Flask app!"
    return f"""{message}<div></div>
    <button><a href="/test-ai">Test AI</a></button> <br>
    <a href="/test-ai">Test AI</a> <br>
    <a href="/ask">Ask</a> <br>
    <a href="/chat">Chat</a>"""

HTML_TEMPLATE = """
<h1>Hello, this is a basic Flask app!</h1>
<button><a href="/test-ai">Test AI</a></button> <br>
<img src="https://placehold.co/200x200.png" alt="Placeholder Image"> <br>
<iframe width="560" height="315" src="https://www.youtube.com/embed/CtdyoH-kvog?si=6lEVlWfIBuNhZhxy" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
"""

@app.route('/page2')
def page2():
    return HTML_TEMPLATE

if __name__ == '__main__':
    app.run(debug=True)
```


**Explanation:**
- **Multiple Routes:** We have multiple routes (`/`, `/page1`, `/page2`) that return different content.
- **HTML Template:** The `/page2` route uses an HTML template with a button, an image, and a video.


### Part 2: Interactive Echo App with POST Requests

**Objective:** Create an interactive Flask app that handles POST requests and returns responses.

**app2.py:**
```python
from flask import Flask, request, jsonify, render_template_string
import requests

app = Flask(__name__)

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Interactive Echo App</title>
</head>
<body>
    <h1>Interactive Echo App</h1>
    <form method="POST" action="/send_echo">
        <input type="text" name="message" placeholder="Enter your message">
        <input type="submit" value="Send to Echo Server">
    </form>
    {% if result %}
    <p>{{ result }}</p>
    {% endif %}
</body>
</html>
'''

def send_echo_request(message):
    url = "http://localhost:5000/echo"
    data = {"message": message}
    response = requests.post(url, json=data)
    if response.status_code == 200:
        return f"Server responded: {response.json()['response']}"
    else:
        return f"Error: Status code {response.status_code}"

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/send_echo', methods=['POST'])
def send_echo():
    message = request.form.get('message', '')
    result = send_echo_request(message)
    return render_template_string(HTML_TEMPLATE, result=result)

@app.route('/echo', methods=['POST'])
def echo():
    data = request.json
    message = data.get('message', 'No message sent')
    return jsonify({'response': message})

if __name__ == '__main__':
    app.run(debug=True)
```

**Explanation:**
- **Interactive Form:** The HTML form sends a message to the Flask server.
- **Echo Endpoint:** The `/echo` endpoint returns the message received.
- **POST Requests:** Handles POST requests and returns JSON responses.

**Running the Apps:**
- Open two terminals.
- In the first terminal, run `python app2.py` to start the Flask server.
- In the second terminal, use the script below to send test messages.

**test_app2.py:**
```python
from app2 import send_echo_request

# Test the echo endpoint
print(send_echo_request("Hello, Flask!"))
print(send_echo_request("Say Phillip in French!"))
```

### Part 3: Azure OpenAI Chat Model Integration

**Objective:** Integrate Azure OpenAI for advanced chat features.

**app3.py:**
```python
from flask import Flask, request, jsonify
from openai import AzureOpenAI
import os
import dotenv

dotenv.load_dotenv()

AOAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AOAI_KEY = os.getenv("AZURE_OPENAI_API_KEY")
MODEL_NAME = "gpt-35-turbo"

app = Flask(__name__)

openai_client = AzureOpenAI(api_key=AOAI_KEY, azure_endpoint=AOAI_ENDPOINT, api_version="2024-05-01-preview")

@app.route('/')
def index():
    return "Hello, this is a simple Flask server."

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data.get('user_input', '')
    response = openai_client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ],
        max_tokens=50,
        temperature=0.5
    )
    suggestions = response.choices[0].message.content
    return jsonify({'suggestions': suggestions})

if __name__ == '__main__':
    app.run(debug=True)
```

**Explanation:**
- **OpenAI Integration:** Connect to Azure OpenAI to handle chat requests.

**Running the Apps:**
- Open two terminals.
- In the first terminal, run `python app3.py` to start the Flask server.
- In the second terminal, use the script below to send test messages.

**test_app3.py:**
```python
import requests

def send_chat_request(user_input):
    url = "http://localhost:5000/chat"
    data = {"user_input": user_input}
    response = requests.post(url, json=data)
    if response.status_code == 200:
        print(f"Server responded: {response.json()}")
    else:
        print(f"Error: Status code {response.status_code}")

# Test the chat function
send_chat_request("Say hi in French")
```

**Explanation:**
- **Testing:** Test the chat functionality by sending a request to the Flask server.

### Part 4: Flask App with HTML and OpenAI Integration

**Objective:** Combine Flask, HTML, and OpenAI for a complete interactive web app.

**app4.py:**
```python
from flask import Flask, request, jsonify, render_template
from openai import AzureOpenAI
import os
import dotenv

dotenv.load_dotenv()

AOAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AOAI_KEY = os.getenv("AZURE_OPENAI_API_KEY")
MODEL_NAME = "gpt-35-turbo"

app = Flask(__name__)

openai_client = AzureOpenAI(api_key=AOAI_KEY, azure_endpoint=AOAI_ENDPOINT, api_version="2024-05-01-preview")

@app.route('/')
def home():
    return render_template('chat_app4.html')

@app.route('/autocomplete', methods=['POST'])
def autocomplete():
    data = request.get_json()
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
```

**templates/chat_app4.html:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Autocomplete App</title>
    <script>
        async function getAutocomplete() {
            const prompt = document.getElementById('inputText').value;
            const response = await fetch('/autocomplete', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ prompt })
            });
            const data = await response.json();
            document.getElementById('suggestions').innerText = data.suggestions;
        }
    </script>
</head>
<body>
    <h1>Autocomplete App</h1>
    <div>
        <input type="text" id="inputText" oninput="getAutocomplete()">
        <div id="suggestions"></div

>
    </div>
</body>
</html>
```

**Explanation:**
- **Render Template:** Serves an HTML file for interaction.
- **JavaScript:** Fetches autocomplete suggestions from the Flask server.


# Activities 
### 1. **Explore Flask Routes and Templates**

**Activity:**  
- **Objective:** Understand Flask routes and rendering HTML.
- **Task:** modify `app1.py` by adding new routes that display different types of content, such as text, images, or embedded videos. Encourage them to use different HTML elements and styles.
- **Challenge:** Ask coders to create a simple personal webpage using Flask that includes sections like "About Me," "Projects," and "Contact."

### 2. **Create a Mini Chatbot**

**Activity:**  
- **Objective:** Implement basic chatbot functionality using Flask and Azure OpenAI.
- **Task:** Using `app3.py` as a starting point, have coders create a simple chatbot that can answer questions based on a specific theme, such as history, science, or technology.
- **Challenge:** integrate additional APIs (like a weather API or a news API) to provide dynamic responses based on real-time data.

### 3. (optional) **Interactive Form with Data Validation**

**Activity:**  
- **Objective:** Learn about form handling and data validation in Flask.
- **Task:** In `app2.py`, extend the interactive form to include additional input fields (e.g., name, age, favorite color) and implement basic validation (e.g., required fields, correct data types).
- **Challenge:** Ask coders to store and display submitted data on a new route, creating a simple guestbook application.

### 4. (optional) **Autocomplete Feature Enhancement**

**Activity:**  
- **Objective:** Improve the autocomplete feature using JavaScript and Flask.
- **Task:** In `app4.py` and `chat_app4.html`, modify the autocomplete functionality to provide more interactive suggestions (e.g., highlighting, filtering based on previous inputs).
- **Challenge:** Have coders create a themed autocomplete feature (e.g., suggesting movie titles, book names, or historical figures) and display related images or links based on the user's selection.
