

quizdict = {}
with open("E:/python_morning_Sessions/quiz.txt", "r") as f:
    d = f.readline()
    quizdict[d] = f.readline()

print(quizdict)
