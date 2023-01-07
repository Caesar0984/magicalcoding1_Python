'''
#1131 디지털 시계
a, b = map(int, input('시간을 입력하시오:').split())
c = int(input('소요 시간을 입력하시오:'))

print((a + ( b + c) // 60) % 24, (b + c) % 60)

#1110 체스판 자르기
n = int(input())
c = n // 2
r = n - c

print((n + 1) * (r + 1))

#1132 햄버거
k, n, m = map(int, input().split())
p = k * n

if p >= m:
    print(p - m)
else:
    print(m - p)
    
#1112 수박
w = int(input('수박의 무게는???'))

if w >= 2 and w % 2 == 0:
    print('Yes')
else:
    print('No')
    
#1133 마법 상자
a, b, c = map(int, input().split())

if a == b == c:
    print(10000 + a * 1000)
elif a == b or c == a:
    print(1000 + a * 100)
elif b == c:
    print(1000 + b * 100)
else:
    if a > b and a > c:
        print(a * 100)
    elif b > a and b > c:
        print(b * 100)
    else:
        print(c * 100)
'''

'''
#1145 철사
N = int(input())

print(sum(range(1, N + 2)) + 1)

#1146 정육각형
x = int(input())

print((6 * sum(range(1, x))) + 1)
'''

'''
'''

