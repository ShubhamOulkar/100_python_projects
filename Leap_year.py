print("""----------------------------------------------------------
             Leap year checker
----------------------------------------------------------""")
year = int(input("Which year do you want to check?\n"))
print("----------------------------------------------------------")

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"Year {year} is a Leap year.")
        else:
            print(f"Year {year} is not a Leap year.")
    else:
        print(f"Year {year} is a Leap year.")
else:
    print(f"Year {year} is not a Leap year.")

print("\n---------- oulkarshubhu@gmail.com ----------")