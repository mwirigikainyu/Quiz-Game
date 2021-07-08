class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password
        self.followers = 0
        self.following = 0
        self.posts = []

    def follow(self, user):
        self.following += 1
        user.followers += 1

    def unfollow(self, user):
        self.following -= 1
        user.followers -= 1


user1 = User('A001', 'michellemwirigi', '*(&^8HSAiwewh')
user2 = User('D232', 'alfredikiugu', 'UOYSAU2327@')

user1.follow(user2)
user2.follow(user1)
user1.unfollow(user2)

print(user1.followers)
print(user2.followers)
