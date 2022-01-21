def numsysCon(number, system):
    result = ''
    while number != 0:
        t = str(number % system)
        result = t + result
        a = number // system
    return result


def zeronumber(number, system):
    t = numsysCon(number, system)
    return t.count('0')


print('---===TeoModule===---')
