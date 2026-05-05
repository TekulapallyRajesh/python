country="INDIA"
class ace:
    clg="ACE COLLEGE"
    def give_details(self,a,b,c,d):
        self.tot=a+b+c
        self.name=d
    def display(self):
        print("1. Name: ",self.name)
        print("2. Marks: ",self.tot)
        print("3. college: ",ace.clg)
        print("4. Country: ",country)

class bvrit:
    clg="BVRIT COLLEGE"
    def set_dim(self,a,b,c,):
        self.tot=a+b
        self.name=c

    def show(self):
        print("1. Name: ",self.name)
        print("2. Marks: ",self.tot)
        print("3. college: ",bvrit.clg)
        print("4. Country: ",country)

        

a=ace()
b=bvrit()
a2=ace()
b2=bvrit()
a.give_details(20,30,40,"RAJESH")
b.set_dim(40,50,"MEERA")
a2.give_details(70,50,30,"RAHUL")
b2.set_dim(50,60,"VAISH")
a.display()
a2.display()
b.show()
b2.show()