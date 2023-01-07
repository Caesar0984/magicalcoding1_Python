'''
#1000 A+B Problem
A = int(input("Enter a number between 0 and 10:"))
B = int(input("Enter a number between 0 and 10:"))

if 0 <= A <= 10 and 0 <= B <= 10:
    print(A + B, '\n')
else:
    print("Error\n")

#1002 구구단
N = int(input("Enter a number between 2 and 100:"))

for i in range(1, 10):
    print(N, '*', i, '=', N * i)

#1012 R2
R1, S = map(int, input().split())

R2 = (S * 2) - R1

print(R2)

#1001 작거나 크거나
x, y  = map(int, input('Enter two numbers:').split())

if x > y:
    print('>')
elif x < y:
    print('<')
else:
    print('=')

#1037 점수
x, y, z, w = map(int, input("Enter scores for Euler:").split())
S = x + y + z + w

a, b, c, d = map(int, input('Enter scores for Euclid:').split())
T = a + b + c + d

if S >= T:
    print(S)
else:
    print(T)

#1005 숫자 계산 1
n = int(input())
sum = 0

for i in range(101):
    sum += (n * i)

print(sum)

#1006 숫자 계산 2
n = int(input())
sum = 0

for i in range(n + 1):
    sum += (i**2)

print(sum)

#1007 숫자 계산 3
n = int(input())
sum = 0

for i in range(1, n + 1):
    sum += (i * (n - i + 1))

print(sum)
'''

'''
#1003 홀수와 짝수의 합
x = int(input())
even = list()
odd = list()

for i in range(1, x + 1):
    if i % 2 != 0:
        odd.append(i)
    else:
        even.append(i)

print(sum(even))
print(sum(odd))

#1013 오일러 프로젝트
#1
n = int(input())
three = list()
five = list()

for i in range(1, n):
    if i % 3 == 0:
        three.append(i)
    elif i % 5 == 0:
        five.append(i)
    else:
        continue

print(sum(three) + sum(five))

#2
N = int(input())
s = 0

for i in range(1, n):
    if i % 3 == 0:
        s += i
    elif i % 5 == 0:
        s += i
    else:
        continue

print(s)

#1011 잠자기 전에 독서 1
x = int(input())
s = 0

for i in range(1, x + 1):
    if x % i == 0:
        s += i
    else:
        continue

print(s)

#1134 두 개의 짝수
x = int(input())
cnt = 0

for i in range(1, x + 1):
    if i % 4 == 0:
        cnt += 1
    else:
        continue

print(cnt)    
        
#1014 수학 숙제
n = int(input())
m = 1

for i in range(1, n + 1):
    m *= i
    
print(m)

#1098 약수
n = int(input())
s = 0

for i in range(1, n):
    if n % i == 0:
        s += i
    else: continue
    
print(s)


#1008 팩토리얼
n = int(input())
m = 1

print(n, '!=(', 1, sep = '', end = '')

for i in range(2, n + 1):
    m *= i
    print('*', i, sep = '', end = '')
    
print(')=', m, sep = '')

#1018 골동품
#1
a, b, c, d = map(int, input().split())

while True:
    if a >= c:
        print(a)
        break
    else:
        a += b
        c -= d

#2
a, b, c, d = map(int, input().split())

while a > c:
    a += b
    c -= d

print(a)
'''

#1009 홀수의 합
a = int(input())
b = int(input())
s = 0

for i in range(a, b + 1):
    if i % 2 == 1:
        s += i

print(s)

