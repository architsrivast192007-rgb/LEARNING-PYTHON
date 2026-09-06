"""
when all the length of the sides of a  trinagle is known -a,b,c
Semi perimeter(s)=(a+b+c)/2
Area =  square root of (s*(s-a)*(s-b)*(s-c))
"""
a=float(input("Enter first side a:"))
b=float(input("Enter second side a:"))
c=float(input("Enter third side a:"))
s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c))**0.5
print("The area of the triangle is",round(area,2))




