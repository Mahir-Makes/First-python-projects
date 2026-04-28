import random 
a=random.randint(1,100)
b=0
tries=0
while b!=a:
    b=int(input("guess the number: "))
    tries = tries+1
    if b>a:
        print("too high")
    elif b<a:
        print("too low")
    else:
        print("you won")
print(f"You won! It took you {tries} tries.")