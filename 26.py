# Write a Python program to replace last value of tuples in a list

a=[(1, 2, 3)]
b=[]
for i in a:
    i=list(i)  
    i[-1]=100  
    b.append(tuple(i))
print("NeW List :-",b)
