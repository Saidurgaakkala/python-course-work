#patterns
'''
n=int(input("enter the size:"))
m=n//2
for i in range(n):
    if i<=m:
        for j in range(i+1):
            print('*',end='')
    else:
        for j in range(n-i):
            print('*',end='')
    print()

#method2
n=int(input("enter the size:"))
m=n//2
for i in range(n):
    if i<=m:
        print('*'*(i+1),end='')
    else:
        print('*'*(n-i),end='')
    print()
    
#print diamond
n = int(input("enter the size: "))
m = n//2
for i in range(n):
    if i<=m:
        print(' '*(m-i),end=' ')
        print('* '*(i+1),end=' ')
    else:
        print(' '*(i-m),end=' ')
        print('* '*(n-i),end=' ')
    print()
   
#method2

n = int(input("enter the size: "))
m = n//2

for i in range(n):
    if i<=m:
        print(' '*(m-i)+'* '*(i+1),end=' ')
    else:
        print(' '*(i-m)+'* '*(n-i),end=' ')
    print()
#hollow square pattern
n=int(input("enter the size: "))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
'''
#square with cross x
n = int(input("Enter the size: "))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1 or j==i or i+j==n-1:
            print('*', end=' ')
        else:

        
            print(' ',end=' ')
    print()



#square with plus
n = int(input("Enter the size: "))
for i in range(n):
    for j in range(n):
        if (i==0 or i==n-1 or j==0 or j==n-1 or i==n//2 or j==n//2):
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()
'''
#H pattern
n=int(input("Enter the size:"))
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==n//2:
            print('*', end=' ')
        else:
            print(" ", end=' ')
    print()

            
            


