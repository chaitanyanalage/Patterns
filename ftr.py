"""

*****
 ****
  ***
   **
    *

"""
n=int(input("Enter triangle height"))

for i in range(n):

    for j in range(i):
        print(" ",end=(""))
    
    k=i

    for k in range(i,n):
        print("*",end=(""))

    print()