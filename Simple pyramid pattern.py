"""
*
**
***
****
*****

"""

#input height from user
n = int(input("Enter Triangle height:"))

#i manages rows
for i in range(n):

    #j manages colums
    for j in range(i+1):
        print("*", end="")

    # print * on next line
    print()
