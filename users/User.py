class User:

    user_post = [[],[]]

    def __init__(self, name, email, drivers_license, age):
        self.name = name
        self.email = email
        self.drivers_license = drivers_license
        self.age = age
        print("Intizializing")

    def __str__(self):
        return f"My name is {self.name} and I am {self.age} years old"
    
    def CreatePost(self, input_string):
        input_string = input_string
        User.user_post[0].append(self.name)
        User.user_post[1].append(input_string)
        print(f"My name is {self.name} and I've been thinking that {input_string}")
    
    def DeletePost(self):
        for x in range(0, len(User.user_post[0])):
            if User.user_post[0][x] == self.name:
                User.user_post[0].pop(x)
                User.user_post[1].pop(x)
                break




    
    
# dalton = User("Dalton", "egglestondalton@yahoo.com", "WDLA12324AD", 22)
# michael = User("Michael", "feaW@gmail.com", "SF223AWDAD3", 40)
# christopher = User("Christopher", 'giadawd@gmail.com', "WDA2323ADFA", 35)
# dalton.CreatePost("The weather is beautiful")
# michael.CreatePost("Yes I would say so myself!")
# print(User.user_post)
# dalton.DeletePost()
# print(User.user_post)