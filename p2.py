Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

======================= RESTART: D:/python_practice/p1.py ======================
Traceback (most recent call last):
  File "D:/python_practice/p1.py", line 3, in <module>
    d={i:i*i for i in 2}
TypeError: 'int' object is not iterable

======================= RESTART: D:/python_practice/p1.py ======================
{1: 1, 2: 4, 3: 9, 4: 16}

======================= RESTART: D:/python_practice/p1.py ======================
{1: 1, 2: 4, 3: 9, 4: 16}
num = [10, 20, 30, 40]
len(num) 
max(num) 
min(num) 
sum(num)
sorted(num)
list(reversed(num))

SyntaxError: multiple statements found while compiling a single statement
num =[10, 20, 30, 40]
len(num)
4
max(num)
40
min(num)
10
sum(num)
100
sorted(num)
[10, 20, 30, 40]
list(reversed(num))
[40, 30, 20, 10]
l=[1, 2, 3, 4, 2]
l.append(5)
print(l)
[1, 2, 3, 4, 2, 5]
l.insert(3)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    l.insert(3)
TypeError: insert expected 2 arguments, got 1
l=[1, 2, 3, 4, 2]
l.insert(3)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    l.insert(3)
TypeError: insert expected 2 arguments, got 1
>>> l.insert(3,2)
>>> l
[1, 2, 3, 2, 4, 2]
>>> l.extend([6, 7])
>>> l
[1, 2, 3, 2, 4, 2, 6, 7]
>>> l.remove(2)
>>> l
[1, 3, 2, 4, 2, 6, 7]
>>> l.pop()
7
>>> l.pop(3)
4
>>> l.clear()
>>> l
[]
>>> l=[1, 2, 3, 2, 4]
>>> l.index(2)
1
>>> l.count(2)
2
>>> l=[6,3,1,2,8]
>>> l.sort()
>>> l
[1, 2, 3, 6, 8]
>>> l.sort(reverse=True)
>>> l
[8, 6, 3, 2, 1]
>>> l.reverse()
>>> l
[1, 2, 3, 6, 8]
>>> l= [1, 2, 3]
>>> copy_l=l.copy()
>>> l
[1, 2, 3]
