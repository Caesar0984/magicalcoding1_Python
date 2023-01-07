#숫자 뒤집기
k, r = 123, 0

while k != 0:
    r = r * 10 + k % 10
    k //= 10

print(r)

#1
n = int(input())
k = n
r = 0

while n != 0:
    r = r * 10 + n % 10
    n //= 10

if k == r:
    print('Palindrome Number')
else:
    print('Normal Number')

#2
a, b = map(int, input().split())
s = 0

for i in range(a, b + 1):
    if i % 10 == 7:
        s += i
    else:
        continue

print(s)

#3
a, b = map(int, input().split())
s = 0

for i in range(a, b + 1):
    if (i % 100) // 10 == 7:
        s += i
    else:
        continue

print(s)

#1043 숫자 뒤집기
a, b = map(int, input().split())
r1, r2 = 0, 0

while a != 0:
    r1 = r1 * 10 + a % 10
    a //= 10

while b != 0:
    r2 = r2 * 10 + b % 10
    b //= 10

if r1 >= r2:
    print(r1)
else:
    print(r2)

#수의 덧셈
x = int(input())
y = x
r = 0

while x != 0:
    r = r * 10 + x % 10
    x //= 10

print(r + y)

#1136 팔린드롬 수
a, b = map(int, input().split())
cnt = 0

for i in range(a, b + 1):
    r = 0
    x = i
    while i != 0:
        r = r * 10 + i % 10
        i //= 10
    if x == r:
        cnt += 1

print(cnt)