from random import random

count = 0

flag = False

val = 0
pos = 0

com = []

for i in range(0,3):
    list = ["1","2","3","4","5","6","7","8","9"]
    rnd = int(random()*9)
    com.append(list[rnd])
    list.remove(list[rnd])
    rnd -= 1

while(count < 10):
    a = input("숫자를 입력해주세요 ")
    aa = []
    for i in a:
        aa.append(i)
    
    for i in range(0,3):
        for j in range(0,3):
            if aa[i] == com[j]:
                if i == j :
                    pos += 1
                else :
                    val += 1
            else:
                continue
    if pos == 3:
        print("성공")
        flag = True
        break
    
    print(aa)
    
    print("{}S{}B".format(pos,val))    
    pos = 0
    val = 0
    count += 1
    
if not flag :
    print("실패")
    
print(com)
