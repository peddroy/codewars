n = 12


def factorial(n):
    if 0 <= n <= 12:
        produto = 1
        for i in range(1, n + 1):
            produto = produto * i
        return produto
    else:
        raise ValueError()


print(factorial(n))