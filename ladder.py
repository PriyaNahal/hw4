def my_steps(n):
    if not 1 <= n <= 25:
        raise ValueError("Input is out of bounds, must be between 1 and 25.")

    num1 = 1
    num2 = 2

    if n == 1:
        return 1
    elif n == 2:
        return 2

    for i in range(2, n):
        result = num1 + num2
        num1 = num2
        num2 = result

    return result
