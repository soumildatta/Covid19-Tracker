# author: Soumil Datta

from flask import Flask, render_template as render, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render("index.html")

if __name__ == "__main__":
    app.run(debug=True)