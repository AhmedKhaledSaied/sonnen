def fib_generator():
    a = 0
    b = 1
    while True:
        yield a

        a = b
        b = a + b


#for num in fib_generator():
 #   if num > 10:
  #      break

    #print(num)
fib_Gen = fib_generator()
print(fib_Gen)
