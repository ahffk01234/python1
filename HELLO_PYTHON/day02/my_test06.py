# 출력할 구구단을 넣으세요(2~9) 2
# 2 * 1 = 2
# 2 * 2 = 4
# 2 * 3 = 6
# 2 * 4 = 8
# 2 * 5 = 10
# 2 * 6 = 12
# 2 * 7 = 14
# 2 * 8 = 16
# 2 * 9 = 18

dan = input("출력할 구구단을 넣으세요.(2~9) ")
dantoint = int(dan)
for j in range(1,10):
    print("{} * {} = {}".format(dantoint,j,dantoint*j))
