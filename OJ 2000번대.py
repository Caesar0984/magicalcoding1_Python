'''
#2004 이지팬갈비
n, k = map(int, input().split())

if n <= k:
    print(2)
elif (n * 2) % k == 0:
    print((n * 2) // k)
else:
    print((n * 2) // k + 1)

#2013 도미노 게임
#1
n = int(input())
s = 0
m = 1

for i in range(0, n + 1):
    s += (i + 1)
    
m = s * n

print(m)

#2
x = int(input())
s = 0

for i in range(n + 1):
    for j in range(i + 1):
        s += (i + j)

print(s)
'''
'''
#2000 세 수의 합
z = int(input("3 이상 30 이하의 자연수를 입력하시오:"))
cnt = 0

for i in range(1, 11):
    for j in range(i + 1, 11):
        for k in range(j + 1, 11):
            if i + j + k == z:
                print(i, j, k)
                cnt += 1       

print(cnt)
       

#2001 추의 합
g = int(input("1 이상 50 이하의 자연수를 입력하시오:"))
cnt = 0

for i in range(1, 11):
    for j in range(1, 11):
        for k in range(1, 11):
            if 2 * i + 3 * j + 5 * k == g:
                print(i, j, k)
                cnt += 1       

print(cnt)

#2007 나비
n = int(input())

#상단
for i in range(1, n):
    for j in range(1, i + 1):
        print(j, end = '')
    print(' ' * ((n - 1) * 2 - (i * 2 - 1)), end = '') 
    for j in range(i, 0 , -1):
        print(j, end = '')
    print()

#허리
for i in range(1, n + 1):
    print(i % 10, end ='')
for i in range(n - 1, 0 , -1):
    print(i, end = '')
print()

#하단
for i in range(n - 1, 0, -1):
    for j in range(1, i + 1):
        print(j, end = '')
    print(' ' * ((n - 1) * 2 - (i * 2 - 1)), end = '')
    for j in range(i, 0, -1):
        print(j, end = '')
    print()
'''

'''
#2016 콜라
#1
k, n = map(int, input().split())
b = k // n

while True:
    if k >= n:
        if b >= n:
            k += (b + (b // n))
            print(k)
            break
        else:
            print(k + b)
            break         
    else:
        print(k)
        break 

#2
n, k = map(int, input().split())
s = n

while n >= k:
    s += (n // k)
    n = (n // k) + (n % k)

print(s)
        
#2085 Gold Coin
n = int(input())
s, day, gold = 0, 0, 0

while n > day:
    gold += 1
    day += gold
    s += gold ** 2

s += (n - day) * gold

print(s)
'''