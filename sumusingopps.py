class ace:
    def set_dim(self,a,b):
        self.tot=a+b
    def display(self):
        print("sum is ",self.tot)
        print("good morning")
    
    
a=ace()
b=ace()
a.set_dim(50,60)
a.display()
b.set_dim(40,59)
b.display()
