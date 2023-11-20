# 첫수를 입력하세요 5
# 끝수를 입력하세요 7
# 5에서 7까지의 합은 18입니다

a = input("첫수를 입력하세요")
i = int(a)
b = input("끝수를 입력하세요")
s = int(b)

#arr = range(i,s+1)

sum = 0
for kidon in range(i,s+1): #arr
    sum += kidon
    
print("{}에서 {}까지의 합은 {}입니다".format(a,b,sum))