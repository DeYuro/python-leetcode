t1 = ('Око за око','А роза упала на лапу Азора','Около Миши молоко')

l1 = []

for v in t1:
    k = 0
    j = len(v) - 1
    while k < j:
        if not v[k].isalnum():
            k += 1
            continue
        if not v[j].isalnum():
            j -= 1
            continue

        if v[k].lower() != v[j].lower():
            break
        k += 1
        j -= 1
    else:
        if k <= j:
            l1.append(v)

print(l1)


