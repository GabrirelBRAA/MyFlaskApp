from flask import Flask
from Misc.functions import * 

app = Flask(__name__)
app.secret_key = '#$ab9&^BB00_.'

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
