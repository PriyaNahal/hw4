def cacti_number(func):
    def wrapper(plot):
        result = func(plot)
        return result
    return wrapper

@cacti_number
def cacti_number(plot):
    total = 0
    row = len(plot)
    col = len(plot[0])

    for i in range(row):
        for j in range(col):
            if plot[i][j] == 0:
                if i > 0 and plot[i - 1][j] == 1:
                    continue
                if i > 0 and j < col - 1 and plot[i - 1][j + 1] == 1:
                    continue
                if i < row - 1 and j > 0 and plot[i + 1][j - 1] == 1:
                    continue
                if i < row - 1 and plot[i + 1][j] == 1:
                    continue
                if i < row - 1 and j < col - 1 and plot[i + 1][j + 1] == 1:
                    continue
                if j < col - 1 and plot[i][j + 1] == 1:
                    continue

                total += 1
    return total
