a=int(input("Enter any number1: "))
b=int(input("enter any number2: "))
m=2
res=1
while(a!=1 or b!=1):
    if a%m==0 or b%m==0:
        res=res*m
        if a%m==0:
            a=a//m
        if b%m==0:
            b=b//m
    else:
        m=m+1
print(res)

   