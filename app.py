# author: Soumil Datta

from flask import Flask, render_template as render, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
    return render("index.html")

@app.route('/statecases', methods=['POST'])
def statecases():
    value = request.form
    return value

if __name__ == "__main__":
    app.run(debug=True)