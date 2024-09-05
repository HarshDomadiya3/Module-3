# Write a Python function that takes a list and returns a new list with unique
# elements of the first list. 

value=[1,2,3,3,2,1]
def function(list):
    unique=[]
    for i in value:
        if i not in unique:
            unique.append(i)
    return unique
print(function(list))




# unique=list(set(value))
# print(unique)