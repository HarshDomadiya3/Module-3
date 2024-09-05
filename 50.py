# Write a Python function to check whether a number is perfect or not


def perfect(number):
    if number <= 0:
        return False  
    a=0
    for i in range(1, number):
        if number %i ==0:
            a+=i 
    return a ==number
print(perfect(6)) 