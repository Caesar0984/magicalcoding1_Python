#누적합 알고리즘
a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
s = [0]
start, end = 5, 9

for i in range(1, 11):
    s.append(s[i - 1] + a[i])

print(s[end] - s[start - 1])

'''
#1

#풀이 1
a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
t = int(input())
res = [0]

for _ in range(t):
    start, end = map(int, input().split())
    s = 0
    for i in range(start, end + 1):
        s += a[i]
    res.append(s)

for x in res[1:]:
    print(x)

#풀이 2
a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
s = [0]
t = int(input())

for i in range(1, 11):
    s.append(s[i - 1] + a[i])

for _ in range(t):
    start, end = map(int, input().split())
    print(s[end] - s[start - 1])

#2025 식량 공급
n, q = map(int, input().split())
a = [0]
b = [0]

for _ in range(n):
    h = int(input())
    a.append(h)

for _ in range(q):
    t = 0
    s, e = map(int, input().split())
    for i in range(s, e + 1):
        t += a[i]
    b.append(t)

for x in b[1:]:
    print(x)

#풀이 2
n, q = map(int, input().split())
s = [0]

for i in range(1, n + 1):
    x = int(input())
    s.append(s[i - 1] + x)

for _ in range(q):
    start, end = map(int, input().split())
    print(s[end] - s[start - 1])
'''

#2109 The Largest Sum

#풀이 1
n, k = map(int, input().split())
a = [0]
res = [0]

for _ in range(n):
    x = int(input())
    a.append(x)

for i in range(1, n - k + 2):
    s = 0
    for j in range(i, i + k):
        s += a[j]
    res.append(s)

print(max(res[1:]))

#풀이 2
n, k = map(int, input().split())
s = [0]

for i in range(1, n + 1):
    x = int(input())
    s.append(s[i - 1] + x)

maxv = s[k]

for i in range(1, n - k + 2):
    maxv = max(maxv, s[i + k - 1] - s[i - 1])

print(maxv)