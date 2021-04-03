from random import randint
quizdict = {}
datafromfile = []

with open("E:/python_morning_Sessions/quiz.txt", "r") as f:
    datafromfile = f.readlines()

for i in datafromfile:
    line = i.split(":")
    quizdict[line[0]] = line[1][:len(line[1])-1]

quizQandA = list(quizdict.items())
# i = randint(0, len(q)-1)

score = 0
for qa in quizQandA:
    print(qa[0])
    ans = input("enter your ans: ")
    if ans == qa[1]:
        score += 1
    else:
        score -= 1

print("your score is: {}".format(score))
