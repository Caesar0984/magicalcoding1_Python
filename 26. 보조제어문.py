#1
s = 0

for i in range(1, 101):
    if i % 2 == 0:
        s += i
        print(i, end = ' ')
        if s >= 50:
            break

print()
print(s)
            
#2 
maxv = 0

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    if maxv <= a + b:
        maxv = a + b

print(maxv)

#3
cnt = 0

for i in range(1, 101):
    if i % 2 == 0 or i % 3 == 0:
        continue
    else:
        print(i, end =' ')
        cnt += 1
        if cnt % 10 == 0:
            print()

#1046 행복한 오일러
cnt = 0

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    if a + b >= 8:
        cnt += 1

print(cnt)