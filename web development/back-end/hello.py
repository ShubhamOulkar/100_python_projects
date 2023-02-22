from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World! \n This is BTS</p>" \
            "<img src='https://media0.giphy.com/media/S5n64VczoyKSgFlYHZ/giphy.gif?cid=ecf05e47olbhj8boahslemin6bfqj8lfkr5sa2hstwsguykg&rid=giphy.gif&ct=g' width=800 height=400>"


@app.route("/username/<name>")
def greet(name):
    return f"<h1 class='name' style='text-align:center'>Hello, {name}!</h1>"



if __name__ == "__main__":
    app.run(debug=True)


## Functions can be returned from other functions
# def outer_function():
#     print("I'm outer")
#
#     def nested_function():
#         print("I'm inner")
#
#     return nested_function
#
# inner_function = outer_function()
# inner_function()


## Simple Python Decorator Functions
# import time
#
# def delay_decorator(function):
#     def wrapper_function():
#         time.sleep(2)
#         #Do something before
#         function()
#         function()
#         #Do something after
#     return wrapper_function
#
# @delay_decorator
# def say_hello():
#     print("Hello")
#
# #With the @ syntactic sugar
# @delay_decorator
# def say_bye():
#     print("Bye")
#
# #Without the @ syntactic sugar
# def say_greeting():
#     print("How are you?")
# decorated_function = delay_decorator(say_greeting)
# decorated_function()
#
