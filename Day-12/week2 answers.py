'''
salary=int(input())
bonus=0
if salary>=70000:
    bonus = salary * 0.2
elif salary >= 50000:
    bonus = salary * 0.15
elif salary >=30000:
    bonus = salary * 0.1
else:
    bonus = salary * 0.05
print("Bonus:",bonus)
'''
'''
tup = tuple(input("Tuple : ").split())
pro = input("product: ")
pri =int(input("Price: "))
s =set(map(int,input("Set Values : ").split()))
print("Tuple:",tup)
d={}
d[pro]=pri
print("Dictionary: ",d)
print("Set:",s)
'''
