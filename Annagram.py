a=input("enter any String : ")
b=input("enter any String : ")
a1="".join(i.lower() for i in a if i.isalnum() )
b1="".join(i.lower() for i in b if i.isalnum())

a2=sorted(a1)
b2=sorted(b1)

if a2==b2:
    print(f"{a} and {b} are annagram")
else:
    print(f"{a} and {b} are not annagram")