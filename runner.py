from users.PremiumUser import PremiumUser
from users.FreeUser import FreeUser


dalton=FreeUser("Dalton", "egglestondalton@yahoo.com", "WDLA12324AD", 22,0)
michael = PremiumUser("Michael", "feaW@gmail.com", "SF223AWDAD3", 40)


print(dalton.number_of_posts)
# print(michael.email)
# print(michael.user_post)
dalton.CreatePost("The weather is beautiful")
michael.CreatePost("I LOVE SOCKS")
print(michael.user_post)