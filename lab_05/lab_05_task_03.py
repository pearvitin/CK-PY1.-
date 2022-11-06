# TODO написать функцию для получения списка уникальных целых чисел
import random


def get_unique_list_numbers(len_: int, floor_: int, ceiling_: int) -> list[int]:
    list_unq = []  # пустой словарь
    while len_ != 0:  # заданная длина пароля используется как счетчик вставленных символов
        elem = random.randint(floor_, ceiling_)  # генерация случайного числа
        if elem not in list_unq:  # проверка, если ли элемент в списке
            list_unq.append(elem)  # добавление элемента в список
            len_ -= 1  # счетчик - 1
    return list_unq


list_unique_numbers = get_unique_list_numbers(15, -10, 10)
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))  # проверка на уникальность
