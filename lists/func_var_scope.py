print("start!!!")


def test1():
    global a
    a = 10

    def test2():
        b = 20
        print("test 2 : ", a, b)

    print("test 1 : ", a)
    test2()

    return test2


t = test1()
print("type : ", type(t))
t()
