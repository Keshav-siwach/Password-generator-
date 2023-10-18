# Password-generator-

print("PASSWORD GENERATOR\n")
n1=int(input("how many special symbol you want="))

password=[]
s=["&","#","$","@","¥"]

import  random
b=random.choice(s)

for i in range(0,n1-1):
    password+=random.choice(s)
    

l=["a","b","c","d","e"]
n2=int(input("how many letter you want="))
import random
d=random.choice(l)
for i in range(0,n2-1):
    password+=random.choice(l)
    

'''set=set()
set=set.union(b,d)
print(str(set))'''
n3=int(input("how many number you want = "))
n=str(random.randint(1,9))
for i in range(0,n3-1):
       password+=str(random.randint(1,9))
       

random.shuffle(password)

password_str=""
for i in password:
    password_str+=i

print(password_str)    
