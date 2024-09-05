# Write a Python program to remove an empty tuple(s) from a list of tuples

a=[(1,2),(),(3,4)]
list=[]
for i in a:
    if i!=() :
        list.append(i)
print(list)


