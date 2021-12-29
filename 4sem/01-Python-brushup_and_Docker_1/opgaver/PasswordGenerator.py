# Password Generator
# Generates a password with the length between 8 and 10 
# with lower and upper case, including numbers and symboles
import random
import string

length = random.randint(8,10)
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation
    
all = lower + upper + num + symbols

temp = random.sample(all,length)

password = "".join(temp)

print(password)                                                                                         