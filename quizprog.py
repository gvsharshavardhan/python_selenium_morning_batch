from random import randint
quizdict = {}
datafromfile = []

"""
reading data from file and stoting it in a list.
readlines -> reads data as list of lines(string)
"""
with open("E:/python_morning_Sessions/quiz.txt", "r") as f:
    datafromfile = f.readlines()


"""
seperating questions and answers and adding them to quizdict
"""
for i in datafromfile:
    line = i.split(":")
    quizdict[line[0]] = line[1][:len(line[1])-1]

"""
converting dict to list of tuples(questions and answers)
eg:
---
[(q1,a1),(q2,a2),(q3,a3)]
"""
quizQandA = list(quizdict.items())
# i = randint(0, len(q)-1)


"""
looping through list of tuples(questions and answers) , verifying answers and updating score.
eg:
---
[(q1,a1),(q2,a2),(q3,a3)]
"""
score = 0
for qa in quizQandA:
    print(qa[0])
    ans = input("enter your ans: ")
    if ans == qa[1]:
        score += 1
    else:
        score -= 1


# printing score
print("your score is: {}".format(score))
