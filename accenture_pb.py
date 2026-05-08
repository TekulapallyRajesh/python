a=int(input('enter any number1: '))
b=int(input('enter any number2: '))
c=int(input('enter any number3: '))

list1=[int(i)for i in str(a)]
list2=[int(i)for i in str(b)]
list3=[int(i)for i in str(c)]
sum1=max(list1)+max(list2)+max(list3)
sum2=min(list1)+min(list2)+min(list3)
print(sum1+sum2)

