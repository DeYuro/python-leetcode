s1 = 'Hello world'
s2 = 'HelloWorld'


def convert(s):
    stm = str.find(s, ' ')
    if stm > 0:
        return str.upper(s)
    else:
        return str.lower(s)


print(convert(s1))
print(convert(s2))
