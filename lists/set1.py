# Q) Write a Program to Print different Vowels Present in the
#  given sentence?

w = "harsha vardhan python sessions"
o = {"a", "e", "i", "o", "u"}

ws = set(w)
print(ws.intersection(o))
