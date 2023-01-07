'''
#1 
a = list()

for i in range(11):
    a.append(i)

a[1:] = a[2:] + a[1:2]

print(a[1:])

#2
a = list()

for i in range(11):
    a.append(i)

a[1:] = a[10:11] + a[1:10]

print(a)

#3

#풀이 1
pn = list()
pcnt = 0

for i in range(1, 51):
    cnt = 0
    for j in range(1, i + 1):
        if i % j == 0:
            cnt += 1
    if cnt == 2:
        pn.append(i)
        pcnt += 1

for i in range(0, pcnt):
    print(pn[i])
    
#풀이 2
import math

pn = list()

for i in range(1, 51):
    cnt = 0
    k = int(math.sqrt(i))
    for j in range(2, k + 1):
        if i % j == 0:
            cnt += 1
    if cnt == 0:
        pn.append(i)

for i in pn[1:]:
    print(i)   

#4 
d = input()

print(d[:4] + 'Y', d[4:6] + 'M', d[6:] + 'D')
'''

'''
#1115 다음 라운드
n, k = map(int, input().split())
p = [0]
p[1:] = list(map(int, input().split()))
pcnt = 0

for x in p[1:]:
    if x > 0 and p[k] <= x:
        pcnt += 1

print(pcnt)    

#1117 데이터 박스

#풀이 1
x = int(input())
n = int(input())
c = c[0]

cnt = 0
s = 0

while cnt < n:
    a = int(input())
    c.append(x - a)
    cnt += 1    

s = sum(c)

print(s + x)

#풀이 2
x = int(input())
n = int(input())
a = [0]

for _ in range(n):
    a.append(int(input()))

s = 0

for val in a[1:]:
    s += (x - val)

print(s + x)
'''

#2010 블록 쌓기

#풀이 1
n = int(input())
x = [0]
x[1:] = list(map(int, input().split()))
a = int(sum(x) / n)
res = 0

for i in x[1:]:
    if a > i:
        res += (a - i)

print(res)    

#풀이 2
n = int(input())
a = [0]
a[1:] = list(map(int, input().split()))
s = sum(a)

ave, res =  s // n, 0

for x in a[1:]:
    if ave < x:
        res += (x - ave)

print(res)

#2137 평균 수열

#풀이 1
n = int(input())
k = list()
b = list(map(int, input().split()))

for i in range(0, len(b)):
    k.append(b[i] * (i + 1))
    if i > 0:
        print(k[i] - k[i - 1])
    else:
        print(k[i])

#풀이 2
n = int(input())
a = list(map(int, input().split()))
s = 0

for i in range(0, n):
    x = (a[i] * i) - s
    print(x, end = ' ')
    s += x

#1121 참치
n = int(input())
x = int(input())
s = 0

for _ in range(n):
    p1, p2 = map(int, input().split())
    if p1 <= p2 and x == p2 - p1:
        s += p2
    elif p2 < p1 and x == p1 - p2:
        s += p1
    else:
        p3 = int(input())
        s += p3

print(s)

#1084 Doubles

#풀이 1
x = list(map(int, input().split()))
cnt = 0

for i in x[:]:
    if i != 0 and i * 2 in x:
        cnt += 1

print(cnt)

#풀이 2
a = list(map(int, input().split()))
a[:] = a[:-1]
cnt = 0

for i in a[:]:
    for j in a[:]:
        if i * 2 == j:
            cnt += 1

print(cnt)

'''
#1104 토끼 사냥
p, q = map(int, input().split())
a = list()
b = list()

for i in range(1, p + 1):
    if p % i == 0:
        a.append(i)

for i in range(1, q + 1):
    if q % i == 0:
        b.append(i)
    
for i in a[:]:
    for j in b[:]:
        print(i, j)        

#2022 왕국 곱셈
a, b = input().split()
s = 0

for i in range(0, len(a)):
    for j in range(0, len(b)):
        s += (int(a[i]) * int(b[j]))

print(s)
'''

