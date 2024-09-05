# Write a Python program to combine two dictionary adding values for
# common keys.



a={'a':100,'b':200,'c':300}
b={'a':300,'b':200,'d':400}
c={}
for i,value in a.items():
    c[i]=value
for i, value in b.items():
    if i in c:
        c[i]+= value
    else:
        c[i] =value
print(c)