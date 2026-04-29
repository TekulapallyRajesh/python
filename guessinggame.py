import random
p1=input("enter player1 Name: ")
p2=input("enter player2 Name: ")
s1=10
s2=10
d1=random.randint(1,10)
d2=random.randint(1,10)
print("-----------------PLAYER1 TURN----------------")
while(True):
    g1=int(input("Enter your guess: "))
    s1=s1-1
    if g1==d1:
        break
print("-----------------PLAYER2 TURN----------------")
while(True):
    g2=int(input("Enter your guess: "))
    s2=s2-1
    if g2==d2:
        break
print("____________SUMMARY__________")
print("{} : {} ".format(p1,s1))
print("{} : {} ".format(p2,s2))
print("________RESULT__________")
if s1>s2:
    print("{} is Winner".format(p1))
elif s2>s1:
    print("{} is Winner".format(p2))
else:
    print("__TIE__")