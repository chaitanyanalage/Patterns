"""

A 
B B 
C C C 
D D D D 
E E E E E 

"""
n=int(input("Enter triangle height: "))

num =65

for i in range(n):
    for j in range(i+1):
        ch = chr(num)
        print(ch,end=" ")

    num = num+1
    print()