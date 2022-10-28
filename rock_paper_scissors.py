import random
# toss = random.randint(0,1)
# if toss == 1:
#     print("Heads")
# else:
#     print("Tails")
print("""----------------------------------------------------------
             Rock Paper Scissors Game 2022
----------------------------------------------------------""")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
art = [rock, paper, scissors]
you = int(input("\n Input 1 for Rock \n Input 2 for Paper\n Input 3 for Scissors\n"))
computer = random.randint(1,3)
if you == 1 and computer == 3:
    print(f"your choice: {art[you-1]}\n computer choice: {art[computer-1]}")
    print("You win!")
elif you == 3 and computer == 2:
    print(f"your choice: {art[you - 1]}\n computer choice: {art[computer - 1]}")
    print("You win!")
elif you == 2 and computer == 1:
    print(f"your choice: {art[you - 1]}\n computer choice: {art[computer - 1]}")
    print("You win!")
else:
    print(f"your choice: {art[you - 1]}\n computer choice: {art[computer - 1]}")
    print("You Lose!")

print("---------------- shubhuoulkar@gmail.com ------------------")