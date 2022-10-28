# number is input() as string in python
# a = input("Type two digit number: ")
# print("sum =", int(a[0])+int(a[1]))
# print(type(a))
print("""----------------------------------------------------------
             Tip Calculator
----------------------------------------------------------""")

print("Welcome to the tip Calculator!")
bill = float(input("What was the total bill? $"))
percent = float(input("What percentage tip would you like to give? "))
people = float(input("How many people to split the bill?"))
bill_tip = bill + (bill*percent*0.01)
# pay = round(bill_tip / people, 2)
pay = "{:.2f}".format(bill_tip / people)
print("-----------------------------------------------------------------------------------------------")
print(f"Each person should pay: ${pay}")
print("-----------------------------------------------------------------------------------------------")
print("Bill payed by each person is ${:.2f}".format(bill / people))
print("Tip payed by each person is ${:.2f}".format((bill*percent*0.01)/people))
