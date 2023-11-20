from random import random

arr = ["1","2","3","4","5","6","7","8","9"]

arr1 = []
for i in range(1,46):
        arr1.append(i)

print("내가 뽑은 로또 번호")
for i in range(0,6):
    rnd1 = int(random()*45)
    print(arr1[rnd1])

for i in range(100):
    rnd = int(random()*9)
    a = arr[0]
    arr[0] = arr[rnd]
    arr[rnd] = a
    
#print(arr[0],arr[1],arr[2])
print(arr1)

arr2 = list(range(1,45+1))