#Assignment A: Empty class + instances

print("-------------------------------- Assignment A: Empty class + instances --------------------------------")

class User:
    pass

user1 = User()
user2 = User()

print(user1)
print(user2)

#Assignment B: Instance attributes

print("-------------------------------- Assignment B: Instance attributes --------------------------------")

user1.username = "sohamqa"
user1.role = "QA Engineer"
user1.is_active = True

user2.username = "admin"
user2.role = "Admin"
user2.is_active = False

print(f"{user1.username} | {user1.role} | active: {user1.is_active}")
print(f"{user2.username} | {user2.role} | active: {user2.is_active}")

#Assignment C: Methods

print("-------------------------------- Assignment C: Methods --------------------------------")

class User:
    def describe(self):
        print(f"{self.username} --> {self.role}")

    def deactivate(self):
        self.is_active = False

user1 = User()
user1.username = "sohamqa"
user1.role = "QA Engineer"
user1.is_active = True

user2 = User()
user2.username = "admin"
user2.role = "Admin"
user2.is_active = True

user1.describe()
user2.describe()

user2.deactivate()
print(f"{user2.username} active: {user2.is_active}")

#Assignment D: List of users

print("-------------------------------- Assignment D: List of users --------------------------------")

user3 = User()
user3.username = "guest"
user3.role = "Guest"
user3.is_active = True

users = [user1, user2, user3]

for i in range(len(users)):
    if users[i].is_active == True:
        users[i].describe()

print("Day 12 OOP basics done")
