# Write a Python program to create and display all combinations of letters,
# selecting each letter from a different key in a dictionary.
# 


from itertools import product
a={'1':['a','b'],'2':['c','d']}
b=[letters for letters in a.values()]
c=product(*b)
for i in c:
    print(''.join(i))