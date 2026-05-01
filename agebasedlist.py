Names=["raj","janu","sachin","harsh","sid"]
age=[47,76,18,17,20,36]
res=list(zip(age,Names))
res1=sorted(res,reverse=True)
p=1
for i in res1:
    print(f"{p}.{i[1]} age is {i[0]}")
    p=p+1