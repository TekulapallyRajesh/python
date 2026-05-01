Name=input("Enter your name: ")
Gender=input("Enter your Gender: ")
age=int(input("enter your age: "))
if age<18:
    print(f"{Name} is not eligible")
if age>60:
    print(f"{Name} is eligible")
if Gender == "M" and age<30:
    print(f"{Name} is not eligible ")
else:
    print(f"{Name} is eligible")