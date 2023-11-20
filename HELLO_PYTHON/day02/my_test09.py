# 예시) 23
# (1~99)숫자를 하나 선택하세요 10
# UP입니다
# (1~99)숫자를 하나 선택하세요 30
# DOWN입니다
# (1~99)숫자를 하나 선택하세요 23
# 정답입니다
from random import random

# 10회 이상 시 Game Over 띄우기

com = int(random()*99)+1
comint = int(com)
result = ""
count = 0
flag_over = False
while(count < 10):
    num = input("(1~99)숫자를 하나 선택하세요 ")
    numint = int(num)
    if comint > numint :
        result = "UP"
        print("{}입니다".format(result))
        count+=1
        continue
    elif comint < numint :
        result = "DOWN"
        print("{}입니다".format(result))
        count+=1
        continue
    else :
        result = "정답"
        print("{}입니다".format(result))
        flag_over = True
        break
    
if not flag_over :
    print("Game Over")