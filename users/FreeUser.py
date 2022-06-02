from users.User import User
class FreeUser(User):
    def __init__(self, name, email, drivers_license, age, number_of_posts=0):
        # parent_instance = super()
        # parent_instance.__init__(name, email, drivers_license, age)
        super().__init__(name, email, drivers_license, age)
        self.number_of_posts=number_of_posts

    def CreatePost(self, input_string):
        if self.number_of_posts <2:
            super().CreatePost(input_string)
            self.number_of_posts+=1
        else:
            print("I'm sorry you've exceed your max as a free user, please upgrade to be able to post more!")


# dalton=FreeUser("Dalton", "egglestondalton@yahoo.com", "WDLA12324AD", 22,0)
# print(dalton.number_of_posts)

# dalton.CreatePost("The weather is beautiful")
# print(User.user_post)
# print(dalton.number_of_posts)
# dalton.CreatePost("The weather is UGLY")
# dalton.CreatePost("I LOVE SOCKS")
