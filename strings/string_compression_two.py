"""string compression:
--------------------
input : kkkmmlllllkk
output : k3m2l5k2

input : kkkmmlllllk
output : k3m2l5k1
"""

inputstring = "kkkmmlllllk"
outputstring = ""
counter = 1
for i in range(1, len(inputstring)):  # 1 2 3 4 5 6 7 8 9 10 11
    if inputstring[i] == inputstring[i-1]:
        counter = counter + 1
    else:
        outputstring = outputstring + inputstring[i-1] + str(counter)
        counter = 1
outputstring = outputstring + inputstring[-1] + str(counter)

print(outputstring)
