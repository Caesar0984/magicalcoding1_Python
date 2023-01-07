'''
#1

#풀이 1
a = set(input())
b = set(input())

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))

#풀이 2
a = set(input())
b = set(input())

print(a | b)
print(a & b)
print(a - b)
print(a ^ b)

#2

#풀이 1
a, b = map(int, input().split())
x, y = [0], [0]

for i in range(1, a + 1):
    if a % i == 0:
        x.append(i)

for i in range(1, b + 1):
    if b % i == 0:
        y.append(i)

s1 = set(x[1:])
s2 = set(y[1:])

print(sum(s1.intersection(s2)))

#풀이 2
a, b = map(int, input().split())
x, y = set(), set()

for i in range(1, a + 1):
    if a % i == 0:
        x.add(i)

for i in range(1, b + 1):
    if b % i == 0:
        y.add(i)

print(sum(x & y))

#1049 사칙연산
a = int(input())
c1 = input()
b = int(input())
c2 = input()
c = int(input())
res = 0

if c1 == '+':
    res += (a + b)
elif c1 == '-':
    res += (a - b)
elif c1 == '*':
    res += (a * b)
elif c1 == '/':
    res += (a // b)

if c2 == '+':
    res += c
elif c2 == '-':
    res -= c
elif c2 == '*':
    res *= c
elif c2 == '/':
    res //= c

print(res)
'''

#2035 장거리 달리기
m, t, u, f, d = map(int, input().split())
s = 0
a = [0]

for _ in range(t):
    a.append(input())

for i in range(1, t + 1):
    if a[i] == 'u' or a[i] == 'd':
        s += (u + d)
    else:
        s += (f * 2)
    if s > m:
        break

print(i - 1)