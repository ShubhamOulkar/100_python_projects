from flask import Flask, render_template
import datetime

now_year = datetime.datetime.now().year

app = Flask(__name__)


@app.route("/")
def  home():
    return render_template('index.html', year=now_year)


@app.route("/blogs")
def get_blogs():
    return render_template('blogs.html', year=now_year)


@app.route("/blogs/post")
def get_post():
    return render_template('post.html', year=now_year)


if __name__ == "__main__":
    app.run(debug=True)
