import random
r=random.randint(1,100)

a=int(input("enter number of times u want this program to run"))
for i in range(0,a):
    n=int(input("enter guessed number"))
    if n>r:
        print("too high")
    elif n<r:
        print("too low")    
    elif n==r:
        print("congrats!") 
else:
        print("oops! you missed it. computers choice was", r)     