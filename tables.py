import time
print("\033[1;31m")
for i in range(1,11):
    time.sleep(1)
    for j in range(1,11):
        print("{:02d}".format(i*j),end=(" "))
    print()