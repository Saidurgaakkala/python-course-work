Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=10
type(a)
<class 'int'>
l=[]
l=list()
type(l)
<class 'list'>
t=()
t=(1,2,3,4,5)
type(t)
<class 'tuple'>
str="sai"
status=true
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    status=true
NameError: name 'true' is not defined. Did you mean: 'True'?
status=True
status=False
status=False
type(status)
<class 'bool'>
a=None

=============================== RESTART: Shell ==============================
a=10
a
10
float(a)
10.0
complex(b)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    complex(b)
NameError: name 'b' is not defined
complex(b)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    complex(b)
NameError: name 'b' is not defined
bool(b)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    bool(b)
NameError: name 'b' is not defined
bool(a)
True
bool(0)
False
b=10.5
int(b)
10
complex(b)
(10.5+0j)
str(b)
'10.5'
list(b)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    list(b)
TypeError: 'float' object is not iterable
tuple(b)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    tuple(b)
TypeError: 'float' object is not iterable
dict(b)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    dict(b)
TypeError: 'float' object is not iterable
bool(b)
True
bool(0.0)
False
c=2+3j
int(c)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(a)
10.0
float(c)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    float(c)
TypeError: float() argument must be a string or a real number, not 'complex'
str(c)
'(2+3j)'
list(c)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    list(c)
TypeError: 'complex' object is not iterable
tuple(c)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    tuple(c)
TypeError: 'complex' object is not iterable
set(c)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    set(c)
TypeError: 'complex' object is not iterable
float(a)
10.0
float(b)
10.5
list(a)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
type(a)
<class 'int'>
list[10,20,30,40]
list[10, 20, 30, 40]
list(a)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
list(s)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    list(s)
NameError: name 's' is not defined
tuple(s)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    tuple(s)
NameError: name 's' is not defined
a=[]
a=[10,20,30]
int(a)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    int(a)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
>>> tuple(a)
(10, 20, 30)
>>> str(a)
'[10, 20, 30]'
>>> complex(a)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    complex(a)
TypeError: complex() first argument must be a string or a number, not 'list'
>>> set?9a)
SyntaxError: invalid decimal literal
>>> set(a)
{10, 20, 30}
>>> bool(a)
True
>>> bool(0)
False
>>> complex(b)
(10.5+0j)
>>> l=[1,2,3,4,5,6,7,8]
>>> int(l)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    int(l)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
>>> flaot(l)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    flaot(l)
NameError: name 'flaot' is not defined. Did you mean: 'float'?
>>> float(l)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    float(l)
TypeError: float() argument must be a string or a real number, not 'list'
>>> str(l)
'[1, 2, 3, 4, 5, 6, 7, 8]'
>>> bool(l)
True
