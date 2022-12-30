class User :
    '''constructor:-  initialise attributes here'''
    def  __init__(self, id, username):
        self.id = id
        self.username = username
        self.followers = 0
        self.following = 0

    # Method : It is function
    def follow(self, user):
        user.followers += 1
        self.following += 1

# Positional arguments
user_1 = User(id = "001",username="Shubham") # positional arguments for class

# user_1.id = "001"
# user_1.username = "Shubham"
print(user_1.id)
print(user_1.username)

user_2 = User("002","Queenie")
print(user_2.id)
print(user_2.username)

print(user_1.followers) # default value for an attribute
print(user_2.followers) # default value for an attribute

user_1.follow(user_2)
user_2.follow(user_1)
print(user_1.following)
print(user_1.followers)
print(user_2.followers)
print(user_2.following)







