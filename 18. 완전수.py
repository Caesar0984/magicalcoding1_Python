'''
1. 어떤 한 개의 양의 정수에 대해서 그 수 자신을 제외한 모든 약수의 합이 그 수 자신과 같은 수를 완전수라고 하고 그 수 자신을 제외한
모든 약수의 합이 그 수 자신보다 작은 수를 부족수라고 한다. 그리고 그 수 자신을 제외한 모든 약수의 합이 그 수 자신보다 큰 수를 과잉수라고 
한다. 한 개의 양의 정수 N이 주어지면 그 수가 완전수인지, 부족수인지, 과잉수인지를 판별하는 프로그램을 작성하여라.
'''
n = int(input())
s = 0

for i in range(1, n):
    if n % i == 0:
        s += i
    else: continue

if n == s:
    print('Perfect')
elif n > s:
    print('Deficient')
else:
    print('Abundant')