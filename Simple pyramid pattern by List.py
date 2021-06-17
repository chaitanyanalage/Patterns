"""
*
**
***
****
*****

"""
# Printing Rightangle triangle using list

# taking input from user
n = int(input("Enter Rightangle Triangle height: "))

myList = []

for i in range(1, n+1):
    myList.append("*"*i)

print("\n".join(myList))
i