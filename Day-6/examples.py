Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
name= input()
sai
name
'sai'
name = input("enter your name:)
             
SyntaxError: unterminated string literal (detected at line 1)
name=input("enter your name:")
             
enter your name:sai
name
             
'sai'
age=input("enter your age:")
             
enter your age:23
age
             
'23'
type(age)
             
<class 'str'>
gpa=("enter your gpa:")
             
enter the gpa:
             
SyntaxError: invalid syntax
gpa=float(input("enter the cpa:")

          enter the cpa:
          
SyntaxError: '(' was never closed
gpa = float(input("enter the cpa:"))
          
enter the cpa:8.5
gpa
          
8.5
type(gpa)
          
<class 'float'>
'sai veda rishi sruj'
          
'sai veda rishi sruj'
'sai veda rishi sruj'.split('')
          
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    'sai veda rishi sruj'.split('')
ValueError: empty separator
names=input("enter the names:").split()
          
enter the names:sai veda rishi sruj
name
          
'sai'
names
          
['sai', 'veda', 'rishi', 'sruj']
products=input("enter the products:").split()
          
enter the products:laptop mouse keyboard
products
          
['laptop', 'mouse', 'keyboard']
topics= tuple(input("enter the topics:").split())
          
enter the topics:token statement variable comments
topics
          
('token', 'statement', 'variable', 'comments')
op=set(input("enter the oper:").split())
          
enter the oper:in not in is is not and or not
op
          
{'or', 'is', 'and', 'in', 'not'}
marks=input("enter the marks:").split())
             
SyntaxError: unmatched ')'
marks=input("enter the marks:").split()
             
enter the marks:34 56 72 77 89
marks
             
['34', '56', '72', '77', '89']
map(int,input("enter the marks:").split())
             
enter the marks:5 6 7 8 9 
<map object at 0x00000154C193CD00>
list(map(int,input("enter the marks:").split()))
             
enter the marks:1 3 5 10 15
[1, 3, 5, 10, 15]
prices=tuple(map(int,input("enter the prices:").split())))
SyntaxError: unmatched ')'
prices=tuple(map(int,input("enter the prices:").split()))
enter the prices:234 456 789 890
prices
(234, 456, 789, 890)
rating = set(map(int,input("enter thr rating:").split()))
enter thr rating:2 3 4 5 6 7 6
rating
{2, 3, 4, 5, 6, 7}
per =list(map(float,input("enter the per's:").split()))
enter the per's:56.8 32.8 76.9
pers
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    pers
NameError: name 'pers' is not defined. Did you mean: 'per'?
per
[56.8, 32.8, 76.9]
prices=tuple(map(float,input("enter the prices:").split()))
enter the prices:3456 6745 7634 7835
prices
(3456.0, 6745.0, 7634.0, 7835.0)
username,password=input("enter the username&password:").split())
SyntaxError: unmatched ')'
username,password=input("enter the username&password:").split()
enter the username&password:codegnan sai@123
password
'sai@123'
username
'codegnan'
a,b,c,d=list(map(int,input("enter the 4 sides:").split()))
enter the 4 sides:3 4 5 6
a
3
b
4
c
5
d
6
prices,discount=list(map(float,input().split()))
54367 87.0
price
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    price
NameError: name 'price' is not defined. Did you mean: 'prices'?
prices
54367.0
>>> discount
87.0
>>> a=eval(input())
32456
>>> a
32456
>>> a=eval(input())
2345.879
>>> a
2345.879
>>> 
=============================== RESTART: Shell ==============================
>>> s='python programming lang'
>>> s
'python programming lang'
>>> type(s)
<class 'str'>
>>> s=''
>>> s
''
>>> a='codegenen'
>>> b='pfs'
>>> a+b
'codegenenpfs'
>>> a*10
'codegenencodegenencodegenencodegenencodegenencodegenencodegenencodegenencodegenencodegenen'
>>> '*'*20
'********************'
>>> 'python'*6
'pythonpythonpythonpythonpythonpython'
>>> 'python' *6
'pythonpythonpythonpythonpythonpython'
>>> 'python' '*6
SyntaxError: unterminated string literal (detected at line 1)
>>> 'python' *6
'pythonpythonpythonpythonpythonpython'
>>> 
=============================== RESTART: Shell ==============================
