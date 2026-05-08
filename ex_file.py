a=open("raj.txt",'r')
l=[]
res=a.readlines()
while res:
    l.append(res)
    res=a.readlines()
a.close()
for i in l:
    print(i)