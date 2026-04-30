a=int(input("Enter num1: "))
b=int(input("enter num2: "))
while(b!=0):
    rem=a%b
    a=b
    b=rem
print("Gcd is {} ".format(a))