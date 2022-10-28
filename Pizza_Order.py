print('''
                      88                                 
                       ""                                 

8b,dPPYba,  88  888888888 888888888 ,adPPYYba,  
88P'       "8a  88      a8P"                a8P"    ""          `Y8  
88          d8   88   ,d8P'              ,d8P'      ,adPPPPP88  
88b,      ,a8"  88 ,d8"             ,d8"             88,          ,88  
88`YbbdP"'   88 888888888 888888888 `"8bbdP"Y8  
88                                             
88  
''')
print("""----------------------------------------------------------
             Pizza Order Bill Generator
----------------------------------------------------------""")
print("""
[ Input: S for small, M for medium, L for large
          Y for yes , N for no ]
""")
size = input("What size pizza do you want ? ").lower()
bill = 0
if size == 's':
    bill = 15
    pepper = input("Do you pepperoni? ").lower()
    if pepper == 'y':
        bill += 2
    else:
        print("Input valid letter")
    cheese = input("Do you want extra cheese?").lower()
    if cheese == 'y':
        bill += 1
    else:
        print("Input valid letter")
elif size == 'm':
    bill = 20
    pepper = input("Do you pepperoni? ").lower()
    if pepper == 'y':
        bill += 3
    else:
        print("Input valid letter")
    cheese = input("Do you want extra cheese?").lower()
    if cheese == 'y':
        bill += 1
    else:
        print("Input valid letter")
elif size == 'l':
    bill = 25
    pepper = input("Do you pepperoni? ").lower()
    if pepper == 'y':
        bill += 3
    else:
        print("Input valid letter")
    cheese = input("Do you want extra cheese?").lower()
    if cheese == 'y':
        bill += 1
    else:
        print("Input valid letter")
else:
    print("Input valid letter.")

# pepper = input("Do you pepperoni? ").lower()
# if pepper == 'y':
#     if size == 's':
#         bill += 2
#     else:
#         bill += 3
# else:
#     print("Input valid letter.")
#
# cheese = input("Do you want extra cheese?").lower()
# if cheese == 'y':
#     bill += 1
# else:
#     print("Input valid letter.")
print("------------------------------------------------------------")
print(f"bill : ${bill}")
print("------------------------------------------------------------")
print("\n---------- shubhuoulkar@gmail.com ----------")
