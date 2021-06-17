"""

    * 
   * * 
  * * * 
 * * * * 
* * * * * 

"""

n=int(input("enter triangle side length: "))

space = n-1

for i in range (n):
    for j in range(space):
        print(" ",end="")

    #decrementing space by 1
    space = space-1

    for j in range(0,i+1):
        print("* ",end="")

    print()
