row1 = ['-', '-', '-']
row2 = ['-', '-', '-']
row3 = ['-', '-', '-']
map = [row1, row2, row3]
position = input("Where do you want to put the treasure?")
map[int(position[0])-1][int(position[1])-1] = "X"
print(f"{row1}\n{row2}\n{row3}")
