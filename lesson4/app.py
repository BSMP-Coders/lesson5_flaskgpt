from flask import Flask
import random
# Flask parentheis  underscore underscope name underscore underscore
# we create a variable called `app` with = to the Flask function with a name python variable (__name__) that 
# __name__ just telling flask to take the name of the current directory and use it as the name of the app
app = Flask(__name__) 

# after creating the app, we can create routes to different pages on the website
# to do that have to do some "decorating" usinng the at symbol `@` and the app object
# @app.route('/') 👈 the @ is a python decorator that basically "adds more functionality to a python function right below it"
# the `route` is a function that tell the app where to go 👈 think defining a new web pages like espn.com/nba espn.com/nfl 

@app.route('/') # Home Page - backslash the home address 127.0.0.1:5000/ to the web path
def home():
   print("> using the home route")
   message = "This is our BSMP Flask HOMEPAGE!"
   #message = "<h1>This is our BSMP Flask HOMEPAGE</h1>" # Add Some HTML #part 1
   return message 
   #return render_template('home.html', message=message) # part 2

# Add a new route to the app @app.route('/hello') will create a new page at 127.0.0.1:5000/hello 
# since there is no content in the function, the page will be blank.
@app.route('/hello') 
def hello():
   print("> using the hello route")
   message = "HELLO!!! "
   return message

@app.route('/number') # Home Page - backslash the home address 127.0.0.1:5000/ to the web path
def number():
    print("> using the number route")
    message = "Here's a random number: {0}"
    #message = "<h1>Here's a random number: {0}</h1>" # Add Some HTML
    num = random.randint(1, 25)   # Select a random integer from 1 - 25.
    return message.format(num)

@app.route('/number2')
def number2():
    print("> using the number2 route")
    page = """
        <h1>Here's a random number: {0}</h1>
        <form>
            <button>New Number</button>
        </form>
    """
    num = random.randint(1, 25)
    return page.format(num)

# route to the name page
@app.route('/name')
def name():
   return "My Name is: Phillip Hale"

@app.route('/name/first')
def firstname():
   return "Phillip"

@app.route('/name/last')
def lastname():
   return "Hale"

@app.route('/name/full')
def fullname():
   first_name = firstname()
   last_name = lastname()
   return f"{first_name} {last_name}"


import requests
## Meme generator
def get_meme():  
    url = "https://meme-api.com/gimme"  
    response = requests.get(url)  
    return response.json()['url']  
  
@app.route('/meme')  
def meme():  
    meme_url = get_meme()  
    return f'<img src="{meme_url}" alt="Meme" style="max-width: 100%; height: auto;">'  

# Register the blueprint  
#from demos.meme_app import meme_bp  # sampe this as the get_meme and meme route but we are importing the meme_bp from the meme_app.py file for demonstration
#app.register_blueprint(meme_bp) # route /meme2


# Example of a simple form and html
from flask import render_template, request
@app.route('/user', methods=['GET', 'POST'])
def user_info():
    user_data = None  # Initialize to None for clarity
    if request.method == 'POST':
        name = request.form['name']
        age = int(request.form['age'])  # Convert age to integer
        city = request.form['city']
        user_data = {'name': name, 'age': age, 'city': city}
    return render_template('simple_form.html', user_data=user_data)  # Pass user data to template




#@app.route('/hi')
#def hi():
#   return "Hi!"

#@app.route('/hi/status')
#def status():
#   return "How are you?"

#@app.route('/hi/status/bye')
#def bye():
#   return "Bye!"

if __name__ == '__main__':
   app.run(debug=True)