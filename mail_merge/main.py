#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

names = open("../mail_merge/Input/Names/invited_names.txt", mode= 'r')
a = names.readlines()
names = []
for i in range(len(a)):
    c = []
    for j in range(len(a[i]) ):
        t = a[i][j]
        if t == '\n':
            t = ""
        c += t
    c = "".join(c)
    names.append(c)

print(names)

letter = open("../mail_merge/Input/Letters/starting_letter.txt", mode = 'r')
b = letter.readlines()
msg = "\n".join(b)


for name in names:
    names_msg = []
    names_msg = msg.replace("[name]", name)
    with open(f"../mail_merge/Output/ReadyToSend/invitation_{name}", mode='w') as file:
        file.write(names_msg)
