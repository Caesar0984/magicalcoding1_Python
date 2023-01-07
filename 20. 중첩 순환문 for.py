#1
for i in range(1, 6):
    print('#' * i)

#2
for i in range(5, 0, -1):
    print('#' * i)
    
#3 
for i in range(1, 6):
    print(' ' * (5 - i), end = '')
    print('#' * i)
    
#4 
for i in range(1, 6):
    print(' ' * (i - 1), end = '')
    print('#' * (6 - i))

#5
for i in range(1, 6):
    print(' ' * (5 - i), end ='')
    print('#' * ((2 * i) - 1))
    
#6
for i in range(1, 6):
    print(' ' * (i - 1), end = '')
    print('#' * (2 * (6 - i) - 1))