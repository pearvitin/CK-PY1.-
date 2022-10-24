# Определить, как часто встречается определенная буква в строке.
# TODO посчитать количество каждой буквы в строке в аргументе str_

def get_count_char(str_):
    slowar = {

    }
    for letter in str_.lower():  # sorted(str_.lower()) для сортировки
        counter = 0  # счетчик
        if letter.isalpha():  # проверка букв
            slowar[letter] = slowar.get(letter, counter) + 1  # заполнение словаря
    return slowar


def get_persent_char(dict_):
    counter = sum(dict_.values())  # количество всех букв
    for i in dict_:
        dict_[i] = round(dict_[i] * 100 / counter, 2)  # округление до 2 знаков
    return dict_


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
# print(get_persent_char(slowar)) 
# Если slowar не глобальная, то не могу на нее ссылаться в конце.
# Как решение - очистка словаря на входе в функцию get_count_char(), а slowar оставить глобальной

