s1 = input("enter string1: ")
s2 = input("enter string2: ")

n1 = int(input("enter num1: "))
n2 = int(input("enter num2: "))

if s1==s2 and n1==n2:
    print("AND")
elif s1==s2 or n1==n2:
    print("OR")
elif s1!=s2 and n1!=n2:
    print("NONE")
