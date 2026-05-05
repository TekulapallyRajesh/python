def fact(a):
    if a==1:
        return 1
    else:
        return a*fact(a-1)
    
a=int(input("enter any number: "))
res=fact(a)
print("factorial is ",res)