from tkinter import *
a=Tk()
a.geometry("400x500")
a.title("CALCULATOR")
x=Entry(a,width=150,text=('Arial',60))
x.grid(column=0,row=0,columnspan=60)
def click(num):
    cur=x.get()
    x.delete(0,END)
    x.insert(0,str(cur)+str(num))

def clear():
    x.delete(0,END)

def equal():
    res=eval(x.get())
    x.delete(0,END)
    x.insert(0,res)


















Button(a,text="1",width=6,height=3,command=lambda:click(1)).grid(row=1,column=0)
Button(a,text="2",width=6,height=3,command=lambda:click(2)).grid(row=1,column=1)
Button(a,text="3",width=6,height=3,command=lambda:click(3)).grid(row=1,column=2)
Button(a,text="+",width=6,height=3,command=lambda:click("+")).grid(row=1,column=3)


Button(a,text="4",width=6,height=3,command=lambda:click(4)).grid(row=2,column=0)
Button(a,text="5",width=6,height=3,command=lambda:click(5)).grid(row=2,column=1)
Button(a,text="6",width=6,height=3,command=lambda:click(6)).grid(row=2,column=2)
Button(a,text="-",width=6,height=3,command=lambda:click("-")).grid(row=2,column=3)


Button(a,text="7",width=6,height=3,command=lambda:click(7)).grid(row=3,column=0)
Button(a,text="8",width=6,height=3,command=lambda:click(8)).grid(row=3,column=1)
Button(a,text="9",width=6,height=3,command=lambda:click(9)).grid(row=3,column=2)
Button(a,text="*",width=6,height=3,command=lambda:click("*")).grid(row=3,column=3)



Button(a,text="C",width=6,height=3,command=clear).grid(row=4,column=0)
Button(a,text="0",width=6,height=3,command=lambda:click(0)).grid(row=4,column=1)
Button(a,text="=",width=6,height=3,command=equal).grid(row=4,column=2)
Button(a,text="/",width=6,height=3,command=lambda:click("/")).grid(row=4,column=3)







a.mainloop()

