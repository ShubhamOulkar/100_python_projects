
def add(a , b):
    return a + b

def subtract(a, b):
    return a - b

def multi(a, b):
    return a * b

def devide(a, b):
    return a / b

operations = {
"+" : add,
"-" : subtract,
"*":multi,
"/":devide
}

a = int(input("Enter number: "))
sign = input("Choose operations +, -, * or / : ")
b = int(input("Enter number: "))

value = operations[sign]
function_call = value(a,b)
print(f"{a} {sign} {b} = {function_call}")