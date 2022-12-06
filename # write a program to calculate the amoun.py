# write a program to calculate the amount payable if money has be land on simple interest

p=float(input("enter the principalamount="))
r=int(input("enter the rent="))
t=int(input("enter the time="))
SI=float((p*r*t)/100)
pa = p+SI
print("the simple interest=",SI)
print("the payable amount=",pa)