
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

keep_doing = True

while keep_doing :
    a = int(input("Enter number: "))
    sign = input("Choose operations +, -, * or / : ")
    b = int(input("Enter number: "))

    value = operations[sign]
    function_call = value(a, b)
    print(f"{a} {sign} {b} = {function_call}")

    repe = input("Do you want to run calculator again? y/n ").lower()
    if repe == "y":
        keep_doing = True
    else:
        keep_doing = False

