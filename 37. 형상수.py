#삼각수 알고리즘
a = [0]

for i in range(1, 6):
    a.append(sum(range(1, i + 1)))

for x in a[1:]:
    print(x)

#사각수 알고리즘
a = [0]

for i in range(1, 6):
    a.append(i * i)

for x in a[1:]:
    print(x)
    
#오각수 알고리즘
a = [0]

for i in range(1, 6):
    a.append((i * i) + sum(range(1, i)))

for x in a[1:]:
    print(x)

'''    
#1
n = int(input())
a = [0]
b = [0]
c = [0]

for i in range(1, n + 1):
    a.append(sum(range(1, i + 1)))

for i in range(1, n + 1):
    b.append(i * i)

for i in range(1, n + 1):
    c.append(i * i + sum(range(1, i)))
    
print(a[n] + b[n] + c[n])

#1147 육각수

#풀이 1
n = int(input())
a = [0]

for i in range(1, n + 1):
    a.append(sum(range(1, 4 * n - 2, 4)))

print(a[n])

#풀이 2
n = int(input())
print(n * (2 * n - 1))

#1073 오각수

#풀이 1
n = int(input())
a = [0] * 15001
res= [0]

for i in range(1, 100):
    for j in range(1, 14951):
        if (i * i + sum(range(1, i))) == j:
            a[j] = 1

for _ in range(n):
    x = int(input())
    res.append(x)

for x in res[1:]:
    if a[x] == 1:
        print(x, 'Y')
    else:
        print(x, 'N')

#풀이 2
n = int(input())
a = [0] * 10001
i = 1

while (i * i) + sum(range(1, i)) <= 10000:
    a[(i * i) + sum(range(1, i))] = 1
    i += 1

for _ in range(n):
    x = int(input())
    if a[x] == 1:
        print(x, 'Y')
    else:
        print(x, 'N')

#1077 곱셈 테이블
n = int(input())

print(' *', end = '')

for i in range(1, n + 1):
    print('%4d' % i, end = '')

print()

for i in range(1, n + 1):
    print('%2d' % i, end = '')
    for j in range(1, n + 1):
        print('%4d' % (i * j), end = ' ')
    print()
'''

#1111 조약돌
n = int(input())
minv = 2 * n + 1

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i * j >= n:
            if minv > i + j or (minv == i + j and r > i):
                minv, r, c = (i + j), i, j

print(r, c)