def fibo(i):
    if i==0:
        return 0
    elif i==1:
        return 1
    else: 
        return fibo(i-2)+fibo(i-1)


a=int(input("ente any number: "))
for i in range(a):
    x=fibo(i)
    print(x,end=" ")