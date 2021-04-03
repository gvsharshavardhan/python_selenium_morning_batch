"""string compression:
--------------------
input : kkkmmlllll
output : k3m2l5"""

inputString = "kkkmmlllll"
outputString = ""

for i in inputString:
    temp = i+str(inputString.count(i))
    if temp not in outputString:
        outputString = outputString + temp


print(outputString)
