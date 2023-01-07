#1 세 개의 정수 A, B, C가 주어진다. 주어진 세 정수에 대한 사칙 연산을 계산하는 프로그램을 작성하여라.
A, B, C = map(int, input("Enter three integers:").split())
#map함수를 사용하면 함수를 거쳐서 변수를 반환해줌

print(A, '+', B, '+', C, '=', A + B + C)
print(A, '-', B, '-', C, '=', A - B - C)
print(A, '*', B, '*', C, '=', A * B * C)
print(A, '/', B, '/', C, '=', round(A / B / C, 4))

#2 두 개의 단일 문자가 주어진다. 주어진 두 문자의 아스키코드(ASCII Code) 값을 출력하는 프로그램을 작성하여라.
x, y = input().split()

print(x, ord(x), sep = ':')
print(y, ord(y), sep = ':')
#문자열을 공백을 ':'로 채워줌 

#참고: 아스키코드(ASCII Code) 값을 문자로 출력하는 프로그램
a, b = map(int, input().split())

print(a, chr(a), sep = ':')
print(b, chr(b), sep = ':')