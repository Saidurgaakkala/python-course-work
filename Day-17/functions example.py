'''syntax:
def function_name(arg):
   #stmts
   return

function_name(para)

def wish(name):
    print(f'Welcome to the python course{name}!')

wish('subbu')
wish('praveen')
wish('rishitha')
wish('saidurga')


def iseven(num):
    if num%2==0:
        return f"{num} - Even Number"
    else:
        return f"{num} - Odd Number"
print(iseven(12))
print(iseven(13))

def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact*=i
    return fact
num = int(input("Enter the number: "))
print("Factorial:",factorial(num))

def isprime(num):
    for i in range(2,num//2):
        if num%i==0:
            return f"{num} - Not Prime Numbers"
        return f"{num} - prime Number"
num = int(input("Enter the number:"))
print(isprime(num))

#positional:

def display(name,email,pwd):
    print("Name:",name)
    print("Email:",email)
    print("password:",pwd)

display('subbu','subbu@gmail.com','subbu@123')
display('sai','sai@gmail.com','sai@123')
display('surya','surya@gmail.com','surya@123')

#keyword argument:

def display(name,email,pwd):
    print("Name:",name)
    print("Email:",email)
    print("password:",pwd)

display(name='subbu',email='subbu@gmail.com',pwd='subbu@123')
display(name='sai',email='sai@gmail.com',pwd='sai@123')
display(name='surya',email='surya@gmail.com',pwd='surya@123')


#default argument:
def display(name,email,pwd=''):
    print("Name:",name)
    print("Email:",email)
    print("password:",pwd)

display('subbu','subbu@gmail.com','subbu@123')
display('sai','sai@gmail.com')

#example2
def display(*names):
    print("Name:",names)


display('subbu','dinesh','naresh','akhil','suri')
display('subbu')
display('subbu','dinesh')
'''
#variable length
def dispplay(**names):
    print("Names",names)
    display(k1='naresh',k2='akhil',k3='nagendra')





        

