def giveRequiredNumbers(start, stop, type):
    numbersList = []
    c = 0
    if type == "even":
        c = 0
    elif type == "odd":
        c = 1
    else:
        return "please enter valid value (even or odd)"

    for i in range(start, stop):
        if i % 2 == c:
            numbersList.append(i)
    return numbersList


# print(giveRequiredNumbers(45, 89, type="harsha"))
print(giveRequiredNumbers(38, 139, type="odd"))
