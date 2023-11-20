def add_min_mul_div(a,b):
    return a + b, a - b, a * b, a / b

def minus(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b

sum,min,mul,div = add_min_mul_div(4,5)
print(sum)

#min = minus(4,5)
print(min)

#mul = multiply(4,5)
print(mul)

#div = divide(4,5)
print(div)