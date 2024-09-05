# Write a Python program to read a random line from a file. 

import random
file=open('file')
lines=file.readlines()
file.close()
print(random.choice(lines))