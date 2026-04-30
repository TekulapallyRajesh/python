a=int(input("enter any number: "))
sum=0
while(a!=0):
    rem=a%10
    sum=sum+rem
    a=a//10
print("sum is {}".format(sum))