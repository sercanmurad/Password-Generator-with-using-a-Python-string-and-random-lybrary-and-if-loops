import random
import string

low_case=string.ascii_lowercase
up_case=string.ascii_uppercase
symbols=string.punctuation
digits=string.digits

all_characters=[low_case,up_case,symbols,digits]

password=" "

for j in range(4):
    for i in range(2):
        password+=all_characters[j][random.randint(0,9)]

#Change the string into list
password=list(password)
random.shuffle(password)
print(password)

new_password=""
for i in password:
    new_password+= i

print(new_password)