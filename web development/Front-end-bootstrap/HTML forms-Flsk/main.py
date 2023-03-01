from flask import render_template, Flask, request


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=['POST'])
def data_receved():
    username = request.form['name']
    passcode =  request.form['pass-name']
    return render_template('index.html', user=username, passw=passcode)


if __name__ == "__main__":
    app.run(debug=True)