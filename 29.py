# Write a Python program to unzip a list of tuples into individual lists.

a=[(1,3),(2,4),(3,5)]
list1,list2,list3=zip(a)
list1=list(list1)
list2=list(list2)
list3=list(list3)
print("List 1 :-",list1)
print("List 2 :-",list2)
print("List 3 :-",list3)