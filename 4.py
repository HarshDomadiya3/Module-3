# Write a Python function to get the largest number, smallest num and sum of all from a list. 

number=[1,2,3,4,5]
def function(number):
    return max(number),min(number),sum(number)
large,small,sum=function(number)
print("large number:-",large)
print("small number:-",small)
print("sum of list:-",sum)
