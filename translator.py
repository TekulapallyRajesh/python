from googletrans import Translator
t=Translator()
a=input("enter text you want to convert: ")
b=input("enter language to convert: ")
res=t.translate(a,dest=b)
print(res.text)