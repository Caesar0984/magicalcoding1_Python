#1
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end = '')
    print()

#2
for i in range(1, 6):
    for j in range(1, 7 - i):
        print(j, end = '')
    print()

#3
for i in range(1, 6):
    print(' ' * (5 - i), end = '')
    for j in range(6 - i, 6):
        print(j, end = '')
    print()
    
#4
for i in range(1, 6):
    print(' ' * (i - 1), end = '')
    for j in range(i, 6):
        print(j, end = '')
    print()

#5
for i in range(1, 6):
    print(' ' * (5 - i), end = '')
    for j in range(1, 2 * i):
        print(j, end = '')
    print()

#6
for i in range(1, 6):
    print(' ' * (i - 1), end = '')
    for j in range(1, 12 - 2 * i):
        print(j, end = '')
    print()

#7
for i in range(1, 6):
    print(' ' * (5 - i), end = '')
    for j in range(11 - 2 * i, 10):
        print(j, end = '')
    print()

#8
for i in range(1, 6):
    print(' ' * (i - 1), end = '')
    for j in range(2 * i - 1, 10):
        print(j, end = '')
    print()

#9
for i in range(1, 6):
    print('%s' %chr(64 + i))

#10 
for i in range(1, 6):
    print(' ' * (5 - i), end = '')
    print('%s' %chr(64 + i) * (2 * i - 1))

#11
for i in range(1, 6):
    for j in range(65, 65 + i):
        print('%s' %chr(j), end = '')
    print()

#12
for i in range(1, 6):
    print(' ' * (5 - i), end = '')
    for j in range(64 + i, 63 + 3 * i):
        print('%s' %chr(j), end = '')
    print()
    