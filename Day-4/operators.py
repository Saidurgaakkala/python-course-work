Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=10
b=10
a+b
20
a-b
0
a*b
100
a/b
1.0
a//b
1
a%b
0
a**b
10000000000

=============================== RESTART: Shell ==============================
a
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a
NameError: name 'a' is not defined
a=20
b=20
a<b
False
a>b
False
a<=b
True
a>=b
True
a==b
True
a!=b
False

=============================== RESTART: Shell ==============================
a=25
b=30
a=b
a+=5
a
35
a*=
SyntaxError: invalid syntax
a*=3



=============================== RESTART: Shell ==============================
a=4
b=3
a+=1
a
5
b+=13
b
16
a=+2
a
2
a*=2
a
4
a%=4
a
0

=============================== RESTART: Shell ==============================
a%10==0
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    a%10==0
NameError: name 'a' is not defined
a=10
b=30
a%==5
SyntaxError: invalid syntax
a%==0
SyntaxError: invalid syntax
a%2==0
True
a=%5
SyntaxError: invalid syntax
a>b
False
b<a
False
a==b
False
not a>b
True
or b>a
SyntaxError: invalid syntax
and a>b
SyntaxError: invalid syntax
a%10==0 or b%30==0 or a<b
True
a%12==0 or b%20==0 or b>a
True
not a<b
False
not a>b
True

=============================== RESTART: Shell ==============================
a='python programming'
a
'python programming'
'n' in a
True
'z' in a
False
'a' not a
SyntaxError: invalid syntax
't' not a
SyntaxError: invalid syntax
't' not in a
False
'v' not in a
True
'p' not in a
False
'o' not in b
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    'o' not in b
NameError: name 'b' is not defined
'c' not in a
True
t=('watch','choco','pen','pizza')
'laptop' in t
False
t=(1,2,3,,55,76,87}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
4 in t
False
1 in t
False
d={'egg':5,'water':9,'pen':20}
water in t
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    water in t
NameError: name 'water' is not defined. Did you mean: 'iter'?
'water' in t
False
'pencil' in t
False
l=['html','css','java','python']
l
['html', 'css', 'java', 'python']
'html' in l
True

=============================== RESTART: Shell ==============================
l=[1,2,3]
m=[1,2,3]
l==m
True
n=m
n
[1, 2, 3]
n==m
True
l is m
False
m is l
False
n is not m
False
n is m
True
m is m
True
n is n
True

=============================== RESTART: Shell ==============================
8 & 3
0
8 & 7
0
8 | 7
15
8 ^ 5
13
>>> 8~7
SyntaxError: invalid syntax
>>> 8 ~ 3
SyntaxError: invalid syntax
>>> 8 ~ 8
SyntaxError: invalid syntax
>>> ~12
-13
>>> ~7
-8
>>> ~66
-67
>>> 6>>6
0
>>> 8>>2
2
>>> 88>>5
2
>>> 15>>1
7
>>> 15>>2
3
>>> 16<<3
128
>>> 
=============================== RESTART: Shell ==============================
>>> a=12
>>> b=12.34
>>> c='python'
>>> print(a,b,c)
12 12.34 python
>>> print("a=",a,'b',b,'c='c,sep=',end='@@@@@')
...       
SyntaxError: unterminated string literal (detected at line 1)
>>> print("a=",a,'b=',b,'c='c,sep=',end='@@@@@')
...       
SyntaxError: unterminated string literal (detected at line 1)
>>> print("a=",a,'b=',b,'c='c,sep='',end='@@@@@')
...       
SyntaxError: invalid syntax. Perhaps you forgot a comma?
