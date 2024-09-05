# Write a Python function that takes two lists and returns true if they have
# at least one common member.


list1=[1,2,3,4]
list2=[1,2,5,6]
def function(list1,list2):
    for i in list1:
        if i in list2:
            return True
        return False
print(function(list1,list2))
