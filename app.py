# author: Soumil Datta

from flask import Flask, render_template as render, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
    return render("index.html")

@app.route('/states', methods=['GET', 'POST'])
def statecases():
    state = request.form['state']
    return render("testing.html", state=state)

if __name__ == "__main__":
    app.run(debug=True)