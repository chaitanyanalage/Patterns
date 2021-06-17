"""

A 
B C 
D E F 
G H I J 
K L M N O 

"""
n = int(input("Enter triangle eight: "))
num=65

for i in range(n):
    for j in range(i+1):
        ch = chr(num)
        print(ch,end=" ")
        num = num + 1
    print()