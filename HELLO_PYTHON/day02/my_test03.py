# 홀/짝을 선택하세요 홀
# 나 : 홀
# 컴 : 홀 짝
# 결과 : 이김 짐
import random

a = input("홀/짝을 선택하세요. ")

print("나 : " + a)
com = ''
rnd = random.random()
if(rnd > 0.5):
    com = "짝"
else :
    com = "홀"

print("컴 : "  + com)
result = ""
if(a == com):
    result = "이김"
else :
    result = "짐"

print("결과 : {}".format(result))
print("rnd : ",rnd)


# b = input("자신의 주사위 숫자를 고르세요. ")
# s = int(b)
#
# rnd1 = random.randint(1,6)
# result1 = ""
# if(s > rnd1):
#     result1 = "이김"
# else :
#     result1 = "짐"
#
# print("결과 : ", result1)