from flask import Flask, render_template
import datetime

app = Flask(__name__)


@app.route("/")
def  home():
    now_year = datetime.datetime.now().year
    return render_template('index.html', year=now_year)


if __name__ == "__main__":
    app.run(debug=True)
