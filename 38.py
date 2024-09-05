# Write a Python program to check multiple keys exists in a dictionary


a={'name':'harsh','age':30, 'city':'surat'}
b=['name','age','city']
c= True
for i in b:
    if i not in a:
        c= False
        break
if c:
    print("keys are present")
else:
    print("keys are missing")