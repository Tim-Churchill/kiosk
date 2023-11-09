from flask import Flask, render_template, request
from waitress import serve
#from weather import function

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
 
def index():
    return "Hello World"

@app.route('/weather')
def get_weather():
    return render_template("weather.html", title = "nice", status = "flipping")
    
    
if __name__ == "__main__":
    serve(app, host="0.0.0.0", port = 8000)