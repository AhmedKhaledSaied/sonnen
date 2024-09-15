def fib_generator():
    a = 0
    b = 1
    while True:
        yield a
        tmp = a
        a = b
        b = tmp + b




for num in fib_generator():
    if num > 20:
        break

    print(num)
