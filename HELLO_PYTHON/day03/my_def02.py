def showDan(dan):
    print("{}단".format(dan))
    for i in range(1,10):
        print("{} * {} = {}".format(dan,i,dan*i))


showDan(3)