# 첫수를 입력하세요 1
# 끝수를 입력하세요 10
# 배수를 입력하세요 5
# 1에서 10까지 5의 배수의 합은 15입니다

firstint = input("첫수를 입력하세요 ")
f = int(firstint)
lastint = input("끝수를 입력하세요 ")
l = int(lastint)
multi = input("배수를 입력하세요 ")
m = int(multi)

sum = 0
for i in range(f, l+1):
    if i % m == 0:
        sum += i
if sum == 0 :
    sum = "없음"
print("{}에서 {}까지 {}의 배수의 합은 {}입니다".format(f,l,m,sum))
