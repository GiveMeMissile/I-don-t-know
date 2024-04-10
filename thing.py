import numpy as NUMP
a = 0
t = 0
while(a == 0 or t == 0):
    try:
        a = int(input("Put in a number that is not zero: "))
        t = int(input("Put in a random number to multiply: "))
    except:
        print("Try again")
b = a * t
c = b * t
d = c * t
e = d * t
listylist = [a, b, c, d, e ]
print(listylist)
f = 0
while f == 0:
    try:
        f = int(input("Put in a random number to divide: "))
    except:
        print("Try again, (Idiot)")
        print("The number will be 2 now")
look = NUMP.array(listylist)
print(look/f)
