from flask import Flask, render_template, request
import datetime
import smtplib

my_email = 'oulkarshubhu@gmail.com'
password = 'loadvnqrbxfcykos'

now_year = datetime.datetime.now().year

app = Flask(__name__)


@app.route("/")
def  home():
    return render_template('index.html', year=now_year)


@app.route("/<about>")
def  about(about):
    return render_template(f'{about}', year=now_year)


@app.route("/post")
def  post():
    return render_template("post.html", year=now_year)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        email= f'Subject: Mail from my web \n\nName: {data["name"]} \nemail: {data["email"]} \ncontact no.: {data["phone"]} \nMessage: {data["message"]}'
        with smtplib.SMTP('smtp.gmail.com') as connections:
            connections.starttls()
            connections.login(user=my_email, password=password)
            connections.sendmail(from_addr=my_email,
                                 to_addrs=my_email,
                                 msg= email)
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


if __name__ == "__main__":
    app.run(debug=True)
