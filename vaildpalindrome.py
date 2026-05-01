a=input("enter word: ")
b="".join(i for i in a if i.isalnum)
if b==(b[::-1]):
    print(f"{b} is palindrome")
else:
    print(f"{b} is not a palindrome")