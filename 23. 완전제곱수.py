import math

#약수의 개수를 이용한 완전제곱수 판별
for i in range(1, 101):
    cnt = 0    #각각의 i를 판별할 때마다 계속 초기화 시켜야함
    for j in range(1, i + 1):   #각각의 i에 대한 약수의 개수 구하기
        if i % j == 0:
            cnt += 1
    if cnt % 2 == 1:    #약수의 개수가 홀수개이면 완전제곱수
        print(i)

#제곱근을 이용한 완전제곱수 판별
for i in range(1, 101):
    k = int(math.sqrt(i))
    if k ** 2 == i:
        print(i)

#순환문을 이용한 완전제곱수 판별
for i in range(1, 101):
    k = 1
    while k ** 2 < i:
        k += 1
    if k ** 2 == i:
        print(i)

#This also works:
for i in range(1, 101):
    for j in range(1, i + 1):
        if j ** 2 == i:
            print(i)
    
'''
#1 한 변의 길이가 양의 정수인 정사각형의 한 변의 길이 N이 주어지면 한 변의 길이가 양의 정수인 크고 작은 정사각형이 모두 몇 개가 있는지
전체 개수를 구하는 프로그램을 작성하여라.
'''
x = int(input())
cnt = 0

for i in range(1, x + 1):
    cnt += math.pow(i, 2)

print(int(cnt))

#1144 타일의 개수
N = int(input())
s = 0

for i in range(1, N + 1):
    if i != N:
        s += (4 * i - 2)
    else:
        s += (2 * i - 1)

print(s)

#1138 정사각수

#1
a, b = map(int, input().split())
s, m = 0, 0

for i in range(a, b + 1):
    cnt = 0
    for j in range(1, i + 1):
        if i % j == 0:
            cnt += 1
    if cnt % 2 == 1:
        s += i
        m += 1
        if m == 1:
            mv = i

if m == 0:
    print(-1)
else:
    print(s)
    print(mv)
    
#2
import math

a, b = map(int, input().split())
s, m = 0, 0

for i in range(a, b + 1):
    cnt = 0
    k = int(math.sqrt(i))
    if math.pow(k, 2) == i:
        s += i
        m += 1
        if m == 1:
            minv = i 

if m == 0:
    print(-1)
else:
    print(s)
    print(minv)
    
#1143 타일 붙이기

#1
n = int(input())
b, r = 0, 0
k = int(math.sqrt(n))

if int(math.pow(k, 2)) == n: 
    for i in range(1, k + 1):
        if i % 2 == 1:
            b += 2 * i - 1
        else:
            r += 2 * i - 1
    print(abs(b - r))
else: 
    print('Error')

#2
n = int(input())
k = 1
while k ** 2 < n:
    k += 1
print(k)

#3
n = int(input())

print(int(math.sqrt(n)))

#2015 술 취한 교도관

#1
import math

n = int(input())
cnt = 0

for i in range(1, n + 1):
    k = int(math.sqrt(i))
    if int(math.pow(k, 2)) == i:
        cnt += 1

print(cnt)

#2
n = int(input())
res = 0

for i in range(1, n + 1):
    cnt = 0
    for j in range(1, i + 1):
        if i % j == 0:
            cnt += 1
    if cnt % 2 == 1:
        res += 1

print(res)

#2071 완전제곱수

#1
n = int(input())
cnt = 0

for i in range(1, 501):
    for j in range(1, 501):
        if i ** 2 + n == j ** 2:
            cnt += 1

print(cnt)

#2
n = int(input())
res = 0

for i in range(1, 501):
    a = i ** 2 + n
    cnt = 0
    for j in range(1, a + 1):
        if a % j == 0:
            cnt += 1
    if cnt % 2 == 1:
        res += 1

print(res)

#3
import math

n = int(input())
cnt = 0

for i in range(1, 501):
    a = i ** 2 + n
    k = int(math.sqrt(a))
    if k ** 2 == a:
        cnt += 1

print(cnt)

#1004 홀수 제곱과 짝수 제곱
N = int(input())
s = 0

for i in range(1, N + 1):
    if i % 2 == 1:
        s += i ** 2
    else:
        s -= i ** 2

print(s)