# Write a Python program to create a dictionary from a string. 


a="harshdomadiya"
b={}
for i in a:
    if i in b:
        b[i]+=1
    else:
        b[i]=1
print(b)