"""
Simple interest is= (P*R*T)/100
P=Principal amount
R=Rate of Interest
T=Time duration of interest

"""
principal=float(input("Enter the principal amount:"))
rate=float(input("Enter the rate of interest:"))
time=float(input("Enter the time duration of the interest:"))
si=(principal*time*rate)/100
print("simple interest is ",si)

