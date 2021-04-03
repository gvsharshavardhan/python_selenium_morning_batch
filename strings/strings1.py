name = "mounika yadala"

l = name.split()

fname = ""

for n in l:
    fname = fname + n[::-1] + " "

print(len(fname))
print(len(fname.strip()))
