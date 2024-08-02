import random
import string
characters=string.ascii_lowercase+string.ascii_lowercase+string.digits+string.punctuation+string.ascii_letters 
pass_len=8
password=""
for i in range(pass_len):
    password=password+random.choice(characters)
print("Your random password is ready",password)
