from random import randint
quizdict = {}
data = []

with open("E:/python_morning_Sessions/quiz.txt", "r") as f:
    data = f.readlines()

for i in data:
    d = i.split(":")
    quizdict[d[0]] = d[1][:len(d[1])-1]

q = list(quizdict.items())
score = 0
while len(q) != 0:
    i = randint(0, len(q)-1)
    p = q.pop(i)
    print(p[0])
    ans = input("enter your ans: ")
    if ans == p[1]:
        score += 1
    else:
        score -= 1

print("your score is: {}".format(score))
