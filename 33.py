#  Write a Python script to concatenate following dictionaries to create anew one. 

a={'a':1,'b':2}
b={'c':3,'d':4}
c={'e':5,'f':6}
d={**a,**b,**c}
print(d)