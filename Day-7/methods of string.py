Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> s='python programming'
>>> len(s)
18
>>> sorted(s)
[' ', 'a', 'g', 'g', 'h', 'i', 'm', 'm', 'n', 'n', 'o', 'o', 'p', 'p', 'r', 'r', 't', 'y']
>>> min(s)
' '
>>> max(s)
'y'
>>> ord('a')
97
>>> ord('A')
65
>>> ord('')
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    ord('')
TypeError: ord() expected a character, but string of length 0 found
>>> ord('0')
48
>>> ord('')
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    ord('')
TypeError: ord() expected a character, but string of length 0 found
>>> ord(' ')
32
>>> char(98)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    char(98)
NameError: name 'char' is not defined. Did you mean: 'chr'?
>>> chr(98)
'b'
>>> chr(120)
'x'
>>> chr(30)
'\x1e'
chr(35)
'#'
chr(37)
'%'
chr(65)
'A'

=============================== RESTART: Shell ==============================
s='python programming'
s.upper()
'PYTHON PROGRAMMING'
s.lower()
'python programming'
s.capitalize()
'Python programming'
s.title()
'Python Programming'
s.swapcase()
'PYTHON PROGRAMMING'
s.casefold()
'python programming'

=============================== RESTART: Shell ==============================
s='Python programming'
s.center(28,'-')
'-----Python programming-----'
s.ljust(28,'-')
'Python programming----------'
s.rjust(28,'-')
'----------Python programming'
s.zfill(28,'-')
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    s.zfill(28,'-')
TypeError: str.zfill() takes exactly one argument (2 given)
'123'.zfill(5)
'00123'
'123'.zfill(10)
'0000000123'

=============================== RESTART: Shell ==============================
s='python programming'
s.find(0)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    s.find(0)
TypeError: find() argument 1 must be str, not int
s.find('0')
-1
s.find('o')
4
s.rfind('o')
9
s.index('o')
4
s.index('z')
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    s.index('z')
ValueError: substring not found
s
'python programming'
s.count('y')
1
s.count('s')
0
s.count('m')
2
s
'python programming'
s.replace('python','java')
'java programming'
s.maketrans('python','12345')
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    s.maketrans('python','12345')
ValueError: the first two maketrans arguments must have equal length
s.maketrans('python','12345')
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    s.maketrans('python','12345')
ValueError: the first two maketrans arguments must have equal length
s.maketransalte('python','12345')
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    s.maketransalte('python','12345')
AttributeError: 'str' object has no attribute 'maketransalte'. Did you mean: 'maketrans'?
s.maketrans('python','java')
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    s.maketrans('python','java')
ValueError: the first two maketrans arguments must have equal length
s.maketrans('python','12345')
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    s.maketrans('python','12345')
ValueError: the first two maketrans arguments must have equal length
s.translate('python','12345')
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    s.translate('python','12345')
TypeError: str.translate() takes exactly one argument (2 given)

=============================== RESTART: Shell ==============================
s='java,python,javascript,c,c++'
s.split(',')
['java', 'python', 'javascript', 'c', 'c++']
s.split(',',2)
['java', 'python', 'javascript,c,c++']
s.rsplit(',',2)
['java,python,javascript', 'c', 'c++']
g='sdfgh'
g='sdfgh'
l=['java','python','javascript','c++']
''.join(1)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    ''.join(1)
TypeError: can only join an iterable
'_'.join(1)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    '_'.join(1)
TypeError: can only join an iterable
'-'.join(1)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    '-'.join(1)
TypeError: can only join an iterable
' '.join(1)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    ' '.join(1)
TypeError: can only join an iterable
