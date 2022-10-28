print("""----------------------------------------------------------
             BMI calculator 2022
----------------------------------------------------------""")
height = input("Input your height in meters: ")
weight = input("Input your weight in kilogram: ")

BMI = round(float(weight)/(float(height))**2, 1)
print("---------------------------------------------------------")
if BMI <= 18.5:
    print(f"Your BMI is {BMI} and you are Underweight.")
elif BMI <= 25:
    print(f"Your BMI is {BMI} and you have normal weight.")
elif BMI <= 30:
    print(f"Your BMI is {BMI} and you are overweight.")
elif BMI <= 35:
    print(f"Your BMI is {BMI} and you are obese.")
else:
    print(f"Your BMI is {BMI} and you are critically obese.")

print("\n---------- oulkarshubhu@gmail.com ----------")
