'''
#최댓값 & 최솟값 알고리즘
a = [0, 33, 67, 23, 87, 95]

maxv = minv = a[1]

for x in a[2:]:
    maxv = max(maxv, x)
    minv = min(minv, x)

print(maxv)
print(minv)

print(max(a[1:]))
print(min(a[1:]))

#최빈값 알고리즘
a = [0, 1, 2, 2, 2, 10]
b = [0] * (max(a) + 1)

for x in a[1:]:
    b[x] += 1
    
maxv = max(b[1:])
idx = b.index(maxv)
print(idx)

#1

#풀이 1
a = [7, -5, 4, -99, 45, 11, 0, 8, 50, 77]
maxv, minv, s = 0, 0, 0

for i in a:
    if maxv <= i:
        maxv = i
    if minv >= i:
        minv = i
    s += i

print(maxv)
print(minv)
print(s)

#풀이 2
a = [7, -5, 4, -99, 45, 11, 0, 8, 50, 77]

print(max(a))
print(min(a))
print(sum(a))

#1023 최댓값과 최솟값
n = int(input())
a = list(map(int, input().split()))

print(max(a))
print(min(a))

#1137 가장 큰 수 

#풀이 1
cnt = 0
a = list()

while cnt < 9:
    x = int(input())
    a.append(x)
    cnt += 1

print(max(a))
print(a.index(max(a)) + 1)

#풀이 2
a = [0]

for _ in range(9):
    a.append(int(input()))

maxv, idx = a[1], 1

for i in range(1, 10):
    if maxv < a[i]:
        maxv, idx = a[i], i

print(maxv)
print(idx)

#풀이 3
a = [0]
idx = 1

for _ in range(9):
    a.append(int(input()))
    
for i in range(1, 10):
    if a[idx] < a[i]:
        idx = i

print(a[idx])
print(idx)

#풀이 4
a = [0]

for _ in range(9):
    a.append(int(input()))

maxv = max(a[1:])
idx = a.index(maxv)

print(maxv)
print(idx)

#1068 최고의 저녁 식사

#풀이 1
cnt = 0
p = list()
res = list()

while cnt < 5:
    x = list(map(int, input().split()))
    p.append(x)
    cnt += 1

for i in range(0, 5):
    res.append(sum(p[i]))

print(res.index(max(res)) + 1, max(res))

#풀이 2
maxv = 0

for i in range(1, 6):
    s1, s2, s3, s4 = map(int, input().split())
    if maxv < (s1 + s2 + s3 + s4):
        maxv, idx = (s1 + s2 + s3 + s4), i

print(idx, maxv)

#1086 iRobot 

#풀이 1
n = int(input())
a = list(map(int, input().split()))
res = list()

m = int(input())
cnt = 0

while cnt < m:
    b = list()
    c = list(map(int, input().split()))
    for i in range(c[1], c[2] + 1):
        b.append(a[i - 1])
    if c[0] == 1:
        res.append(min(b))
    elif c[0] == 2:
        res.append(max(b))
    elif c[0] == 3:
        res.append(sum(b))
    cnt += 1

for i in res[:]:
    print(i)

#풀이 2
n = int(input())
a = [0]
a[1:] = list(map(int, input().split()))
m = int(input())

for _ in range(m):
    order, x, y = map(int, input().split())
    if order == 1:
        print(min(a[x:y + 1]))
    elif order == 2:
        print(max(a[x:y + 1]))
    else:
        print(sum(a[x:y + 1]))
'''

'''     
#1045 유행 
n = int(input())
b = [0] * 10000
        
for _ in range(n):
    x = int(input())
    b[x] += 1

maxv = max(b)
idx = b.index(maxv)

print(idx)
'''

'''
#1061 슈퍼마리오 
a = list()
s = 0

for _ in range(0, 10):
    a.append(int(input()))

for x in a:
    s += x
    if s <= 100:
        res = s
    else:
        if 100 - res >= s - 100:
            res = s
        break

print(res)

#1082 The King
n = int(input())
p = int(input())
iq = list(map(int, input().split()))
s = 0

for x in iq:
    if x ** p >= 0:
        s += (x ** p)

print(s)
'''

#1123 블랙잭 
b = [0] * 2 + [4] * 8 + [16] + [4]
n = int(input())
s = 0

for _ in range(n):
    a = int(input())
    s += a
    b[a] -= 1

x, c1, c2 = 21 - s, 0, 0

for i in range(2, 12):
    if x < i:
        c1 += b[i]
    else:
        c2 += b[i]

if c1 > c2:
    print("STOP")
else:
    print("DRAW")

#2093 주차하기 가장 좋은 곳 
#걸어야 하는 거리는 (p - x) * 2 + (y - p) * 2 = (y - x) * 2
n = int(input())
i = [0]
i[1:] = list(map(int, input().split()))

x = min(i[1:])
y = max(i[1:])

print((y - x) * 2)

#2089 주사위 게임

#풀이 1
s = list(map(int, input().split()))
res = list()

for i in range(1, s[0] + 1):
    for j in range(1, s[1] + 1):
        for k in range(1, s[2] + 1):
            res.append(i + j + k)

fin = [0] * 100000

for x in res:
    fin[x] += 1

print(max(fin))

#풀이 2
s1, s2, s3 = map(int, input().split())
b = [0] * (s1 + s2 + s3 + 1)

for i in range(1, s1 + 1):
    for j in range(1, s2 + 1):
        for k in range(1, s3 + 1):
            b[i + j + k] += 1

maxv = max(b[1:])
idx = b.index(maxv)
print(idx)