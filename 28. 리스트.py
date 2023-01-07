'''
#1019 홀수와 짝수의 개수
n = int(input())
num = list()
ecnt = 0
ocnt = 0

while n > 0:
    x = int(input())
    num.append(x)
    if x % 2 == 0:
        ecnt += 1
    else:
        ocnt += 1
    n -= 1

print(ecnt)
print(ocnt)

#1020 짝수와 홀수
x = int(input())

e = list()
es = 0

o = list()
os = 0

while x > 0:
    n = int(input())
    if n % 2 == 0:
        e.append(n)
    else:
        o.append(n)
    x -= 1

es = sum(e)
os = sum(o)

print(es, os)    
    
#1030 Graphing
n = int(input())
f = list()
fcnt = 0

while n > 0:
    x = int(input())
    f.append(x)
    fcnt += 1
    n -= 1

for i in range(fcnt):
    print(f[i], '*' * f[i])
'''

#1026 Black
a = list(map(int, input().split()))

b = [1, 1, 2, 2, 2, 8]
for i in range(6):
    print(b[i] - a[i], end = ' ')

#1094 파티
l, p = map(int, input().split())
t = l * p

n = list(map(int, input().split()))

for i in range(5):
    print(n[i] - t, end = ' ')

#1139 숫자 슬라이스
a , b, c = map(int, input().split())
x = a * b * c

cnt = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

while x:
    cnt[x % 10] += 1 
    x //= 10
    
for i in range(10):
    print(cnt[i])