'''
* * * * *
# # # # #
* * * * *
# # # # #
* * * * *
'''
# rows = int(input("enter a num of rows: "))
# design = input("please enter a design to print: ")
#rows
# 1,5
design = """
sample design:
----------------
*   
$ $ 
* * *
$ $ $ $
* * * * *
$ $ $ $ $ $

"""
print(design)
rows = int(input("enter a num of rows: "))
for i in range(1,rows+1):
        if i%2==1:
            print("* " * i)
        else:
            print("$ " * i)
    









