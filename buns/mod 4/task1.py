def characteristic_lst(lst):
    if len(set(lst)) == len(lst):
        return "Все числа разные"
    elif lst.count(lst[0]) == len(lst):
        return "Все числа равны"
    return "Есть равные и неравные числа"
