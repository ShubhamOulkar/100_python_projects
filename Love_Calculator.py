print("""----------------------------------------------------------
             Love Calculator 2022
----------------------------------------------------------""")
name = input("Type Your name: \n").lower()
partner = input("Type your partner name: \n").lower()
true = []
love = []
string = ["t","r","u","e","l","o","v","e"]
for i in string[0:4]:
    true.append(name.count(i))
    true.append(partner.count(i))
for q in string[4:8]:
    love.append(name.count(q))
    love.append(partner.count(q))
love_score = int(str(sum(true))+str(sum(love)))


