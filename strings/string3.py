demo = """Washington DC police on Wednesday (local time) arrested a Texas man outside Vice President Kamala Harris' official residence, the US Naval Observatory, with a rifle and ammunition recovered from his vehicle"""

demo = demo.replace(",", "")
l = demo.split("'")
testString = l[1].strip()
print(testString)
spl = testString.split()

fdemo = ""
counter = 1
for i in spl:
    if counter % 2 == 1:
        fdemo = fdemo + i[::-1] + " "
    else:
        fdemo = fdemo + i + " "

    counter = counter + 1

print(fdemo.strip())
