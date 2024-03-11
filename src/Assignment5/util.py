def print_format_numbers(n):
    width = len(bin(n)[2:])
    for i in range(1, n + 1):
        print("{:>{width}} {:>{width}o} {:>{width}X} {:>{width}b}".format(i, i, i, i, width=width))
