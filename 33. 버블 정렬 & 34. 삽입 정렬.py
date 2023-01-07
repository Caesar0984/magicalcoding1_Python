#버블 정렬 알고리즘
a = [0, 7, 6, 9, 5, 8]

for i in range(1, 5):
    for j in range(1, 6 - i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

print(a[1:])

#1
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(1, 11):
    for j in range(0, 11 - i):
        if a[j] < a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

print(a[:10])

#삽입 정렬 알고리즘
a = [0, 7, 6, 9, 5, 8]

for i in range(2, 6):
    key = a[i]
    for j in range(i - 1, 0, -1):
        if a[j] <= key:
            break
        a[j + 1] = a[j]
    else:
        j -= 1
    a[j + 1] = key
    
print(a[1:]) 

#1 
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(2, 11):
    key = a[i]
    for j in range(i - 1, 0, -1):
        if a[j] >= key:
            break
        a[j + 1] = a[j]
    else:
        j -= 1
    a[j + 1] = key

print(a[1:11])