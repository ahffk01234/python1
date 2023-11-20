# 첫별수를 입력하시오 5
# 끝별수를 입력하시오 7

# *****
# ******
# *******

a = input("첫별수를 입력하시오 ")
aa = int(a)
b = input("끝별수를 입력하시오 ")
bb = int(b)

for i in range(aa,bb+1):
    for j in range(0,i):
        print(end="*")
    print()