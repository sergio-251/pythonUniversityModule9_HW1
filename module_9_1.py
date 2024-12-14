def apply_all_func(int_list, *functions):
    try:
        return {i.__name__: i(int_list) for i in functions}
    except TypeError:
        return f'Ошибка: Коллекция {int_list} содержит нечисловые элементы!'

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
print(apply_all_func(['6', 20, 15, 9], max, min))