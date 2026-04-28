import random
e=random.randint(1,9999)
if e < 10:
    ("000"+str(e))
elif e < 100:
    ("00"+str(e))
elif e < 1000:
    ("0"+str(e))
else:
    (e)
print(" To enter femboy land please login or sign in.")
a=input(" Login or sign in: ").lower()
if a =="login":
    f=input(" Enter gmail: ")
    if "@gmail.com" in f:
        b=input("enter password: ")
        if b=="1234":
            print(' Logged in succesfully.')
            print(" Welcome back! to femboy land, user.")
        else:
         print(" Login failed. Try again later.")
    else:
         print(" Login failed. Try again later.")
elif a=="sign in":
    b=input(" Enter gmail: ")
    if "@gmail.com" in b:
        print("""We have sent a code to ur gmail.
        
 Code from gmail: """+str(e))
        c=input(" Enter code: ")
        if c==str(e):
            print(" Signed in succesfully.")
            print(" Welcome! to femboy land, user.")
        else:
            print(" Wrong code. Try again later.")
elif ("") in a:
    print(" Syntax failed. Try again.")