class User():
    name = ""
    surname = ""
    b_date = 0
    city = ""
    hobby = ""

user1 = User()
user1.name = "Andrew"
user1.surname = "Kadochnikov"
user1.b_date = 1990
user1.city = "Saint-Petersburg"
user1.hobby = "music"

user2 = User()
user2.name = "Ivan"
user2.surname = "Ivanov"
user2.b_date = 2001
user2.city = "Monaco"
user2.hobby = "Swimming"
print(user1, 2022 - user1.b_date)
print(user2, 2022 - user2.b_date)