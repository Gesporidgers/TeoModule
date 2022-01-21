def numsysCon(number, system):
    """Converts number to a specified number system

    :param number: original number
    :param system: necessary number system
    :return: Conversed number
    """
    result = ''
    while number != 0:
        t = str(number % system)
        result = t + result
        number = number // system
    return result


def zeronumber(number, system):
    """Counts '0' in number in specified number system

    :param number: original number
    :param system: necessary number system
    :return: Quantity '0'
    """
    t = numsysCon(number, system)
    return t.count('0')


print('---===TeoModule===---')
