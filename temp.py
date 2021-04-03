isSunny= input("is it sunny (True/False) :")

if isSunny =='True':
    temp= int(input("please enter temp outside: "))
    print("It is sunny outside!!")
    if temp>85:
        print("I'll go to beach!!")
    else:
        print("Ill go to park!!")
else:
    print("practice java!!")