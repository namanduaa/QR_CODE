import random
import string

n = int(input("enter the length of password :"))
chars = string.ascii_letters + string.digits + string.punctuation

password="".join([random.choice(chars) for i in range(n)])

# password=""
# newlist=[]
# for i in range(n):
#     password=random.choice(chars)
#     newlist+=password

print(password)