for i in range(1, 10):
    for j in range(1, 10):
        print("{b} * {a} = {c}".format(a=i, b=j, c=i * j).center(10, ' '), end='   ')  # len(4 * 5 = 20) =< 10
    else:
        print('\n', end='')  # instead of print('')
