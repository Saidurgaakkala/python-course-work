Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
t=(1,2,3,4,5,)
t
(1, 2, 3, 4, 5)
t=()
t
()
t
()
t=(1,2,3,4,5,)
h=(90+3+10)
t+h
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    t+h
TypeError: can only concatenate tuple (not "int") to tuple
t
(1, 2, 3, 4, 5)
h=(90,80,98)
t+h
(1, 2, 3, 4, 5, 90, 80, 98)
t*4
(1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
t
(1, 2, 3, 4, 5)
t[1]
2
t[3]
4
t[1]
2
t[6]
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    t[6]
IndexError: tuple index out of range
t[2]
3
t
(1, 2, 3, 4, 5)
t[:3]
(1, 2, 3)
t[1:4]
(2, 3, 4)
t[2:]
(3, 4, 5)
t[::2]
(1, 3, 5)
t[:-1]
(1, 2, 3, 4)
t[:-2]
(1, 2, 3)
t[:-3]
(1, 2)
t[:-4]
(1,)
t[:-0]
()
t[::2]
(1, 3, 5)
t[1:4]
(2, 3, 4)
t[-1:-4:-1]
(5, 4, 3)
t
(1, 2, 3, 4, 5)
1 in t
True
3 in t
True
4 not in t
False
5 not in t
False
t
(1, 2, 3, 4, 5)
len(t)
5
sort(t)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    sort(t)
NameError: name 'sort' is not defined. Did you mean: 'sorted'?
sorted(t)
[1, 2, 3, 4, 5]
min(t)
1
sum(t)
15
t.count(10)
0
t.index(2)
1
t.index(0)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    t.index(0)
ValueError: tuple.index(x): x not in tuple
a,b,c=(1,2,3)
a
1
b
2
3
3
c
3
a
1
a,b,c
(1, 2, 3)
x,y,z=a
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    x,y,z=a
TypeError: cannot unpack non-iterable int object
t=(1,2,3,[4,5,6],7,8)
t
(1, 2, 3, [4, 5, 6], 7, 8)
t[2]
3
t[4]
7
t[3]
[4, 5, 6]
t[3].append(10)
t
(1, 2, 3, [4, 5, 6, 10], 7, 8)
a=(1,2,4)
a
(1, 2, 4)
x,y,z=a
x
1
y
2
y
2

=============================== RESTART: Shell ==============================
s={1,2,3,4}
s
{1, 2, 3, 4}
s=set()
s={1,1,1,1,1,1,1,}
s
{1}
s={987,678,356,678,1,2,3,4,8}
s=set()
s
set()
s.add(1)
s
{1}
s.add(45)
s
{1, 45}
s
{1, 45}
s.add(True)
s
{1, 45}
s.add(False)
s
{False, 1, 45}
s.add("kjh")
s
{False, 1, 'kjh', 45}
s.add([1,2,3,4,4])
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    s.add([1,2,3,4,4])
TypeError: unhashable type: 'list'
s
{False, 1, 'kjh', 45}
1 in s
True
2 in s
False
False not in s
False
a={1,2,3,5,6,8,10}
b={6,7,8,9,3}
a|b
{1, 2, 3, 5, 6, 7, 8, 9, 10}
a.union(b)
{1, 2, 3, 5, 6, 7, 8, 9, 10}
{1, 2, 3, 5, 6, 7, 8, 9, 10}
{1, 2, 3, 5, 6, 7, 8, 9, 10}

a.intersection(b)
{8, 3, 6}
a&b
{8, 3, 6}
a-b
{1, 2, 10, 5}
a^b
{1, 2, 5, 7, 9, 10}

=============================== RESTART: Shell ==============================
#{1}{2}{3}{4}{5}{6}{4,4}{8,3}
a<={1}
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    a<={1}
NameError: name 'a' is not defined
a <= {1}
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    a <= {1}
NameError: name 'a' is not defined
a <= {1}
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    a <= {1}
NameError: name 'a' is not defined
a <= {1,2,3,4,5,6,7,8,10,11,12,13}
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    a <= {1,2,3,4,5,6,7,8,10,11,12,13}
NameError: name 'a' is not defined
a={1,2,3,5,6,8,10}
b={6,7,8,9,3}
SyntaxError: multiple statements found while compiling a single statement
a={1,2,3,5,6,8,10}
b={6,7,8,9,3}
a|b
{1, 2, 3, 5, 6, 7, 8, 9, 10}
a <= {1}
False
a >= {2}
True
a.isdisjoint(b)
False
a.isdisjoint({90,80})
True
a.add(17)
a
{1, 2, 3, 17, 5, 6, 8, 10}
a.add(14)
a
{1, 2, 3, 5, 6, 8, 10, 14, 17}
a.update({11,12,13})
a
{1, 2, 3, 5, 6, 8, 10, 11, 12, 13, 14, 17}
a.pop()
1
a.pop()
2
a.pop()
3
a.remove(10)
a
{5, 6, 8, 11, 12, 13, 14, 17}
>>> a.discard(6)
>>> a
{5, 8, 11, 12, 13, 14, 17}
>>> a.discard(12)
>>> a
{5, 8, 11, 13, 14, 17}
>>> a.clear()
>>> a
set()
>>> a={1,23,4,57,235}
>>> b={1,2,34,4}
>>> a.intersection(b)
{1, 4}
>>> a
{1, 4, 23, 57, 235}
>>> b
{1, 2, 4, 34}
>>> a.intersection_update(b)
>>> a
{1, 4}
>>> b
{1, 2, 4, 34}
>>> b
{1, 2, 4, 34}
>>> c=b
>>> c.add(12)
>>> c
{1, 2, 34, 4, 12}
>>> b
{1, 2, 34, 4, 12}
>>> len(c)
5
>>> min(c)
1
>>> max(c)
34
>>> sorted(c)
[1, 2, 4, 12, 34]
>>> sum(c)
53
