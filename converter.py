while True:
    b=input("""chose an conversion: 
 1|c-f,   2|f-c,
 3|kg-lb, 4|lb-kg,
 5|cm-in, 6|in-cm,
 7|m-feet,8|feet-m,
 9|oz-gm,10|gm-oz,
11|km-mi,12|mi-km,
13|li-ga,14|ga-li 
     """)
    a=float(input("type ammount: "))
    if b == "3":
        print(a/0.4536)
    elif b== "4":
        print(a*.4536)
    elif b== "5":
        print(a/2.54)
    elif b== "6":
        print(a*2.54)
    elif b== "1":
        print(a*1.8+32)
    elif b== "2":
        print((a-32)/1.8)
    elif b== "7":
        print(a*3.28)
    elif b== "8":
        print(a/3.28)
    elif b== "9":
        print(a*28.35)
    elif b== "10":
        print(a/28.35)
    elif b== "11":
        print(a/1.61)
    elif b== "12":
        print(a*1.61)
    elif b== "13":
        print(a/3.785)
    elif b== "14":
        print(a*3.785)