class Rect:
    def __init__ (self,l,b):
        self.l=l
        self.b=b
    def display(self):
        print("area is : ",self.l*self.b)


a=Rect(20,40)
a.display()
b=Rect(40,50)
b.display()