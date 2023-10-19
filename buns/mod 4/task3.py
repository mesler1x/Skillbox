def divider(first, second):
    if first == 0:
        return second
    if second == 0:
        return first
    return divider(second, first % second)
