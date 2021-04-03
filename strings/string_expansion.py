"""
string expansion:
--------------------
input : k3h1m2l5j4
output : kkkmmlllll"""

inputString = "m3a0b0"  # 012345
finalString = ""

for i in range(len(inputString)):
    if i % 2 == 1:
        finalString = finalString + inputString[i-1] * int(inputString[i])

if len(finalString) < len(inputString):
    print(inputString)
else:
    print(finalString)
