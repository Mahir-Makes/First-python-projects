import random
while True:
    b=input("").lower()
    a=random.randint(1,9999)
    if b=="exit":
        break
    if a < 9:
        print("000"+str(a))
    elif a < 99:
        print("00"+str(a))
    elif a < 999:
        print("0"+str(a))
    else:
        print(a)