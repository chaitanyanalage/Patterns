"""
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 

"""
n = int(input("Enter triangle height: "))
num = 1
for i in range(n):
    for j in range(i+1):
        print(num,end=" ")
        num = num+1

    print()