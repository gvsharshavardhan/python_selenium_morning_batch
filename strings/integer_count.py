"""
Five States: Maharashtra, Punjab, Karnataka, Gujarat and Tamil Nadu- continue to drive up India’s Active Cases; account for 71.10% of the 28,903 new cases reported in the last 24 hours.

83.91% of new cases reported from 6 states.

7 + 1 + 1 + 0 + 2 + 8 + 9 + 0 + 3 + 2 + 4 + 8 + 3 + 9 + 1 + 6 = 64


"""

inputstring = """Five States: Maharashtra, Punjab, Karnataka, Gujarat and Tamil Nadu- continue to drive up India’s Active Cases; account for 71 of the 28903 new cases reported in the last 24 hours.

83 of new cases reported from 6 states."""

# 71 + 28903 + 24 + 83 + 6 = 29087

finalcount = 0
temp = "0"

for i in inputstring:
    if i.isdigit():
        temp = temp + i
    else:
        finalcount = finalcount + int(temp)
        temp = "0"
print(finalcount)
