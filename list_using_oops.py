
class CIRCLES:
    def __init__ (self):
        x=int(input("enter radius: "))
        self.radius=x
    def display(self):
        print("area of circle is: ",3.14*self.radius**2)


a=int(input("enter no of circles: "))
circles=[]
for i in range(a):
    c=CIRCLES()
    circles.append(c)
    c.display()
    print("___________________________________")
