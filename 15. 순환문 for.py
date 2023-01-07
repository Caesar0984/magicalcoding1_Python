#1. 한 개의 양의 정수 N이 주어지면 1부터 N까지 출력하는 프로그램을 작성하여라.
N = int(input())

for i in range(N + 1):
    print(i, end = ' ')
#줄 내림 대신에 출력

print('\n')

#2. 한 개의 양의 정수 N이 주어지면 N부터 1까지 출력하는 프로그램을 작성하여라.
N = int(input())

for i in range(N, 0, -1):
    print(i, end = ' ')

print('\n')
    
#3. 두 개의 양의 정수 A와 B가 주어지면 A부터 B까지 출력하는 프로그램을 작성하여라
A, B = map(int, input().split())

if A > B:
    for i in range(B, A + 1):
        print(i, end = ' ')
elif A < B:
    for i in range(A, B + 1):
        print(i, end = ' ')
else:
    print(A)

print('\n')

#4. 두 개의 양의 정수 B와 A가 주어지면 B부터 A까지 출력하는 프로그램을 작성하여라.
A, B = map(int, input().split())

if A > B:
    for i in range(A, B - 1, -1):
        print(i, end = ' ')
elif A < B:
    for i in range(B, A - 1, -1):
        print(i, end = ' ')
else:
    print(A)

print('\n')

#5. 한 개의 양의 정수 N이 주어지면 1부터 N까지의 총합을 구하는 프로그램을 작성하여라.
n = int(input())
sum = 0

for i in range(n + 1):
    sum += i

print(sum, '\n')


#6. 두 개의 양의 정수 A와 B가 주어지면 A부터 B까지의 총합을 구하는 프로그램을 작성하여라.
A, B = map(int, input().split())
sum = 0

if A > B:
    for i in range(B, A + 1):
        sum += i
elif A < B:
    for i in range(A, B + 1):
        sum += i
else:
    print(A)

print(sum)

