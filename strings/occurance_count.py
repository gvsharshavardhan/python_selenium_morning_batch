demo = "A total of 70 districts in 16 states have registered more than 150 per cent increase in active COVID-19 cases from March 1-15, the Union Health Ministry said on Wednesday."
anotherDemo = ""

for i in demo:
    if i not in anotherDemo and not i.isalpha() and not i.isnumeric():
        anotherDemo = anotherDemo + i

print(anotherDemo)

for i in anotherDemo:
    print(i, demo.count(i))
