def factorial(num):
    if num == 1:
        return num
    else:
        x = num * factorial(num - 1)

        return x
