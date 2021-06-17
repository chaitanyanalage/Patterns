"""
1
12
123
1234
12345

"""
n = int(input("Enter triangle height: "))

num = 1

for i in range(n):
    num = 1

    for j in range (i+1):
        print(num,end="")

        num = num+1

    print()