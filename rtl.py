n=int(input("Enter Triangle Height: "))

for i in range(n):
    for j in range(1,n-i):
        print(" ",end="")
    
    for k in range(n-i,n+1):
        print("*",end="")

    print()

    #APPPU THANK YOU