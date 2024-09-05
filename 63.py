# Write a Python program to returns sum of all divisors of a number 

number=int(input("enter a number: "))
total=0
for i in range(1,number+1):
    if number %i== 0:
        total+=i
print("sum of all divisors :-",total)