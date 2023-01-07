'''
#선택 정렬 알고리즘
a = [7, 6, 9, 5, 8]

for i in range(0, 5):
    for j in range(i + 1, 5):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]

print(a)

#1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

a.sort(reverse = True)

print(a)

#1022 정렬(Sorting)
n = int(input())
a = list(map(int, input().split()))
b = sorted(a)

for i in a:
    print(i, end = ' ')
    
print()

for i in b:
    print(i, end = ' ')
    
#1025 세 번째로 가장 큰 값

#풀이 1
n = list(map(int, input().split()))
a = sorted(n)
res = a[len(n) - 3]

print(res)

#풀이 2
n = list(map(int, input().split()))
a = sorted(n, reverse = True) 

print(a[2])   
'''

'''
#1127 마법 지팡이

#풀이 1
n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
z = [0] * (max(y) + 1)
cnt = 0

for i in x:
    for j in y:
        if i <= j:
            z[j] += 1

for i in z:
    if i != 0:
        cnt += 1

if cnt == n:
    print('YES')
else:
    print('NO')

#풀이 2
n = int(input())
a = [0]
b = [0]
a[1:] = list(map(int, input().split()))
b[1:] = list(map(int, input().split()))

a[1:] = sorted(a[1:])
b[1:] = sorted(b[1:])

isOk = True

for i in range(1, n + 1):
    if a[i] > b[i]:
        isOk = False
        break

if isOk:
    print('Yes')
else:
    print('No')

#2017 캥거루
a = [0]
a[1:] = list(map(int, input().split()))
a[1:] = sorted(a[1:])

if a[2] - a[1] <= a[3] - a[2]:
    print(a[3] - a[2] - 1)
else:
    print(a[2] - a[1] - 1)

'''

#2123 네 개의 정수

#풀이 1
a = list(map(int, input().split()))
a = sorted(a)

if a[1] - a[0] < a[2] - a[1]:
    d = a[1] - a[0]
    res = a[1] + d
elif a[1] - a[0] > a[2] - a[1]:
    d = a[2] - a[1]
    res = a[0] + d
else:
    d = a[1] - a[0]
    res = a[2] + d

print(res)

#풀이 2
a = [0]
a[1:] = list(map(int, input().split()))
a[1:] = sorted(a[1:])

if a[3] - a[2] == a[2] - a[1]:
    print(a[3] + a[2] - a[1])
elif a[3] - a[2] == (a[2] - a[1]) * 2:
    print((a[3] + a[2]) // 2)
else:
    print((a[2] + a[1]) // 2)

#2113 상점

#풀이 1
c = int(input())
n = int(input())
p = [0]
p[1:] = list(map(int, input().split()))
res = list()

for x in p[1:]:
    for y in p[1:]:
        if x + y == c:
            res.append(p.index(x))

for x in res:
    print(x, end = ' ')

#풀이 2
c = int(input())
n = int(input())
a = [0]
a[1:] = list(map(int, input().split()))
isOk = False

for i in range(1, n):
    for j in range(i + 1, n + 1):
        if a[i] + a[j] == c:
            print(i, j)
            isOk = True
            break
    if isOk == True:
        break