# Write a Python program to find the highest 3 values in a dictionary 

a={'a':100,'b':200,'c':300,'d':400,'e':500}
b=sorted(a.values(),reverse=True)[:3]
print(b)