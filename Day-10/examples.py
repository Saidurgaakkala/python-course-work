Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
d={}
d=dict()
type(d)
<class 'dict'>
d={'k1':'v1','k2':'v2'}
d
{'k1': 'v1', 'k2': 'v2'}
d={}
d[1]='int'
d
{1: 'int'}
d[12.3]='float'
d
{1: 'int', 12.3: 'float'}
d['demo']='str'
d
{1: 'int', 12.3: 'float', 'demo': 'str'}
d[2+3j]='complex'
d
{1: 'int', 12.3: 'float', 'demo': 'str', (2+3j): 'complex'}
d[false]='bool'
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    d[false]='bool'
NameError: name 'false' is not defined. Did you mean: 'False'?
d
{1: 'int', 12.3: 'float', 'demo': 'str', (2+3j): 'complex'}
d={}
d[1]=1
d
{1: 1}
d
{1: 1}
d[23]=23.4
d[3]='fdghjk'
d[4]=3+4j
d[5]=[1,2,3]
d[6]={1,2,3]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
d[6]=(1,2,3)
d[7]={1,3}
d[8]={1:1,2:2}
d[9]=False
d
{1: 1, 23: 23.4, 3: 'fdghjk', 4: (3+4j), 5: [1, 2, 3], 6: (1, 2, 3), 7: {1, 3}, 8: {1: 1, 2: 2}, 9: False}
d={}
d
{}
d[1]=2
d[2]=2
d[3]=2
d[4]=2
d
{1: 2, 2: 2, 3: 2, 4: 2}
d
{1: 2, 2: 2, 3: 2, 4: 2}
d[3]
2
d={1:2,2:4,3:6,4:8,5:10,6:12}
d[4]
8
d[6]
12
d[1]
2
d[4]
8
d={'saidurga':89,'rishi':76,'surya':90,'nagendra':76,'subbu':50}
d
{'saidurga': 89, 'rishi': 76, 'surya': 90, 'nagendra': 76, 'subbu': 50}
d['saidurga']
89
d['surya']
90
d['rishi']
76
d.get('surya')
90
d.get('amar','user not found')
'user not found'
'kumar' ind
SyntaxError: invalid syntax
'kumar' in d
False
'surya' in d
True
'karthi' not in d
True
d.keys()
dict_keys(['saidurga', 'rishi', 'surya', 'nagendra', 'subbu'])
d.values()
dict_values([89, 76, 90, 76, 50])
d.items()
dict_items([('saidurga', 89), ('rishi', 76), ('surya', 90), ('nagendra', 76), ('subbu', 50)])
sorted(d)
['nagendra', 'rishi', 'saidurga', 'subbu', 'surya']
max(d)
'surya'
min(d)
'nagendra'
len(5)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    len(5)
TypeError: object of type 'int' has no len()
lend(d)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    lend(d)
NameError: name 'lend' is not defined. Did you mean: 'len'?
>>> len(d)
5
>>> d['surya']
90
>>> d['surya']=100
>>> d
{'saidurga': 89, 'rishi': 76, 'surya': 100, 'nagendra': 76, 'subbu': 50}
>>> d['saidurga']=70
>>> d
{'saidurga': 70, 'rishi': 76, 'surya': 100, 'nagendra': 76, 'subbu': 50}
>>> d
{'saidurga': 70, 'rishi': 76, 'surya': 100, 'nagendra': 76, 'subbu': 50}
>>> d['rishi']=87
>>> d
{'saidurga': 70, 'rishi': 87, 'surya': 100, 'nagendra': 76, 'subbu': 50}
>>> d.update({'kumar':90,'dilip':78})
>>> d
{'saidurga': 70, 'rishi': 87, 'surya': 100, 'nagendra': 76, 'subbu': 50, 'kumar': 90, 'dilip': 78}
>>> d.popitem()
('dilip', 78)
>>> d
{'saidurga': 70, 'rishi': 87, 'surya': 100, 'nagendra': 76, 'subbu': 50, 'kumar': 90}
>>> d.clear()
>>> d
{}
>>> d
{}
>>> d={'saidurga': 89, 'rishi': 76, 'surya': 100, 'nagendra': 76, 'subbu': 50}
... d
SyntaxError: multiple statements found while compiling a single statement
>>> d={'saidurga':100,'surya':100}
>>> d
{'saidurga': 100, 'surya': 100}
>>> d.setdefault('satish',0)
0
