#피보나치 수열 알고리즘
a = [0, 1]

for i in range(2, 13):
    a.append(a[i - 1] + a[i - 2])

print(a[1:])

#1
n = int(input())
a = [0, 1]

for i in range(2, n + 1):
    a.append(a[i - 1] + a[i - 2])

print(a[n])


#1017 금화
n = int(input())
g = [0, 1, 1]

for i in range(3, n + 1):
    if i % 2 != 0:
        g.append(g[i // 2] + g[i // 2 + 1])
    else:
        g.append(g[i // 2])

print(max(g[1:]))

'''
#1072 Speed Limit

#풀이 1
n = int(input())
s = [0]
t = [0]
res = 0

for _ in range(1, n + 1):
    x, y = map(int, input().split())
    s.append(x)
    t.append(y)

t[1:] = sorted(t[1:])

for i in range(1, n + 1):
    res += (s[i] * (t[i] - t[i - 1]))

print(res)

#풀이 2
n = int(input())
s, r = [0] * (n + 1), [0] * (n + 1)
res = 0

for i in range(1, n + 1):
    s[i], t[i] = map(int, input().split())
    res += (s[i] * (t[i] - t[i - 1]))

print(res) 
'''