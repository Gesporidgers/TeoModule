def numsysCon(a, s):
    result = ''
    while a != 0:
        t = str(a % s)
        result = t + result
        a = a // s
    return result


def zeronumber(a, s):
    t = numsysCon(a, s)
    return t.count('0')


print('---===TeoModule===---')
