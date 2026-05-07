maths=["rajesh","ashok","rahul","ram"]
social=["ram","vaish","harsh","rahul"]
comp=["sid","vishal","ram","ashok"]

m=set(maths)
s=set(social)
c=set(comp)
a=m|s|c
print("three subjects: ",list(m&s&c))
x=(m&s)|(m&c)|(s&c)
print("two subjects: ",list(x-(m&s&c)))
print("one subject: ",list[a])