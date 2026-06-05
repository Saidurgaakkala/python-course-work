Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s=' hello   world  '
s
' hello   world  '
s.strip()
'hello   world'
s.lstrip()
'hello   world  '
s.rstrip()
' hello   world'
s='string.py'
s.startswith('str')
True

=============================== RESTART: Shell ==============================
s='string.py'
s.startswith('str')
True
s.startswith('gfh')
False
s.endswith('py')
True
s,endswith('js')
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    s,endswith('js')
NameError: name 'endswith' is not defined
s.endswith('js')
False
'sdfyui'.isalpha()
True
'sdfyui'isalnum()
SyntaxError: invalid syntax
'sdfyui'.isalnum()
True
True
True

'DSFGHJdjkrjkfekf'.isaplha()
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    'DSFGHJdjkrjkfekf'.isaplha()
AttributeError: 'str' object has no attribute 'isaplha'. Did you mean: 'isalpha'?
'DSFGHJdjkrjkfekf'.isalpha()
True
'sai@21234'.isalnum()
False
'ewdjdg'.islower()
True
'UYcdjcsvbd'.isupper()
False
'GSHFGSDFHHSJF'.isupper()
True
'jsbnd '.isspace()
False
' ' .isspace()
True
'hello'    .ispace()
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    'hello'    .ispace()
AttributeError: 'str' object has no attribute 'ispace'. Did you mean: 'isspace'?
'hello'    .isspace()
False
'hello   '.isspace()
False
'Python'.istitle()
True
'ytfg'.istitle()
False

=============================== RESTART: Shell ==============================
type(1)
<class 'int'>
==[1,2,3,4,5]
SyntaxError: invalid syntax
l=[1,2,3,4,5]
m=[8,8,9,0,6]
l+m
[1, 2, 3, 4, 5, 8, 8, 9, 0, 6]

=============================== RESTART: Shell ==============================
l=[1,2,3,4,5]
m=[8,8,9,0,6]
SyntaxError: multiple statements found while compiling a single statement
l=[1,2,3,4,5]
m=[8,8,9,0,6]
l+m
[1, 2, 3, 4, 5, 8, 8, 9, 0, 6]
1*4
4
l*4
[1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
l
[1, 2, 3, 4, 5]
[10,20,30,40,50]
[10, 20, 30, 40, 50]
l=[10,20,30,40,50]
l(4)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    l(4)
TypeError: 'list' object is not callable
l[4]
50
l[2]
30
l[3]
40
1[0]
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    1[0]
TypeError: 'int' object is not subscriptable
l[0]
10
l[1]
20
l[-1]
50
l[-3]
30
l[1:4]
[20, 30, 40]
1[1:5]
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    1[1:5]
TypeError: 'int' object is not subscriptable
l[::-1]
[50, 40, 30, 20, 10]
l[1:5]
[20, 30, 40, 50]
2o in 1
SyntaxError: invalid decimal literal
20 in 1
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    20 in 1
TypeError: argument of type 'int' is not iterable
70 not in l
True
20 in l
True
30 in l
True
l
[10, 20, 30, 40, 50]
id[1]
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    id[1]
TypeError: 'builtin_function_or_method' object is not subscriptable
id[1]
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    id[1]
TypeError: 'builtin_function_or_method' object is not subscriptable
l[4]
50
l[4]=100
l
[10, 20, 30, 40, 100]
l.append(120)
l
[10, 20, 30, 40, 100, 120]
l.append(400)
l
[10, 20, 30, 40, 100, 120, 400]
l.append(500)
l
[10, 20, 30, 40, 100, 120, 400, 500]
l.insert(1,5)
l
[10, 5, 20, 30, 40, 100, 120, 400, 500]
l.insert(4,50)
l
[10, 5, 20, 30, 50, 40, 100, 120, 400, 500]
l.extend([67.89.09,99])
SyntaxError: invalid syntax. Perhaps you forgot a comma?
l.extend([70.89.09,99])
SyntaxError: invalid syntax. Perhaps you forgot a comma?
l.extend[[80,90,110])
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
l.extend([80,90,110])
l
[10, 5, 20, 30, 50, 40, 100, 120, 400, 500, 80, 90, 110]
l.pop(1)
5
l
[10, 20, 30, 50, 40, 100, 120, 400, 500, 80, 90, 110]
l.remove(100)
l
[10, 20, 30, 50, 40, 120, 400, 500, 80, 90, 110]
l.clear(500)
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    l.clear(500)
TypeError: list.clear() takes no arguments (1 given)
l.pop(3)
50
l
[10, 20, 30, 40, 120, 400, 500, 80, 90, 110]
l.clear()
l
[]
l
[]
del l[1]
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    del l[1]
IndexError: list assignment index out of range
l.del()
SyntaxError: invalid syntax
del()
l
[]
l=[200,60,80,90,30,50,20,10,300]
sorted[l]
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    sorted[l]
TypeError: 'builtin_function_or_method' object is not subscriptable
sorted[l]
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    sorted[l]
TypeError: 'builtin_function_or_method' object is not subscriptable
l
[200, 60, 80, 90, 30, 50, 20, 10, 300]
l.sort()
l
[10, 20, 30, 50, 60, 80, 90, 200, 300]
min(l)
10
max(l)
300
l
[10, 20, 30, 50, 60, 80, 90, 200, 300]
l.reverse()
l
[300, 200, 90, 80, 60, 50, 30, 20, 10]
l.sorted(reverse=True)
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    l.sorted(reverse=True)
AttributeError: 'list' object has no attribute 'sorted'. Did you mean: 'sort'?
>>> sorted(l,reverse=True)
[300, 200, 90, 80, 60, 50, 30, 20, 10]
>>> l.index(200)
1
>>> l.inder(90)
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    l.inder(90)
AttributeError: 'list' object has no attribute 'inder'. Did you mean: 'index'?
>>> l
[300, 200, 90, 80, 60, 50, 30, 20, 10]
>>> l.index(10)
8
>>> l.count(90)
1
>>> l
[300, 200, 90, 80, 60, 50, 30, 20, 10]
>>> m=l
>>> m
[300, 200, 90, 80, 60, 50, 30, 20, 10]
>>> m.append(700)
>>> m
[300, 200, 90, 80, 60, 50, 30, 20, 10, 700]
>>> l
[300, 200, 90, 80, 60, 50, 30, 20, 10, 700]
>>> len(1)
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    len(1)
TypeError: object of type 'int' has no len()
>>> len(l)
10
>>> l
[300, 200, 90, 80, 60, 50, 30, 20, 10, 700]
>>> any([1,2,4,5,5,0,0,0,0,])
True
>>> all([1,2,4,5,5,0,0,0,0])
False
