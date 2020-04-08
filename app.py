# author: Soumil Datta

from flask import Flask, render_template as render, url_for, request
import data 

def createApp():
    app = Flask(__name__)

    @app.route('/')
    def index():
        total, death, recovered = data.getTotal()
        return render("index.html", total=total, death=death, recovered=recovered)

    @app.route('/states', methods=['GET', 'POST'])
    def statecases():
        state = request.form['state']
        _, total, newcases, death = data.getData(state)
        return render("states.html", state=state, total=total, newcases=newcases, death=death)

    if __name__ == "__main__":
        app.run(debug=False)

    return app

createApp()