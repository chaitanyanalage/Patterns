# Rightangle Triangle using 2xfor loop
n = int(input("Enter Triangle height:"))


for i in range(n):

    for j in range(i+1):
        print("*", end="")

    # print * on next line
    print()
