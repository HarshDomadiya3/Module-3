# Write a Python script to sort (ascending and descending) a dictionary byvalue. 

a={'apple':3,'banana':5,'cherry':2,'date':4}
b=dict(sorted(a.items(),key=lambda item:item[1]))
c=dict(sorted(a.items(),key=lambda item:item[1],reverse=True))
print("Ascending :-",b)
print("Descending :-",c)