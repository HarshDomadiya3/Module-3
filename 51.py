# Write a Python function that checks whether a passed string is
# palindrome or not 

def palindrome(a):
    a=a.replace(" ", "").lower()
    return a ==a[::-1]
print(palindrome("level"))