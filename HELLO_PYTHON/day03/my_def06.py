def add_min_mul_div(a,b):
    return a + b, a - b, a * b, a / b

def minus(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b
# 멀티리턴의 결과는 튜플의 형태 '()'로 감싸짐 사용은 배열처럼 index
sum= add_min_mul_div(4,5)
print(sum[2])

#min = minus(4,5)
# print(min)

#mul = multiply(4,5)
# print(mul)

#div = divide(4,5)
# print(div)