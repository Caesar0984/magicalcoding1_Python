'''
#스캐닝 메소드 알고리즘 1
a = [-1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0]
maxv, cnt, flag = 0, 0, 1

for i in range(1, len(a)):
    if a[i] == 1:
        cnt += 1
        if maxv < cnt:
            maxv, lef, rig = cnt, flag, i
    else:
        cnt, flag = 0, i + 1

print(lef, rig)
print(maxv)

#스캐닝 메소드 알고리즘 2
a = [-1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0]
maxv, flag = 0, 1

for i in range(1, len(a)):
    if a[i] == 1:
        if maxv < i - flag + 1:
            maxv, lef, rig = i - flag + 1, flag, i
    else:
        flag = i + 1

print(lef, rig)
print(maxv)

#1
a = [0]
a[1:] = list(map(int, input().split()))
maxv = 0

for i in range(1, 11):
    if a[i - 1] == a[i]:
        cnt += 1
    else:
        cnt = 1
    if maxv < cnt:
        maxv, k = cnt, a[i]

print(k)
print(maxv)

#1078 서로 다른 구슬

#풀이 1
n = int(input())
color = list(map(int, input().split()))
cnt = 0

for i in range(1, n):
    if color[i] != color[i - 1]:
        cnt += 1

print(cnt)

#풀이 2
n = int(input())
a = [0]
a[1:] = list(map(int, input().split()))
cnt = 0

for i in range(2, n + 1):
    if a[i - 1] != a[i]:
        cnt += 1

print(cnt)

#1076 음표

#풀이 1
a = [0]
a[1:] = list(map(int, input().split()))
cnt = 0

for i in range(1, 8):
    if a[i + 1] > a[i]:
        cnt += 1
    elif a[i + 1] < a[i]:
        cnt -= 1
    else:
        pass

if cnt == 7:
    print('ascending')
elif cnt == -7:
    print('descending')
else:
    print('mixed')

#풀이 2
a = [0]
a[1:] = list(map(int, input().split()))
asc, des = 0, 0

for i in range(1, 8):
    if a[i] < a[i + 1]:
        asc += 1

for i in range(1, 8):
    if a[i] > a[i + 1]:
        des += 1

if asc == 7:
    print('ascending')
elif des == -7:
    print('descending')
else:
    print('mixed')

#1125 선물
n = int(input())
a = [0]
cnt = 0

for _ in range(n):
    a.append(input())

for i in range(1, n + 1):
    if a[i - 1] != a[i]:
        cnt += 1

print(cnt + 1)
'''

#2069 아침운동
n = int(input())
a = [0]
cnt, maxv = 0, 0

for _ in range(n):
    x, y = map(int, input().split())
    a.append(x + y)

for x in a[1:]:
    if x == 0:
        cnt += 2
    else:
        cnt = 0
    if maxv < cnt:
        maxv = cnt

print(maxv)