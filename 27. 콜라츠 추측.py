#1
x = int(input())
cnt = 0

while True:
    if x % 2 == 0:
        x /= 2
        cnt += 1
    else:
        x = (x + 1) / 2
        cnt += 1
    if x == 1:
        break

print(cnt)

#1027 우박수

#1
n = int(input())
maxv = n
hscnt = 0
hs = list()

hs.append(n)
hscnt += 1

while n != 1:
    if n % 2 == 0:
        n /= 2
        hs.append(int(n))
        hscnt += 1
    else:
        n = 3 * n + 1
        hs.append(int(n))
        hscnt += 1

    for i in range(1, hscnt):
        if hs[i] >= maxv:
            maxv = hs[i]

print(maxv)

#2
n = int(input())
maxv = n

while n != 1:
    if n % 2 == 0:
        n //= 2
    else:
        n = 3 * n + 1
    if maxv < n:
        maxv = n

print(maxv)