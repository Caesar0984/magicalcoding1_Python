'''
#에라토스테네스의 체 알고리즘
check = [0] * 101

for i in range(2, 101):
    if check[i] == 0:
        print(i, end = ' ')
        for j in range(i * i, 101, i):
            check[j] = 1

#이미 구해진 소수로 소수 구하기
import math

a = [0]

for i in range(2, 1001):
    isPrime = True
    for x in a[1:]:
        if x < int(math.sqrt(i)):
            break
        if i % x == 0:
            isPrime = False
            break
    if isPrime:
        a.append(i)

for x in a[1:]:
    print(x, end = ' ')
'''
    
#1
a = [0] * 101
cnt = 0

for i in range(2, 101):
    if a[i] == 0:
        print(i, end = ' ')
        cnt += 1
        if cnt % 5 == 0:
            print()
        for j in range(i * i, 101, i):
            a[j] = 1

#2

#풀이 1
a = [0] * 101
b = [0]

for i in range(2, 101):
    if a[i] == 0:
        b.append(i)
        for j in range(i * i, 101, i):
            a[j] = 1

for x in b[1:]:
    if x in b[1:] and x + 2 in b[1:]:
        print(x, x + 2)

#풀이 2
a = [0] * 101
cnt = 0

for i in range(2, 101):
    if a[i] == 0:
        for j in range(i * i, 101, i):
            a[j] = 1

for i in range(2, 99):
    if a[i] == 0 and a[i + 2] == 0:
        print(i, i + 2)

#1006 숙제를 안 해온 사람은 누구

'''
#풀이 1
a = [0]

for _ in range(28):
    x = int(input())
    a.append(x)

for i in range(1, 30):
    if i not in a[1:]:
        print(i)

#풀이 2
a = [0] * 31

for _ in range(28):
    x = int(input())
    a[x] = 1

for i in range(1, 31):
    if a[i] == 0:
        print(i)
'''

'''
#1038 나머지
a = [0] * 42

for _ in range(10):
    x = int(input())
    a[x % 42] = 1

print(sum(a))
'''
     
#1044 꽃 축제

#풀이 1
s, n = map(int, input().split())
f = [0] * s 
cnt = 0

for _ in range(n):
    a, b = map(int, input().split())
    for i in range(a, s + 1, b):
        f[i] = 1

print(f.count(0))

#풀이 2
s, n = map(int, input().split())
f = [0] * (s + 1)

for _ in range(n):
    a, b = map(int, input().split())
    for j in range(a, s + 1, b):
        f[j] = 1

print(s - sum(f[1:]))

'''
#2031 크리스마스 전등 축제 1

#풀이 1
n, m = map(int, input().split())
a = [0] * (n + 1)
cnt = list()

for _ in range(m):
    p, si, ei = map(int, input().split())
    if p == 0:
        for i in range(si, ei + 1):
            if a[i] == 0:
                a[i] = 1
            elif a[i] == 1:
                a[i] = 0
    elif p == 1:
        cnt.append(a[si: ei + 1].count(1))

for x in cnt:
    print(x)   
       
#풀이 2
n, m = map(int, input().split())
a = [0] * (n + 1)

for _ in range(m):
    op, s, e = map(int, input().split())
    if op == 0:
        for j in range(s, e + 1):
            a[j] = 1 - a[j]
    else:
        print(sum(a[s: e + 1]))
 
#1126 가로등

#풀이 1
n = int(input())
m = int(input())
k = int(input())
a = [0] * (n + 1)

for _ in range(m):
    x = int(input())
    if x - k >= 1 and x + k <= n:
        for i in range(x - k, x + k + 1):
            a[i] = 1
    elif x - k < 1 and x + k > n:
        for i in range(1, n + 1):
            a[i] = 1
    elif x - k < 1 and x + k <= n:
        for i in range(1, x + k + 1):
            a[i] = 1
    elif x - k >= 1 and x + k > n:
        for i in range(x - k, n + 1):
            a[i] = 1

print(a[1:].count(0))

#풀이 2
n = int(input())
m = int(input())
k = int(input())
a = [0] * (n + 1)

for _ in range(m):
    x = int(input())
    for j in range(x - k, x + k + 1):
        if 1 <= j <= n:
            a[j] = 1

cnt = 0
for i in range(1, n + 1):
    if a[i] == 0:
        cnt += 1
        for j in range(i, min(i + k * 2, n) + 1):
            a[j] = 1

print(cnt)

#2079 Trees

#풀이 1
l, m = map(int, input().split())
a = [1] * (l + 1)

for _ in range(m):
    start, end = map(int, input().split())
    for i in range(start, end + 1):
        a[i] = 0

print(sum(a))

#풀이 2
l, m = map(int, input().split())
n = l + 1

for _ in range(m):
    s, e = map(int, input().split())
    n -= (e - s + 1)

print(n)

#2126 주차요금

#풀이 1
a, b, c = map(int, input().split())
t = [0] * 101
x, y, z = 0, 0, 0

for _ in range(3):
    s, e = map(int, input().split())
    for i in range(s, e):
        t[i] += 1

for i in range(1, 101):
    if t[i] == 1:
        x += t[i] * a
    elif t[i] == 2:
        y += t[i] * b
    elif t[i] == 3:
        z += t[i] * c

print(x + y + z)

#풀이 2
a, b, c = map(int, input().split())
t = [0] * 100

for _ in range(3):
    s, e = map(int, input().split())
    for j in range(s, e):
        t[j] += 1

print(a * t.count(1) + b * t.count(2) + c * t.count(3))

#4124 골드바흐의 추측

#풀이 1
n = int(input())
a = [0] * (n + 1)
b = list()
cnt = 0

for i in range(2, n + 1):
    if a[i] == 0:
        b.append(i)
        for j in range(i * i, n + 1, i):
            a[j] = 1

for x in b:
    for y in b:
        if x <= y and x + y == n:
            print(x, y)
            cnt += 1

print(cnt)

#풀이 2
n = int(input())
a = [0] * (n + 1)
b = [0]
cnt = 0

for i in range(2, n + 1):
    if a[i] == 0:
        b.append(i)
        for j in range(i * i, n + 1, i):
            a[j] = 1

for i in range(1, len(b)):
    for j in range(i, len(b)):
        if b[i] + b[j] == n:
            print(b[i], b[j])
            cnt += 1

print(cnt)
'''