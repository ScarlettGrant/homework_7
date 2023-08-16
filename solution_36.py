def print_operation_table(operation, rows = 6, columns = 6):
    a = [[operation(i, j) for j in range(1, columns + 1)] for i in range(1, rows + 1)]
    for i in a:
        print(*[f"{x:>3}" for x in i])

print_operation_table(lambda x, y: x * y)