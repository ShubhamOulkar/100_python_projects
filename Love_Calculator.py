print("""----------------------------------------------------------
             Love Calculator 2022
             
            88                                     
            88                                     
            88                                     
            88  ,adPPYba,  8b       d8  ,adPPYba,  
            88 a8"         "8a `8b     d8' a8P_____88  
            88 8b           d8  `8b   d8'  8PP"""""""  
            88 "8a,      , a8"   `8b,d8'   "8b,      ,aa  
            88  `"YbbdP"'          "8"      `"Ybbd8"'  
                                       
----------------------------------------------------------""")
name = input("Type Your name: \n").lower()
partner = input("Type your partner name: \n").lower()
true = []
love = []
string = ["t", "r", "u", "e", "l", "o", "v", "e"]
for i in string[0:4]:
    true.append(name.count(i))
    true.append(partner.count(i))
for q in string[4:8]:
    love.append(name.count(q))
    love.append(partner.count(q))
love_score = int(str(sum(true))+str(sum(love)))

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 50 >= love_score >= 40:
    print(f"Your score is {love_score}, you are alright together.")
else :
    print(f"Your score is {love_score}.")

print("\n---------- oulkarshubhu@gmail.com ----------")