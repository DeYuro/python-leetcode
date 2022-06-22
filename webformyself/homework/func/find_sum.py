# 3 and 5 div
def find_sum(n):
    sum = 0
    for i in range(n + 1):
        if (i % 3 == 0) or (i % 5 == 0):
            sum += i
    return sum


def find_sum_inline(n):
    return sum([v for v in range(n + 1) if v % 3 == 0 or v % 5 == 0])


print(find_sum(5))
print(find_sum(10))

print(find_sum_inline(5))
print(find_sum_inline(10))
