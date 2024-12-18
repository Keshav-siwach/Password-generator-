import random

print("PASSWORD GENERATOR\n")
n1 = int(input("How many special symbols do you want? "))
password = []
s = ["&", "#", "$", "@", "¥"]

for i in range(n1):
    password.append(random.choice(s))

n2 = int(input("How many letters do you want? "))

l = ["a", "b", "c", "d", "e"]

for i in range(n2):
    password.append(random.choice(l))

n3 = int(input("How many numbers do you want? "))

for i in range(n3):
    password.append(str(random.randint(0, 9)))

random.shuffle(password)

password_str = ''.join(password)

print("Generated Password:", password_str)
