n= int(input("please enter any number: "))
if n%2==0:
    print("value is even")
    if n>1000:
        print("Even value is larger")
    elif n<1000:
        print("Even vaule is just right")   
else:
    print("value is odd")