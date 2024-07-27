from flask import Flask
app = Flask(__name__)


@app.route('/')
def main_page():
    #this is the main page of file
    return 'hello M.R.Zarei'