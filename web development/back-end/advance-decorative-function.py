# Create the logging_decorator() function 👇
def logging_decorator(function):
    def wrapper(*args, **kwargs):
        answer = function(args[0], args[1], args[2])
        print(f"You called {function.__name__} function.")
        print(f"It returned: {answer}")
    return wrapper


# Use the decorator 👇
@logging_decorator
def add(a,b,c):
    return a+b+c

add(4,5,6)