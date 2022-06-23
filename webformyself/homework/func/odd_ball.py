def odd_ball(arr):
    try:
        arr.index(arr.index('odd'))
    except ValueError:
        return False

    return True


def odd_ball_inline(arr):
    try:
        return arr.index('odd') in arr
    except ValueError:
        return False


list1 = [
    ["even", 4, "even", 7, "even", 55, "even", 6, "even", 10, "odd", 3, "even"],
    ["even", 4, "even", 7, "even", 55, "even", 6, "even", 9, "odd", 3, "even"],
    ["even", 10, "odd", 2, "even"],
    ["even", 10, "even"],
]

for i in list1:
    print(odd_ball(i))

for i in list1:
    print(odd_ball_inline(i))
