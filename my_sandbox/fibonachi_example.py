def fibo_recursion(num):
    if num < 2:
        return num
    return fibo_recursion(num - 1) + fibo_recursion(num - 2)


def fibo_cycle(num):
    fibo = 0
    for n in range(1, num+1):
        fibo = fibo + n
    return fibo


def factorial_cycle(num):
    fact = 1
    for n in range(2, num + 1):
        fact = fact * n
    return fact


def factorial_recursion(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial_recursion(num - 1)


if __name__ == '__main__':
    print(fibo_recursion(10))
    print(fibo_cycle(10))
    # print(factorial_cycle(10))
    # print(factorial_recursion(100000))


