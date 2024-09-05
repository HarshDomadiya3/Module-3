#  Write a Python program to generate and print a list of first and last 5
# elements where the values are square of numbers between 1 and 30.

a=[]
for x in range(1,31):
    a.append(x**2)
print("First 5 elements :-",a[:5])
print("Last 5 elements :-",a[-5:])

b=[]
for i in range(1,31):
    b.append(i**2)
print("first element :-",b[:5])
print("last element :-",b[-5:])
