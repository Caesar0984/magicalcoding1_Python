#1. 다 섯개의 정수가 주어지면 주어진 정수의 누적 결과를 각 줄에 차례대로 출력하는 프로그램을 작성하여라
cnt = 0
total = 0

while cnt < 5:
    try:
        x = int(input('Enter a number:'))
        
        if 0 <= x <= 100:
            total += x
            cnt += 1
            print(total)
        else:
            print('Error')
    
    except: print('Error')
        
#2. 세 개의 정수 A, B, C가 주어지면 주어진 세 수의 총합과 평균을 구하는 프로그램을 작성하여라
A, B, C = map(int, input('Enter three numbers:').split())

if 0 <= A <= 100 and 0 <= B <= 100 and 0 <= C <= 100:
    print('Sum:', (A + B + C))
    print('Average:', round((A + B + C) / 3, 2))
else: print('Error')
