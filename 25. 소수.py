'''
#제곱근을 이용한 소수 판별
import math

for i in range(2, 100):
    cnt = 0
    k = int(math.sqrt(i))
    for j in range(2, k + 1):
        if i % j == 0:
            cnt += 1
    if cnt == 0:
        print(i)
    
#1
a, b = map(int, input().split())
n = 0

for i in range(a, b + 1):
    cnt = 0
    for j in range(1, i + 1):
        if i % j == 0:
            cnt += 1
    if cnt == 2:
        print(i, end = ' ')
        n += 1
        if n % 5 == 0:
            print()    

#1140 소수 찾기

#1
a, b, k = map(int, input().split())
t = 0
p = list()
pcnt = 0

for i in range(a, b + 1):
    cnt = 0
    for j in range(1, i + 1):
        if i % j == 0:
            cnt += 1
    if cnt == 2:
        t += i
        p.append(i)
        pcnt += 1

if pcnt >= k:
    print(t)
    print(p[k - 1])
else:
    print(t)
    print(-1)  
    
#2
a, b, k = map(int, input().split())
pcnt, s, kth = 0, 0, -1

for i in range(a, b + 1):
    cnt = 0
    for j in range(1, i + 1):
        if i % j == 0:
            cnt += 1
    if cnt == 2:
        s += i
        pcnt += 1
        if pcnt == k:
            kth = i

print(s)
print(kth) 
'''

#1141 쌍둥이 소수
n = int(input())
p = list()
pcnt = 0
tpcnt = 0

for i in range(1, n + 1):
    cnt = 0
    for j in range(1, i + 1):
        if i % j == 0:
            cnt += 1
    if cnt == 2:
        p.append(i)
        pcnt += 1

for i in range(0, pcnt):
    if p[i] + 2 in p:
        print(p[i], p[i] + 2)
        tpcnt += 1

print(tpcnt)

#2
n = int(input())
twincnt = 0

for i in range(2, n - 1):
    cnt = 0
    for j in range(1, i + 1):
        if i % j == 0:
            cnt += 1
    if cnt == 2:
        cnt = 0
        for j in range(1, i + 3):
            if (i + 2) % j == 0:
                cnt += 1
        if cnt == 2:
            print(i, i + 2)
            twincnt += 1

print(twincnt)

#3
import math

n = int(input())
twincnt = 0

for i in range(2, n - 1):
    cnt = 0
    k = int(math.sqrt(i))
    for j in range(2, k + 1):
        if i % j == 0:
            cnt += 1
    if cnt == 0:
        k = int(math.sqrt(i + 2))
    for j in range(2, k + 1):
        if (i + 2) % j == 0:
            cnt += 1
    if cnt == 0:
        print(i, i + 2)
        twincnt += 1

print(twincnt)

#1142 메르센 소수

#1
n = int(input())
p = list()
pcnt = 0
t = 0

for i in range(1, n + 1):
    cnt = 0
    for j in range(1, i + 1):
        if i % j == 0:
            cnt += 1
    if cnt == 2:
        p.append(i)
        pcnt += 1

for i in range(0, pcnt):
    if i in p and (2 ** i - 1) in p:
        print(2 ** i - 1)

#2
n = int(input())
i = 2

while (2 ** i - 1) <= n:
    cnt = 0
    for j in range(1, i + 1):
        if i % j == 0:
            cnt += 1
    if cnt == 2:
        cnt = 0
        mp = 2 ** i - 1
        for j in range(1, mp + 1):
            cnt += 1
        if cnt == 2:
            print(mp)
    i += 1

#3
import math

n = int(input())
i = 2

while(2 ** i - 1) <= n:
    cnt = 0
    k = int(math.sqrt(i))
    for j in range(2, k + 1):
        if i % j == 0:
            cnt += 1
    if cnt == 0:
        mp = 2 ** i - 1
        k = int(math.sqrt(mp))
        for j in range(2, k + 1):
            if mp % j == 0:
                cnt += 1
        if cnt == 0:
            print(mp)
    i += 1