def divide(a):
    try:
        a = 10 / a
    except ZeroDivisionError:
        return "fail"
    return a

print(divide(0))
print(divide(5))
print(divide(10))
print(divide(20))
print(divide(0))