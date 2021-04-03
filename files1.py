import random


with open("E:/python_morning_Sessions/notes200.txt", "a") as f:

    def otp(size):
        myotp = ""
        for i in range(size):
            myotp = myotp + str(random.randint(0, 9))
        return myotp

    sec_num = otp(20)
    f.write("\n"+sec_num)
