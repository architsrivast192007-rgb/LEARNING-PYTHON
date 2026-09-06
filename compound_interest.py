"""
Amount=P(1+R/100)**T
ci=Amount-P
"""
principal=float(input("Enter ur principal amount:"))
rate=float(input("Enter your rate of interest:"))
time=float(input("Enter your time:"))
#amount1=principal*(1+rate/100)**time
amount2=principal*pow((1+rate/100),time)

print(round(amount2,2))
ci=amount2-principal
print("Compound Interest is:",round(ci,2))





