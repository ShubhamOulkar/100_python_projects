from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/")
def  home():
    return "Know Your Gender and Age"

@app.route("/<name>")
def gender_age(name):
    age = requests.get(f"https://api.agify.io/?name={name}").json()['age']
    gender = requests.get(f"https://api.genderize.io/?name={name}").json()['gender']
    return render_template('index.html', n=name, a= age, g= gender)

if __name__ == "__main__":
    app.run(debug=True)
