from random import randint
quizdict = {}
data = []

with open("E:/python_morning_Sessions/quiz.txt", "r") as f:
    data = f.readlines()

for i in data:
    d = i.split(":")
    quizdict[d[0]] = d[1][:len(d[1])-1]

q = list(quizdict.items())
# i = randint(0, len(q)-1)

score = 0
for i in q:
    print(i[0])
    ans = input("enter your ans: ")
    if ans == i[1]:
        score += 1
    else:
        score -= 1

print("your score is: {}".format(score))
