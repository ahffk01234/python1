# 가위/바위/보를 선택하세요 가위
# 나 : 가위
# 컴 : 가위
# 결과 : 비김
from random import random

arr = ["가위", "바위", "보"]
comrcp = int(random()*2)
com = arr[comrcp]
my = input("가위/바위/보를 선택하세요 ")
rcp = 0
result = ""

if my == "가위":
    rcp = 0
elif my == "바위":
    rcp = 1
else :
    rcp = 2
    
if comrcp - rcp == 0:
    result = "비김"
elif comrcp - rcp > 0:
    result = "짐"
else :
    result = "이김"
print("나 : {}".format(my))
print("컴 : {}".format(com))
print("결과 : {}".format(result))

