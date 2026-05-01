a=int(input("enter any number: "))
count=0
for i in range(2,a):
    if a%i==0:
        count=count+1
if count==0:
    print(f"{a} is prime")
else:
    print(f"{a} is composite")