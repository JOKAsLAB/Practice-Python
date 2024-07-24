# zip function

usernames = [ "Dude", "Bro", "Mister"]
passwords = [ "p@ssword", "abc123", "guest"]
login_date = [ "1/1/2021", "1/2/2021", "1/3/2021"]

users = zip(usernames, passwords)
print(type(users))

for i in users:
    print(i)

print()
print("---------")
print()

list_users = list(zip(usernames, passwords))
print(type(list_users)) 

for i in list_users:
    print(i)

print()
print("---------")
print()

users = zip(usernames, passwords, login_date)

for i in users:
    print(i)