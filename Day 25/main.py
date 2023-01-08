# List Comprehension

# challenge 1: Square number

# number = [1, 8 , 5, 9 , 44, 20, 60, 40]
# square_number = [num * num for num in number]
# print(square_number)
#
# square_number = [num * num for num in range(1203, 135068)]
# print(square_number)

# challenge 2: find even number from a list
# number = [1,1,2,3,4,5,6,7,8,9,1,313,21,34,55]
# result = [num for  num in number if num % 2 == 0 ]
# print(result)

# challenge 3: How many letters from each word in a sentence?
sentence ="What is the airspeed velocity of an unladen swallow?"
word_split = sentence.split(" ")
result = {word : len(word) for word in word_split }
print(result)





















