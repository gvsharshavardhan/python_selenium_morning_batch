from random import randint


def goodMorning():
    print("***************")
    print("Good morning!")
    print("***************")


def areaOfATriangle(base, height):
    area = base*height*0.5
    return area


salary = 4500


def otp(size):
    s = ""
    for i in range(size):
        r = randint(0, 9)
        s = s + str(r)
    return int(s)
