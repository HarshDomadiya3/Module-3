# Write a Python program to calculate surface volume and area of acylinder 

a=3.14
radius=float(input("enter radius :-"))
height=float(input("enter height :-"))
volume=a*radius**2*height
b=2*a*radius*(radius + height)
print(volume)
print(b)

